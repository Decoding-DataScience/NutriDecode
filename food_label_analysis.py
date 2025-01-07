import logging
import os
import numpy as np
from vision_agent.tools import *
from typing import Dict, List, Any
from pillow_heif import register_heif_opener

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

register_heif_opener()

def process_food_label(image_path: str) -> Dict[str, Any]:
    """
    Process food label images to extract nutritional information, ingredients,
    allergens, and eco-impact details.
    
    Args:
        image_path (str): Path to the food label image
        
    Returns:
        Dict[str, Any]: Extracted information from the food label
    """
    try:
        # Verify image exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at path: {image_path}")
            
        # Load the image
        image = load_image(image_path)
        logger.info(f"Successfully loaded image from {image_path}")
        
        # Extract text using OCR
        ocr_results = ocr(image)
        
        # Initialize dictionaries for categorized information
        nutritional_info = {}
        ingredients = []
        allergens = []
        eco_impact = {}
        
        # Process OCR results
        for item in ocr_results:
            text = item['label'].lower()
            
            if 'energy' in text or 'fat' in text or 'carbohydrate' in text or 'protein' in text or 'salt' in text:
                # Process nutritional information
                parts = text.split()
                if len(parts) >= 2:
                    nutritional_info[parts[0]] = ' '.join(parts[1:])
            
            elif 'ingredients' in text:
                # Extract ingredients
                ingredients = [ing.strip() for ing in text.split(':')[1].split(',')]
            
            elif 'allergens' in text or 'contains' in text:
                # Extract allergens
                allergens = [allergen.strip() for allergen in text.split(':')[1].split(',')]
            
            elif 'recycled' in text or 'plastic' in text or 'bottle' in text:
                # Extract eco-impact information
                eco_impact['packaging'] = text
        
        # Use VQA for any missing or unclear information
        vqa_prompt = "What are the main nutritional facts, ingredients, allergens, and eco-impact details on this label?"
        vqa_result = qwen2_vl_images_vqa(vqa_prompt, [image])
        
        # Process VQA result to fill in any gaps
        vqa_lines = vqa_result.split('\n')
        for line in vqa_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key == 'ingredients' and not ingredients:
                    ingredients = [ing.strip() for ing in value.split(',')]
                elif key == 'allergens' and not allergens:
                    allergens = [allergen.strip() for allergen in value.split(',')]
                elif key == 'eco-impact details' and not eco_impact:
                    eco_impact['details'] = value
        
    except Exception as e:
        logger.error(f"Error processing food label: {str(e)}")
        raise

    return {
        'nutritional_info': nutritional_info,
        'ingredients': ingredients,
        'allergens': allergens,
        'eco_impact': eco_impact
    }

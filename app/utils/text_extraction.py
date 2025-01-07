import os
from typing import Dict, List
from pillow_heif import register_heif_opener
register_heif_opener()

from vision_agent.tools import load_image, ocr, qwen2_vl_images_vqa

def extract_text_from_label(image_path: str) -> Dict[str, any]:
    """Extract text information from food label image."""
    image = load_image(image_path)
    ocr_results = ocr(image)
    
    nutritional_info = {}
    ingredients = []
    allergens = []
    eco_impact = {}
    
    for item in ocr_results:
        text = item['label'].lower()
        process_text_segment(text, nutritional_info, ingredients, allergens, eco_impact)
    
    # Fill gaps with VQA
    vqa_data = get_vqa_information(image)
    merge_vqa_data(vqa_data, ingredients, allergens, eco_impact)
    
    return {
        'nutritional_info': nutritional_info,
        'ingredients': ingredients,
        'allergens': allergens,
        'eco_impact': eco_impact
    }

def process_text_segment(text: str, nutritional_info: dict, ingredients: list, 
                        allergens: list, eco_impact: dict) -> None:
    """Process individual text segments from OCR results."""
    if any(nutrient in text for nutrient in ['energy', 'fat', 'carbohydrate', 'protein', 'salt']):
        parts = text.split()
        if len(parts) >= 2:
            nutritional_info[parts[0]] = ' '.join(parts[1:])
    
    elif 'ingredients' in text:
        ingredients.extend([ing.strip() for ing in text.split(':')[1].split(',')])
    
    elif 'allergens' in text or 'contains' in text:
        allergens.extend([allergen.strip() for allergen in text.split(':')[1].split(',')])
    
    elif any(eco_term in text for eco_term in ['recycled', 'plastic', 'bottle']):
        eco_impact['packaging'] = text

def get_vqa_information(image) -> str:
    """Get additional information using VQA."""
    vqa_prompt = "What are the main nutritional facts, ingredients, allergens, and eco-impact details on this label?"
    return qwen2_vl_images_vqa(vqa_prompt, [image])

def merge_vqa_data(vqa_result: str, ingredients: list, allergens: list, eco_impact: dict) -> None:
    """Merge VQA results with existing data."""
    vqa_lines = vqa_result.split('\n')
    for line in vqa_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()
            
            if key == 'ingredients' and not ingredients:
                ingredients.extend([ing.strip() for ing in value.split(',')])
            elif key == 'allergens' and not allergens:
                allergens.extend([allergen.strip() for allergen in value.split(',')])
            elif key == 'eco-impact details' and not eco_impact:
                eco_impact['details'] = value 
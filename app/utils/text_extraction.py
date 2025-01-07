import os
from typing import Dict, List
from pillow_heif import register_heif_opener
import logging
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

# Configure basic logging
logger = logging.getLogger(__name__)

register_heif_opener()

from vision_agent.tools import load_image, ocr, qwen2_vl_images_vqa
from .ai_client import AIClient
import json

# Initialize the Computer Vision client
computervision_client = ComputerVisionClient(
    endpoint=os.getenv('AZURE_VISION_ENDPOINT'),
    credentials=CognitiveServicesCredentials(os.getenv('AZURE_VISION_KEY'))
)

async def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an image using Azure Computer Vision API.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Extracted text from the image
    """
    try:
        # Open and read the image file
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            
        # Process with Computer Vision
        result = await computervision_client.read_in_stream(image_data)
        # Rest of the function...
        
    except Exception as e:
        logger.error(f"Error extracting text from image: {str(e)}")
        raise

async def extract_text_from_label(image_path: str) -> dict:
    """Extract information from food label using OpenAI Vision."""
    ai_client = AIClient()
    
    try:
        # Get AI analysis
        analysis_text = await ai_client.analyze_food_label(image_path)
        
        # Parse the response into structured data
        # Note: This assumes OpenAI returns data in a parseable format
        try:
            # First try to parse as JSON if AI returned structured data
            data = json.loads(analysis_text)
        except json.JSONDecodeError:
            # Fallback to basic text parsing if not JSON
            data = parse_unstructured_text(analysis_text)
            
        return {
            'nutritional_info': data.get('nutritional_info', {}),
            'ingredients': data.get('ingredients', []),
            'allergens': data.get('allergens', []),
            'eco_impact': data.get('eco_impact', {})
        }
    except Exception as e:
        logger.error(f"Error analyzing food label: {str(e)}")
        raise

def parse_unstructured_text(text: str) -> dict:
    """Parse unstructured text response into structured data."""
    # Basic parsing logic - you might need to enhance this based on actual responses
    sections = {
        'nutritional_info': {},
        'ingredients': [],
        'allergens': [],
        'eco_impact': {}
    }
    
    current_section = None
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        # Identify sections
        if 'nutrition' in line.lower():
            current_section = 'nutritional_info'
        elif 'ingredient' in line.lower():
            current_section = 'ingredients'
        elif 'allergen' in line.lower():
            current_section = 'allergens'
        elif 'eco' in line.lower() or 'sustainability' in line.lower():
            current_section = 'eco_impact'
        elif current_section:
            # Add content to appropriate section
            if current_section == 'nutritional_info':
                # Parse nutrition facts
                if ':' in line:
                    key, value = line.split(':', 1)
                    sections['nutritional_info'][key.strip()] = value.strip()
            elif current_section in ['ingredients', 'allergens']:
                sections[current_section].extend([i.strip() for i in line.split(',')])
            elif current_section == 'eco_impact':
                sections['eco_impact']['details'] = line

    return sections 
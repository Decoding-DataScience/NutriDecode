from app.utils.text_extraction import extract_text_from_label
from app.models.food_label_model import FoodLabel

def process_food_label(image_path: str) -> FoodLabel:
    """Main function to process food label images."""
    extracted_data = extract_text_from_label(image_path)
    return FoodLabel.from_dict(extracted_data) 
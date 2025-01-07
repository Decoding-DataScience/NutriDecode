from openai import OpenAI
from base64 import b64encode
from .config import Config
from PIL import Image
import io

class AIClient:
    def __init__(self):
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def encode_image(self, image_path):
        with Image.open(image_path) as img:
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Convert to JPEG bytes
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG')
            return b64encode(buffer.getvalue()).decode('utf-8')

    async def analyze_food_label(self, image_path):
        """
        Analyze food label using OpenAI's Vision model
        """
        base64_image = self.encode_image(image_path)

        response = self.client.chat.completions.create(
            model=Config.VISION_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """You are a nutrition expert analyzing food labels. 
                    Extract and structure the following information:
                    - Nutritional facts (calories, protein, carbs, fat, etc.)
                    - Ingredients list
                    - Allergens
                    - Any eco-impact or sustainability information"""
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please analyze this food label and provide structured information:"
                        },
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    ]
                }
            ],
            max_tokens=Config.MAX_TOKENS,
            temperature=Config.TEMPERATURE
        )

        return response.choices[0].message.content 
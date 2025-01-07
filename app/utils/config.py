import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    VISION_MODEL = os.getenv('VISION_MODEL', 'gpt-4-vision-preview')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '1000'))
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in environment variables") 
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Initialize the client
credentials = CognitiveServicesCredentials('your-key')
client = ComputerVisionClient(credentials, 'your-endpoint')

# For image_data, prepare your image
image_data = None  # Replace with your image data source 
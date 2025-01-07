import { ComputerVisionClient } from '@azure/cognitiveservices-computervision';
import { ApiKeyCredentials } from '@azure/ms-rest-js';

const credentials = new ApiKeyCredentials({ inHeader: { 'Ocp-Apim-Subscription-Key': 'your-key' } });
const client = new ComputerVisionClient(credentials, 'your-endpoint');

const imageData = null; // Replace with your image data source 
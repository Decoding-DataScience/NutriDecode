import { AnalyzeRequest, ApiResponse, NutritionResponse } from '@/types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:3000/api';

export const analyzeFood = async (
  request: AnalyzeRequest
): Promise<ApiResponse<NutritionResponse>> => {
  try {
    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      return {
        error: {
          message: 'Failed to analyze food',
          status: response.status,
        },
      };
    }

    const data = await response.json();
    return { data };
  } catch (error) {
    return {
      error: {
        message: error instanceof Error ? error.message : 'An unknown error occurred',
        status: 500,
      },
    };
  }
};

export const analyzeImage = async (imageData: string): Promise<NutritionResponse> => {
  try {
    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ image: imageData }),
    });

    if (!response.ok) {
      throw new Error('Analysis failed');
    }

    return response.json();
  } catch (error) {
    throw new Error('Failed to analyze image');
  }
}; 
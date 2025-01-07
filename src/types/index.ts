// API Response Types
export interface NutritionResponse {
  calories: number;
  protein: number;
  carbs: number;
  fat: number;
  recommendations: string[];
}

export interface Nutrient {
  name: string;
  amount: number;
  unit: string;
  percentOfDailyNeeds: number;
}

// API Request Types
export interface AnalyzeRequest {
  text: string;
}

// Common Types
export interface ApiError {
  message: string;
  status: number;
}

export interface ApiResponse<T> {
  data?: T;
  error?: ApiError;
} 
'use client';

import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { analyzeImage } from '@/lib/api';
import { NutritionResponse } from '@/types';
import { Upload, Camera } from 'lucide-react';

export default function Home() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [nutritionData, setNutritionData] = useState<NutritionResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onloadend = () => {
      setSelectedImage(reader.result as string);
    };
    reader.readAsDataURL(file);
  };

  const handleAnalyze = async () => {
    if (!selectedImage) return;

    setIsLoading(true);
    setError(null);

    try {
      const data = await analyzeImage(selectedImage);
      setNutritionData(data);
    } catch (err) {
      setError("Failed to analyze image. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-4 md:p-8 bg-gray-50">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8">NutriDecode</h1>
        
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex flex-col items-center gap-6">
            {/* Image Upload Section */}
            <div className="w-full max-w-md">
              <label className="block text-center">
                <Button
                  variant="outline"
                  className="w-full h-32 border-dashed"
                  onClick={() => document.getElementById('imageInput')?.click()}
                >
                  {selectedImage ? (
                    <img
                      src={selectedImage}
                      alt="Preview"
                      className="max-h-28 object-contain"
                    />
                  ) : (
                    <div className="flex flex-col items-center">
                      <Upload className="h-8 w-8 mb-2" />
                      <span>Upload Food Image</span>
                    </div>
                  )}
                </Button>
                <input
                  id="imageInput"
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleImageUpload}
                />
              </label>
            </div>

            {/* Camera Button */}
            <Button
              variant="secondary"
              className="flex items-center gap-2"
              onClick={() => document.getElementById('imageInput')?.click()}
            >
              <Camera className="h-4 w-4" />
              Take Photo
            </Button>

            {/* Analyze Button */}
            <Button
              onClick={handleAnalyze}
              disabled={!selectedImage || isLoading}
              className="w-full max-w-md"
            >
              {isLoading ? 'Analyzing...' : 'Analyze Image'}
            </Button>

            {/* Error Message */}
            {error && (
              <div className="text-red-500 text-center">{error}</div>
            )}

            {/* Results Section */}
            {nutritionData && (
              <div className="w-full max-w-md bg-gray-50 p-4 rounded-lg">
                <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
                <div className="space-y-4">
                  <div>
                    <h3 className="font-medium">Nutrition Information</h3>
                    <div className="grid grid-cols-2 gap-2 mt-2">
                      <div>Calories: {nutritionData.calories}</div>
                      <div>Protein: {nutritionData.protein}g</div>
                      <div>Carbs: {nutritionData.carbs}g</div>
                      <div>Fat: {nutritionData.fat}g</div>
                    </div>
                  </div>
                  
                  <div>
                    <h3 className="font-medium">Recommendations</h3>
                    <ul className="list-disc list-inside mt-2">
                      {nutritionData.recommendations.map((rec, index) => (
                        <li key={index}>{rec}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
} 
"use client";

import React, { useState } from "react";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Upload } from "lucide-react";
import axios from "axios";
import { useToast } from "@/components/ui/use-toast";

export default function Home() {
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState<any>(null);
  const { toast } = useToast();

  const handleImageSelect = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Preview
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreviewUrl(reader.result as string);
    };
    reader.readAsDataURL(file);

    // Upload and analyze
    try {
      setIsLoading(true);
      const formData = new FormData();
      formData.append("image", file);

      const response = await axios.post("/api/analyze", formData);
      setResults(response.data);
      
      toast({
        title: "Analysis Complete",
        description: "Your food image has been successfully analyzed.",
      });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to analyze image. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-8">
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
                  {previewUrl ? (
                    <img
                      src={previewUrl}
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
                  onChange={handleImageSelect}
                />
              </label>
            </div>

            {/* Results Section */}
            {isLoading && (
              <div className="text-center">
                <p>Analyzing your food image...</p>
              </div>
            )}

            {results && !isLoading && (
              <div className="w-full">
                <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
                {/* Add your results display logic here */}
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}

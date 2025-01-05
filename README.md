# NutriDecode+

**Project Statistics:**
- Total Lines of Code: 815 (Python: 500, JSON: 215, Markdown: 100)
- Total Lines of Documentation: 600 (README, instructions, guides, and templates)

NutriDecode+ is an advanced system designed to empower users to make better food-related decisions. By leveraging AI, it provides detailed insights on food labels, assesses produce quality, and evaluates the environmental impact of food items. The system also suggests healthier and sustainable alternatives.

## Features

### Core Functionality
- **Food Label Analysis**
  - Extracts nutritional facts, allergens, and ingredient details.
  - Highlights additives and preservatives.
  - Recommends healthier options.
  
- **Produce Quality Assessment**
  - Provides tips for identifying freshness and ripeness.
  - Suggests optimal storage practices for extended shelf life.

- **Eco-Impact Evaluation**
  - Assesses the carbon footprint of products.
  - Recommends eco-friendly packaging alternatives.

### Data Management
- Structured JSON data storage for consistency.
- Automatic data validation using pre-defined schemas.
- Comprehensive logging system to track processes and errors.

### Command System
- **UPLOAD**: Add food label or produce images for analysis.
- **GENERATE**: Create eco-impact or nutritional reports.
- **SAVE**: Save session data for later use.
- **EXIT**: End the session safely while saving progress.

## Installation

1. Clone the repository using:
   ```
   git clone https://github.com/yourusername/NutriDecode.git
   cd NutriDecode
   ```

2. Ensure Python 3.x is installed.

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

NutriDecode+ is organized into modules for seamless operation:

- `food_label_analysis.py`: Main script for analyzing food labels.
- `eco_impact_calculator.py`: Module for evaluating environmental impact.
- `data/`: Contains sample data, templates, and user session records.
- `logs/`: Stores system operation logs and error reports.
- `docs/`: Includes guides, FAQs, and supporting documentation.

## Usage

### Food Label Analysis
- Upload an image of a food label for processing.
- The system extracts:
  - Nutritional facts (calories, fats, proteins, etc.).
  - Allergens and ingredients.
  - Eco-impact information on packaging materials.
- Recommendations for healthier options are provided.

### Produce Quality Assessment
- Follow the guidance in `Produce_Quality_Guide.txt` for assessing the ripeness and freshness of produce.
- Includes storage advice to maintain quality.

### Eco-Impact Evaluation
- Input the product name into the system to get an eco-impact assessment.
- Outputs include:
  - Carbon footprint rating.
  - Suggestions for sustainable alternatives.

## System Features

### Progress Management
- Save and resume sessions anytime.
- Files are saved with timestamps for easy version control.

### Logging and Error Handling
- Real-time operation logging.
- Detailed error tracking for debugging and user feedback.

### Validation and Security
- Data is validated against a robust schema.
- Secure storage of user sessions and analysis results.

## Recent Changes

- Enhanced OCR capabilities for better text extraction from food labels.
- Added support for real-time eco-impact assessments.
- Improved user interface for produce quality guidance.
- Updated documentation with new usage examples and best practices.

## Planned Improvements

- Advanced allergen detection using machine learning.
- Integration with global food databases for deeper insights.
- Multi-language support to reach a broader audience.

## Best Practices

- Save session progress frequently to avoid data loss.
- Use clear, high-resolution images for food label analysis.
- Validate eco-impact recommendations with reliable sources.

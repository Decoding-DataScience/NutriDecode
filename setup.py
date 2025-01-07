import os

def create_project_structure():
    # Define the directory structure
    directories = [
        "NutriDecode/app/utils",
        "NutriDecode/app/models",
        "NutriDecode/app/static/schemas",
        "NutriDecode/app/static/logs",
        "NutriDecode/tests/test_utils",
        "NutriDecode/tests/data",
        "NutriDecode/docs/templates"
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create initial files
    files = [
        "NutriDecode/app/__init__.py",
        "NutriDecode/app/main.py",
        "NutriDecode/app/commands.py",
        "NutriDecode/requirements.txt",
        "NutriDecode/README.md"
    ]
    
    for file in files:
        with open(file, 'a') as f:
            pass  # Just create empty files
        print(f"Created file: {file}")

if __name__ == "__main__":
    create_project_structure() 
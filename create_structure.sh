#!/bin/bash

# Create base directories
mkdir -p nutridecode-frontend/src/components/ui
mkdir -p nutridecode-frontend/src/lib

# Create essential component directories
mkdir -p src/components/{ui,layout,shared}

# Create base files
touch src/types/index.ts
touch src/utils/index.ts
touch src/hooks/index.ts

# Create basic layout component
touch src/components/layout/RootLayout.tsx

echo "Project structure created successfully!"
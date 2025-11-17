#!/bin/bash

echo "🔍 Starting CI/CD checks..."

# Проверка Python файлов
echo "1. Checking Python syntax..."
python -m py_compile generate_data.py export_to_formats.py main.py

# Генерация данных
echo "2. Generating data..."
python generate_data.py

# Экспорт форматов  
echo "3. Exporting formats..."
python export_to_formats.py

# Проверка файлов
echo "4. Checking output files..."
files=("oceanworld_data.xlsx" "oceanworld_report.html" "oceanworld_report.php" "oceanworld_data.xml")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists ($(wc -c < "$file") bytes)"
    else
        echo "❌ $file missing!"
        exit 1
    fi
done

echo "🎉 CI/CD checks passed!"
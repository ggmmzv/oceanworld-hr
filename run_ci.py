import os
import sys
import subprocess
from pathlib import Path

def run_ci_checks():
    print("🚀 Running CI/CD checks for OceanWorld HR...")
    
    # 1. Проверка существования файлов
    required_files = [
        'generate_data.py',
        'export_to_formats.py', 
        'main.py'
    ]
    
    print("\n1. Checking required files...")
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - MISSING!")
            return False
    
    # 2. Генерация данных
    print("\n2. Generating test data...")
    try:
        subprocess.run([sys.executable, "generate_data.py"], check=True)
        print("   ✅ Data generation successful")
    except subprocess.CalledProcessError:
        print("   ❌ Data generation failed")
        return False
    
    # 3. Экспорт в форматы
    print("\n3. Exporting to formats...")
    try:
        subprocess.run([sys.executable, "export_to_formats.py"], check=True)
        print("   ✅ Format export successful")
    except subprocess.CalledProcessError:
        print("   ❌ Format export failed")
        return False
    
    # 4. Проверка сгенерированных файлов
    print("\n4. Validating output files...")
    output_files = [
        'oceanworld_data.xlsx',
        'oceanworld_report.html',
        'oceanworld_report.php', 
        'oceanworld_data.xml'
    ]
    
    all_files_exist = True
    for file in output_files:
        if os.path.exists(file):
            file_size = os.path.getsize(file)
            print(f"   ✅ {file} ({file_size} bytes)")
        else:
            print(f"   ❌ {file} - NOT FOUND!")
            all_files_exist = False
    
    # 5. Базовая валидация контента
    print("\n5. Basic content validation...")
    
    # Проверка HTML
    if os.path.exists('oceanworld_report.html'):
        with open('oceanworld_report.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
            if '<title>Учет кадров - Мир океана</title>' in html_content:
                print("   ✅ HTML title correct")
            else:
                print("   ❌ HTML title missing")
    
    # Проверка XML структуры
    if os.path.exists('oceanworld_data.xml'):
        with open('oceanworld_data.xml', 'r', encoding='utf-8') as f:
            xml_content = f.read()
            if '<?xml version="1.0" encoding="UTF-8"?>' in xml_content:
                print("   ✅ XML declaration present")
            else:
                print("   ❌ XML declaration missing")
    
    # 6. Проверка зависимостей
    print("\n6. Checking dependencies...")
    try:
        import pandas
        import openpyxl 
        import faker
        import jinja2
        print("   ✅ All dependencies installed")
    except ImportError as e:
        print(f"   ❌ Missing dependency: {e}")
        return False
    
    print("\n🎉 All CI checks passed! Ready to commit.")
    return True

if __name__ == "__main__":
    success = run_ci_checks()
    sys.exit(0 if success else 1)
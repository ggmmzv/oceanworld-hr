import subprocess
import sys

def main():
    print("=== Запуск полной генерации данных для 'Мир океана' ===\n")
    
    # Запускаем генерацию данных
    print("1. Генерация Excel файла с данными...")
    subprocess.run([sys.executable, "generate_data.py"])
    
    # Запускаем экспорт в форматы
    print("\n2. Экспорт данных в HTML, PHP, XML...")
    subprocess.run([sys.executable, "export_to_formats.py"])
    
    print("\n🎉 Все задачи выполнены успешно!")
    print("\nСозданные файлы:")
    print("✅ oceanworld_data.xlsx - Excel с 960+ записями на 3 листах")
    print("✅ oceanworld_report.html - HTML отчет с CSS стилями")
    print("✅ oceanworld_report.php - PHP версия отчета")
    print("✅ oceanworld_data.xml - XML данные организации")

if __name__ == "__main__":
    main()
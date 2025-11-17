import pandas as pd
from jinja2 import Template
import os
from datetime import datetime

def read_excel_data():
    """Чтение данных из Excel файла"""
    print("Чтение данных из Excel...")
    
    employees = pd.read_excel('oceanworld_data.xlsx', sheet_name='Сотрудники')
    animals = pd.read_excel('oceanworld_data.xlsx', sheet_name='Морские обитатели')
    equipment = pd.read_excel('oceanworld_data.xlsx', sheet_name='Оборудование')
    
    return employees, animals, equipment

def create_css_styles():
    """Создание CSS стилей"""
    css = """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f8ff; /* Бледный светлый голубой */
            color: #2c3e50; /* Темно-синий текст */
            line-height: 1.6;
        }
        
        .header {
            background: linear-gradient(135deg, #1e90ff, #00bfff);
            color: white;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .nav {
            background-color: #4682b4;
            padding: 15px 0;
            text-align: center;
        }
        
        .nav a {
            color: white;
            text-decoration: none;
            margin: 0 20px;
            font-weight: 600;
            font-size: 1.1em;
            transition: color 0.3s;
        }
        
        .nav a:hover {
            color: #ffeb3b;
            text-decoration: underline;
        }
        
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #1e90ff;
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 20px;
            border-bottom: 3px solid #1e90ff;
            padding-bottom: 10px;
        }
        
        h3 {
            color: #4682b4;
            font-size: 1.5em;
            font-weight: 600;
            margin: 20px 0 10px 0;
        }
        
        .employee-card, .animal-card, .equipment-card {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            transition: transform 0.2s;
        }
        
        .employee-card:hover, .animal-card:hover, .equipment-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            display: block;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }
        
        th {
            background-color: #1e90ff;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }
        
        td {
            padding: 10px 12px;
            border-bottom: 1px solid #ddd;
        }
        
        tr:hover {
            background-color: #f5f5f5;
        }
        
        .ocean-image {
            width: 300px;
            height: 200px;
            object-fit: cover;
            border-radius: 8px;
            margin: 10px;
            border: 3px solid #1e90ff;
        }
        
        .image-gallery {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin: 20px 0;
        }
        
        .footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 30px 0;
            margin-top: 40px;
        }
        
        .footer a {
            color: #1e90ff;
            text-decoration: none;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
        
        .department-badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 15px;
            color: white;
            font-weight: bold;
            font-size: 0.9em;
        }
        
        .aquarium { background: #e74c3c; }
        .science { background: #3498db; }
        .logistics { background: #2ecc71; }
        .admin { background: #9b59b6; }
        .maintenance { background: #f39c12; }
        .excursion { background: #1abc9c; }
    </style>
    """
    return css

def generate_html(employees, animals, equipment):
    """Генерация HTML файла"""
    print("Генерация HTML файла...")
    
    template_str = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Учет кадров - Мир океана</title>
    {{ css_styles }}
</head>
<body>
    <header class="header">
        <h1>🌊 Мир океана</h1>
        <p>Система учета кадров и ресурсов</p>
    </header>
    
    <nav class="nav">
        <a href="#employees">Сотрудники</a>
        <a href="#animals">Морские обитатели</a>
        <a href="#equipment">Оборудование</a>
        <a href="#stats">Статистика</a>
        <a href="#contacts">Контакты</a>
    </nav>
    
    <div class="container">
        <section id="stats">
            <h2>📊 Статистика организации</h2>
            <div class="stats">
                <div class="stat-card">
                    <span class="stat-number">{{ employees_count }}</span>
                    <span>Сотрудников</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{{ animals_count }}</span>
                    <span>Морских обитателей</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{{ equipment_count }}</span>
                    <span>Единиц оборудования</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{{ departments_count }}</span>
                    <span>Отделов</span>
                </div>
            </div>
        </section>
        
        <section id="employees">
            <h2>👥 Сотрудники организации</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>ФИО</th>
                        <th>Должность</th>
                        <th>Отдел</th>
                        <th>Зарплата</th>
                        <th>Стаж</th>
                    </tr>
                </thead>
                <tbody>
                    {% for emp in employees %}
                    <tr>
                        <td>{{ emp.ID }}</td>
                        <td><strong>{{ emp.ФИО }}</strong></td>
                        <td>{{ emp.Должность }}</td>
                        <td>
                            <span class="department-badge {{ emp.Отдел|replace(' ', '')|lower }}">
                                {{ emp.Отдел }}
                            </span>
                        </td>
                        <td>{{ "%.2f"|format(emp.Зарплата) }} руб.</td>
                        <td>{{ emp.Стаж_лет }} лет</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </section>
        
        <section id="animals">
            <h2>🐠 Морские обитатели</h2>
            <div class="image-gallery">
                <img src="https://via.placeholder.com/300x200/1e90ff/white?text=Дельфин" alt="Дельфин" class="ocean-image">
                <img src="https://via.placeholder.com/300x200/4682b4/white?text=Акула" alt="Акула" class="ocean-image">
                <img src="https://via.placeholder.com/300x200/00bfff/white?text=Черепаха" alt="Черепаха" class="ocean-image">
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Вид</th>
                        <th>Кличка</th>
                        <th>Возраст</th>
                        <th>Вес</th>
                        <th>Статус</th>
                    </tr>
                </thead>
                <tbody>
                    {% for animal in animals %}
                    <tr>
                        <td>{{ animal.ID }}</td>
                        <td><strong>{{ animal.Вид }}</strong></td>
                        <td>{{ animal.Кличка }}</td>
                        <td>{{ animal.Возраст_лет }} лет</td>
                        <td>{{ animal.Вес_кг }} кг</td>
                        <td>{{ animal.Статус }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </section>
        
        <section id="equipment">
            <h2>⚙️ Оборудование</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Тип оборудования</th>
                        <th>Модель</th>
                        <th>Статус</th>
                        <th>Местоположение</th>
                        <th>Стоимость</th>
                    </tr>
                </thead>
                <tbody>
                    {% for eq in equipment %}
                    <tr>
                        <td>{{ eq.ID }}</td>
                        <td><strong>{{ eq.Тип_оборудования }}</strong></td>
                        <td>{{ eq.Модель }}</td>
                        <td>{{ eq.Статус }}</td>
                        <td>{{ eq.Местоположение }}</td>
                        <td>{{ eq.Стоимость_руб }} руб.</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </section>
    </div>
    
    <footer class="footer" id="contacts">
        <p>🌊 <strong>Мир океана</strong> - Организация по изучению и сохранению морской среды</p>
        <p>📞 Телефон: +7 (495) 123-45-67 | ✉️ Email: info@oceanworld.ru</p>
        <p>📍 Адрес: г. Москва, ул. Океанская, д. 1</p>
        <p>© 2024 Мир океана. Все права защищены.</p>
        <p>
            <a href="#">Политика конфиденциальности</a> | 
            <a href="#">Условия использования</a> | 
            <a href="#">Карта сайта</a>
        </p>
    </footer>
</body>
</html>
    """
    
    template = Template(template_str)
    css_styles = create_css_styles()
    
    html_content = template.render(
        css_styles=css_styles,
        employees=employees.to_dict('records'),
        animals=animals.to_dict('records'),
        equipment=equipment.to_dict('records'),
        employees_count=len(employees),
        animals_count=len(animals),
        equipment_count=len(equipment),
        departments_count=6
    )
    
    with open('oceanworld_report.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("HTML файл 'oceanworld_report.html' создан!")

def generate_php(employees, animals, equipment):
    """Генерация PHP файла"""
    print("Генерация PHP файла...")
    
    php_template = """
<?php
// Ocean World - HR Management System
$page_title = "Учет кадров - Мир океана";
$current_year = date('Y');

// Данные сотрудников
$employees = {{ employees_data }};

// Данные морских обитателей  
$animals = {{ animals_data }};

// Данные оборудования
$equipment = {{ equipment_data }};

function getDepartmentClass($dept) {
    $classes = [
        'Аквариумистика' => 'aquarium',
        'Научный отдел' => 'science', 
        'Логистика' => 'logistics',
        'Администрация' => 'admin',
        'Обслуживание' => 'maintenance',
        'Экскурсионный отдел' => 'excursion'
    ];
    return $classes[$dept] ?? 'default';
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $page_title; ?></title>
    <?php include 'styles.css'; ?>
</head>
<body>
    <header class="header">
        <h1>🌊 Мир океана</h1>
        <p>PHP система учета кадров</p>
    </header>
    
    <nav class="nav">
        <a href="#employees">Сотрудники (<?php echo count($employees); ?>)</a>
        <a href="#animals">Обитатели (<?php echo count($animals); ?>)</a>
        <a href="#equipment">Оборудование (<?php echo count($equipment); ?>)</a>
    </nav>
    
    <div class="container">
        <h2>Статистика организации</h2>
        <div class="stats">
            <div class="stat-card">
                <span class="stat-number"><?php echo count($employees); ?></span>
                <span>Сотрудников</span>
            </div>
            <div class="stat-card">
                <span class="stat-number"><?php echo count($animals); ?></span>
                <span>Морских обитателей</span>
            </div>
        </div>
        
        <section id="employees">
            <h2>Сотрудники</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>ФИО</th>
                        <th>Должность</th>
                        <th>Отдел</th>
                        <th>Зарплата</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($employees as $emp): ?>
                    <tr>
                        <td><?php echo $emp['ID']; ?></td>
                        <td><strong><?php echo $emp['ФИО']; ?></strong></td>
                        <td><?php echo $emp['Должность']; ?></td>
                        <td>
                            <span class="department-badge <?php echo getDepartmentClass($emp['Отдел']); ?>">
                                <?php echo $emp['Отдел']; ?>
                            </span>
                        </td>
                        <td><?php echo number_format($emp['Зарплата'], 2); ?> руб.</td>
                    </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </section>
    </div>
    
    <footer class="footer">
        <p>© <?php echo $current_year; ?> Мир океана. Все права защищены.</p>
        <p>Разработано на PHP | Время генерации: <?php echo date('d.m.Y H:i:s'); ?></p>
    </footer>
</body>
</html>
    """
    
    # Конвертируем данные в PHP-массивы
    employees_php = "array(\n"
    for _, emp in employees.head(50).iterrows():  # Берем только первые 50 для примера
        employees_php += f"    array('ID' => {emp['ID']}, 'ФИО' => '{emp['ФИО']}', 'Должность' => '{emp['Должность']}', 'Отдел' => '{emp['Отдел']}', 'Зарплата' => {emp['Зарплата']}),\n"
    employees_php += ")"
    
    animals_php = "array(\n"
    for _, animal in animals.head(30).iterrows():
        animals_php += f"    array('ID' => {animal['ID']}, 'Вид' => '{animal['Вид']}', 'Кличка' => '{animal['Кличка']}', 'Возраст_лет' => {animal['Возраст_лет']}),\n"
    animals_php += ")"
    
    equipment_php = "array(\n"
    for _, eq in equipment.head(30).iterrows():
        equipment_php += f"    array('ID' => {eq['ID']}, 'Тип_оборудования' => '{eq['Тип_оборудования']}', 'Модель' => '{eq['Модель']}', 'Статус' => '{eq['Статус']}'),\n"
    equipment_php += ")"
    
    php_content = Template(php_template).render(
        employees_data=employees_php,
        animals_data=animals_php,
        equipment_data=equipment_php
    )
    
    with open('oceanworld_report.php', 'w', encoding='utf-8') as f:
        f.write(php_content)
    
    print("PHP файл 'oceanworld_report.php' создан!")

def generate_xml(employees, animals, equipment):
    """Генерация XML файла"""
    print("Генерация XML файла...")
    
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<oceanworld_organization>')
    xml_content.append('  <metadata>')
    xml_content.append('    <title>Учет кадров - Мир океана</title>')
    xml_content.append('    <generated_date>' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '</generated_date>')
    xml_content.append('    <total_records>' + str(len(employees) + len(animals) + len(equipment)) + '</total_records>')
    xml_content.append('  </metadata>')
    
    xml_content.append('  <employees>')
    for _, emp in employees.iterrows():
        xml_content.append('    <employee>')
        xml_content.append(f'      <id>{emp["ID"]}</id>')
        xml_content.append(f'      <full_name>{emp["ФИО"]}</full_name>')
        xml_content.append(f'      <position>{emp["Должность"]}</position>')
        xml_content.append(f'      <department>{emp["Отдел"]}</department>')
        xml_content.append(f'      <salary>{emp["Зарплата"]}</salary>')
        xml_content.append(f'      <experience>{emp["Стаж_лет"]}</experience>')
        xml_content.append('    </employee>')
    xml_content.append('  </employees>')
    
    xml_content.append('  <marine_animals>')
    for _, animal in animals.iterrows():
        xml_content.append('    <animal>')
        xml_content.append(f'      <id>{animal["ID"]}</id>')
        xml_content.append(f'      <species>{animal["Вид"]}</species>')
        xml_content.append(f'      <name>{animal["Кличка"]}</name>')
        xml_content.append(f'      <age>{animal["Возраст_лет"]}</age>')
        xml_content.append(f'      <weight>{animal["Вес_кг"]}</weight>')
        xml_content.append(f'      <status>{animal["Статус"]}</status>')
        xml_content.append('    </animal>')
    xml_content.append('  </marine_animals>')
    
    xml_content.append('  <equipment>')
    for _, eq in equipment.iterrows():
        xml_content.append('    <item>')
        xml_content.append(f'      <id>{eq["ID"]}</id>')
        xml_content.append(f'      <type>{eq["Тип_оборудования"]}</type>')
        xml_content.append(f'      <model>{eq["Модель"]}</model>')
        xml_content.append(f'      <status>{eq["Статус"]}</status>')
        xml_content.append(f'      <location>{eq["Местоположение"]}</location>')
        xml_content.append(f'      <cost>{eq["Стоимость_руб"]}</cost>')
        xml_content.append('    </item>')
    xml_content.append('  </equipment>')
    
    xml_content.append('</oceanworld_organization>')
    
    with open('oceanworld_data.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content))
    
    print("XML файл 'oceanworld_data.xml' создан!")

def main():
    """Основная функция"""
    print("=== Генерация отчетов для 'Мир океана' ===\n")
    
    # Читаем данные из Excel
    employees, animals, equipment = read_excel_data()
    
    # Генерируем все форматы
    generate_html(employees, animals, equipment)
    generate_php(employees, animals, equipment)
    generate_xml(employees, animals, equipment)
    
    print("\n=== Все файлы успешно созданы! ===")
    print("📊 oceanworld_data.xlsx - исходные данные Excel")
    print("🌐 oceanworld_report.html - HTML отчет")
    print("⚡ oceanworld_report.php - PHP версия")
    print("📋 oceanworld_data.xml - XML данные")

if __name__ == "__main__":
    main()
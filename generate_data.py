import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Инициализация Faker для русских данных
fake = Faker('ru_RU')

# Данные для организации "Мир океана"
departments = {
    'Аквариумистика': ['Главный аквариумист', 'Старший аквариумист', 'Аквариумист', 'Младший аквариумист'],
    'Научный отдел': ['Ведущий океанолог', 'Океанолог', 'Морской биолог', 'Ихтиолог', 'Гидролог'],
    'Логистика': ['Начальник логистики', 'Логист', 'Специалист по снабжению', 'Кладовщик'],
    'Администрация': ['Директор', 'Заместитель директора', 'Менеджер по персоналу', 'Бухгалтер'],
    'Обслуживание': ['Инженер-технолог', 'Техник', 'Слесарь', 'Электрик'],
    'Экскурсионный отдел': ['Гид-экскурсовод', 'Старший гид', 'Специалист по работе с посетителями']
}

ocean_animals = ['Дельфин', 'Акула', 'Черепаха', 'Скат', 'Осьминог', 'Медуза', 'Морской конёк', 'Кит', 'Кальмар', 'Морская звезда']

def generate_employee_data(num_employees=320):
    """Генерация данных сотрудников"""
    employees = []
    
    for i in range(num_employees):
        department = random.choice(list(departments.keys()))
        position = random.choice(departments[department])
        
        # Зарплата в зависимости от должности
        base_salary = {
            'Главный аквариумист': 90000, 'Старший аквариумист': 70000, 'Аквариумист': 50000, 'Младший аквариумист': 35000,
            'Ведущий океанолог': 95000, 'Океанолог': 65000, 'Морской биолог': 60000, 'Ихтиолог': 55000, 'Гидролог': 58000,
            'Начальник логистики': 80000, 'Логист': 45000, 'Специалист по снабжению': 40000, 'Кладовщик': 35000,
            'Директор': 150000, 'Заместитель директора': 100000, 'Менеджер по персоналу': 55000, 'Бухгалтер': 50000,
            'Инженер-технолог': 60000, 'Техник': 45000, 'Слесарь': 40000, 'Электрик': 42000,
            'Гид-экскурсовод': 40000, 'Старший гид': 50000, 'Специалист по работе с посетителями': 35000
        }
        
        salary = base_salary.get(position, 40000) + random.randint(-5000, 15000)
        
        # Дата приема от 1 до 5 лет назад
        hire_date = fake.date_between(start_date='-5y', end_date='today')
        
        employee = {
            'ID': i + 1,
            'ФИО': fake.name(),
            'Должность': position,
            'Отдел': department,
            'Дата_приема': hire_date,
            'Зарплата': salary,
            'Email': fake.email(),
            'Телефон': fake.phone_number(),
            'Стаж_лет': round((datetime.now().date() - hire_date).days / 365, 1)
        }
        employees.append(employee)
    
    return employees

def generate_animal_data(num_animals=320):
    """Генерация данных морских обитателей"""
    animals = []
    
    for i in range(num_animals):
        animal_type = random.choice(ocean_animals)
        statuses = ['Здоров', 'На лечении', 'Карантин', 'Выпущен в природу']
        
        animal = {
            'ID': i + 1,
            'Вид': animal_type,
            'Кличка': fake.first_name(),
            'Возраст_лет': round(random.uniform(0.1, 25), 1),
            'Вес_кг': round(random.uniform(0.1, 5000), 1),
            'Аквариум': f"Аквариум {random.randint(1, 15)}",
            'Дата_поступления': fake.date_between(start_date='-3y', end_date='today'),
            'Статус': random.choice(statuses),
            'Ответственный': fake.name(),
            'Особые_приметы': fake.text(max_nb_chars=50)
        }
        animals.append(animal)
    
    return animals

def generate_equipment_data(num_items=320):
    """Генерация данных оборудования"""
    equipment_types = [
        'Фильтр водный', 'Компрессор', 'Обогреватель', 'Осветительная система',
        'Система контроля pH', 'Автокормушка', 'Система озонации', 'Холодильная установка'
    ]
    
    equipment = []
    
    for i in range(num_items):
        eq_type = random.choice(equipment_types)
        statuses = ['Работает', 'На обслуживании', 'Требует ремонта', 'Списан']
        
        equipment_item = {
            'ID': i + 1,
            'Тип_оборудования': eq_type,
            'Модель': f"{eq_type} M{random.randint(100, 999)}",
            'Серийный_номер': f"SN-{fake.random_number(digits=8)}",
            'Дата_установки': fake.date_between(start_date='-4y', end_date='today'),
            'Статус': random.choice(statuses),
            'Местоположение': f"Аквариум {random.randint(1, 15)}",
            'Ответственный': fake.name(),
            'Следующее_ТО': fake.date_between(start_date='today', end_date='+1y'),
            'Стоимость_руб': random.randint(5000, 150000)
        }
        equipment.append(equipment_item)
    
    return equipment

def create_excel_with_data():
    """Создание Excel файла с данными на листах 1, 4, 7"""
    
    print("Генерация данных сотрудников...")
    employees = generate_employee_data(320)
    print("Генерация данных морских обитателей...")
    animals = generate_animal_data(320)
    print("Генерация данных оборудования...")
    equipment = generate_equipment_data(320)
    
    # Создаем Excel файл
    with pd.ExcelWriter('oceanworld_data.xlsx', engine='openpyxl') as writer:
        # Лист 1 - Сотрудники
        df_employees = pd.DataFrame(employees)
        df_employees.to_excel(writer, sheet_name='Сотрудники', index=False)
        
        # Создаем пустые листы 2 и 3
        empty_df = pd.DataFrame()
        empty_df.to_excel(writer, sheet_name='Лист2', index=False)
        empty_df.to_excel(writer, sheet_name='Лист3', index=False)
        
        # Лист 4 - Морские обитатели
        df_animals = pd.DataFrame(animals)
        df_animals.to_excel(writer, sheet_name='Морские обитатели', index=False)
        
        # Создаем пустые листы 5 и 6
        empty_df.to_excel(writer, sheet_name='Лист5', index=False)
        empty_df.to_excel(writer, sheet_name='Лист6', index=False)
        
        # Лист 7 - Оборудование
        df_equipment = pd.DataFrame(equipment)
        df_equipment.to_excel(writer, sheet_name='Оборудование', index=False)
    
    print(f"Файл 'oceanworld_data.xlsx' создан успешно!")
    print(f"Всего записей: {len(employees) + len(animals) + len(equipment)}")
    print(f"- Сотрудники: {len(employees)} записей")
    print(f"- Морские обитатели: {len(animals)} записей")
    print(f"- Оборудование: {len(equipment)} записей")

if __name__ == "__main__":
    create_excel_with_data()
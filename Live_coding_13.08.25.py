import time
from datetime import date, timedelta

def check_date():
    # автоматическое определение даты для текущего/следующего года
    current_year = date.today().year
    year = current_year if date.today().month < 11 else current_year + 1
    create_date = date(year, 11, 1)
    return {
        "create": create_date,
        "remind": create_date + timedelta(days=7),
        "close": create_date + timedelta(days=14)
    }

employees = {
    "Alex": {"vacation": None, "notified": False},
    "Lera": {"vacation": None, "notified": False},
    "Mari": {"vacation": None, "notified": False}
}

def create_plans():
    # создание графиков отпусков 1 ноября
    for name in employees:
        employees[name]["vacation"] = None
    print(f"Созданы пустые графики для: {list(employees.keys())}")

def send_reminders():
    print("\n[8 ноября] Отправляем напоминания:")
    for name, data in employees.items():
        if data["vacation"] is None:
            print(f" - {name}: заполните график отпусков!")
            data['notified'] = True

def close_plans():
    print("\n[15 ноября] Завершаем прием графиков:")
    # Стандартные отпуска для тех, кто не заполнил
    default_vacation = [
        {'period': 'осенний', 'date': '1 сентября', 'duration': '2 недели'},
        {'period': 'летний', 'date': '1 июля', 'duration': '2 недели'}
    ]

    for name, data in employees.items():
        if data["vacation"] is None:
            employees[name]["vacation"] = default_vacation
            print(f' - {name}: установлен стандартный отпуск')

    print("\nИтоговые графики:")
    for name, data in employees.items():
        print(f" - {name}: {'заполнен' if data['vacation'] else 'не заполнен'}")

def main():
    print("    Система управления отпусками")
    dates = check_date()
    
    print(f"\nДаты работы системы:")
    print(f" - Создание графиков: {dates['create']}")
    print(f" - Напоминания: {dates['remind']}")
    print(f" - Завершение: {dates['close']}\n")
    
    while True:
        today = date.today()
        
        # Проверяем даты
        if today == dates['create']:
            create_plans()
        elif today == dates['remind']:
            send_reminders()
        elif today == dates['close']:
            close_plans()
            print("\nРабота системы завершена!")
            break
        
        time.sleep(86400)  # Ждем 1 день (86400 секунд)

if __name__ == '__main__':
    main()
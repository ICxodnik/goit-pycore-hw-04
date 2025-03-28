from pathlib import Path

FILENAME = Path(__file__).parent / "data" / "task_1_data.txt"

def total_salary(items):
    size = len(items) if items else 0

    if(size == 0):
        return 0, 0
    
    total = sum(items)
    average = total / size
    return total, average
    
def parseFile(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            int_lines = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:  # Переконуємося, що є два елементи
                    try:
                        int_lines.append(int(parts[1]))
                    except ValueError:
                        print(f"Помилка перетворення в число: {parts[1]}")
                else:
                    print(f"Некоректний рядок (пропускаємо): {line.strip()}")
            return int_lines
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

if __name__ == '__main__':
    items = parseFile(FILENAME)

    total, average = total_salary(items)

    print(f"Загальна сума зарплат: {total}, Середня зарплата: {average}")

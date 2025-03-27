from pathlib import Path

FILENAME = Path(__file__).parent / "task_2_data.txt"

    
def parseFile(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            cats_lines = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:  # Переконуємося, що є три елементи
                    try:
                        cats_lines.append({"cat_id":parts[0], "name": parts[1], "age": int(parts[2])})
                    except ValueError:
                        print(f"Помилка перетворення віку в число: {parts[2]}")
                else:
                    print(f"Некоректний рядок (пропускаємо): {line.strip()}")
            return cats_lines
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

if __name__ == '__main__':
    items = parseFile(FILENAME)

    print(f"Список котів: {items}")

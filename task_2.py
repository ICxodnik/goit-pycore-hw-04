from pathlib import Path

FILENAME = Path(__file__).parent / "data" / "task_2_data.txt"

def get_cats_info(string_data: str):
    cats_lines = []
    for line in string_data:
        parts = line.strip().split(",")
        if len(parts) == 3:  # Переконуємося, що є три елементи
            try:
                cats_lines.append({"cat_id": parts[0], "name": parts[1], "age": int(parts[2])})
            except ValueError:
                print(f"Помилка перетворення віку в число: {parts[2]}")
        else:
            print(f"Некоректний рядок (пропускаємо): {line.strip()}")
    return cats_lines
    
def parseFile(filename)-> str: 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
            #lines = [el.strip() for el in file.readlines()]
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

if __name__ == '__main__':
    data = parseFile(FILENAME)
    cats = get_cats_info(data)

    print(f"Список котів: {cats}")

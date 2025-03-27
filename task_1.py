from pathlib import Path

FILENAME = Path(__file__).parent / "task_1_data.txt"

def total_salary(items):
    total = sum(items)
    average = total / len(items)
    return total, average
    
def parseFile(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [el.strip().split(",")[1] for el in file.readlines()]
            int_lines = list(map(int, lines))
            return int_lines
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

if __name__ == '__main__':
    items = parseFile(FILENAME)

    total, average = total_salary(items)

    print(total, average)
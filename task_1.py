from pathlib import Path

FILENAME = Path(__file__).parent / "task_1_data.txt"


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip().split(",")[1] for el in file.readlines()]
            int_lines = list(map(int, lines))

            total = sum(int_lines)
            average = total / len(int_lines)
            return total, average 
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

if __name__ == '__main__':
    print(total_salary(FILENAME))
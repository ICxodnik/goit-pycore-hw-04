import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)


def parse_file(path: Path):
    if not path.exists():
        print(Fore.RED + f"Directory not exist: {path}")
        return
    
    for el in path.iterdir():
        # Підрунок вкладеності і встановлення глибини
        if el.is_dir():
            print(Fore.RED + (len(el.parts) * " ") + f"{el.name}/")
            parse_file(el)
        else:
            print(Fore.GREEN + (len(el.parts) * " ") + f"{el.name}")


if __name__ == "__main__":
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати шлях до директорії.")
        sys.exit(1)

    # Отримання шляху до директорії з аргументу командного рядка
    directory_path = Path(sys.argv[1])
    # Виведення структури директорії
    parse_file(directory_path)

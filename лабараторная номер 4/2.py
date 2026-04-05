import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # открываем CSV файл, читаем строки как словари, собираем в список
    with open(INPUT_FILENAME, "r", encoding="utf-8") as csv_file:
        csv_data = [row for row in csv.DictReader(csv_file)]

    # открываем JSON файл, записываем данные с отступами 4 пробела
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:
        json.dump(csv_data, json_file, indent=4, ensure_ascii=False)

    # выводим содержимое получившегося JSON файла на печать
    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")

if __name__ == '__main__':
    # Нужно для проверки
    task()
# ну это уже так называемый гроб
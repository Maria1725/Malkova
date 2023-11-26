# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        b = [i for i in reader]

    with open(OUTPUT_FILENAME, "w") as file:
        json.dump(b, file, indent=4)

    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

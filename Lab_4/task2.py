import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    a = []
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            a.append(row)

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(a, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

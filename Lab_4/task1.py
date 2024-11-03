import json


def task() -> float:
    with open('input.json', 'r') as file:
        file_data = json.load(file)

    return round(sum(i['score'] * i['weight'] for i in file_data), 3)

print(task())

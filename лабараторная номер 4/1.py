# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    sum = 0.0

    for element in dataset:
        value = element.get('score', 0)
        weight = element.get('weight', 0)
        multiplication = value * weight
        sum += multiplication

    rounded_output = round(sum, 3)
    return rounded_output
print(task())
#я окончательно перестал понимать что здесь происходит
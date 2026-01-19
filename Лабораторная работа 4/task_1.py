import json

def task() -> float:
    with open('input.json', 'r') as file:
        input = json.load(file)

    total_sum = 0.0
    for item in input:
        score = item.get("score", 0.0)
        weight = item.get("weight", 0.0)
        total_sum += score * weight

    return round(total_sum, 3)

print(task())

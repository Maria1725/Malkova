# TODO решите задачу
import json

imputjson = "input.json"


def task() -> float:
    with open(imputjson) as f:
        a = json.load(f)
    result = [i["score"] * i["weight"] for i in a]
    sum_result = round(sum(result), 3)
    return sum_result


print(task())

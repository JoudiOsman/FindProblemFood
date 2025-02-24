import json
import random

fileName = "default"

def find(fileName):
    print(fileName)
    


def add(food, day, fileName):
    x = {
            "name": food,
            "date": day,
            "id": random.randrange(1,999999999999999)

    }
    print(json.dumps(x))

    try: #try to write
        with open(fileName, "r") as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):# catch empty file
        data = []  

    data.append(x)  # Append new entry

    with open(fileName, "w+") as file:
        json.dump(data, file, indent=4)  # Write updated list back to file
 
add("c", "b", "c.json")
add("2", "b", "c.json")
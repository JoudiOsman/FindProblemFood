import json
import random

fileName = "default"

def find(fileName):
    print(fileName)

#deletes entry based on id 
def delete(data, id):
    for entry in data:
        if entry['id'] == id:
            data.remove(entry)

#returns a list of json objects
def loadData(fileName):
    try: #try to read
        with open(fileName, "r") as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):# catch empty file
        data = []  

#saves json objects to file
def saveData(data, fileName):
    with open(fileName, "w+") as file:
        json.dump(data, file, indent=4)  # Write updated list back to file


# def getData(fileName):
#     try: #try to read
#         with open(fileName, "r") as file:
#             data = json.load(file)  # Load existing data
#     except (FileNotFoundError, json.JSONDecodeError):# catch empty file
#         data = []  


def add(food, day, data):
    x = {
            "name": food,
            "date": day,
            "id": random.randrange(1,999999999999999)

    }
    data.append(x)  # Append new entry
    


 
fileName = "c.json"

try: #try to read
    with open(fileName, "r") as file:
        data = json.load(file)  # Load existing data
except (FileNotFoundError, json.JSONDecodeError):# catch empty file
    data = []

delete(data, 531059441710585)

# getData("c.json")
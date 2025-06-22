import json
import random
import datetime

fileName = "default"

def find(fileName):
    print(fileName)

#deletes entry based on id 
def delete(data, id):
    for entry in data:
        if entry['id'] == id:
            data.remove(entry)

#returns a list of json objects containing the diet
def loadData(fileName):
    try: #try to read
        with open(fileName, "r") as file:
            data = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):# catch empty file
        data = [] 
    return data

    
#saves json objects to file
def saveData(data, fileName):
    with open(fileName, "w+") as file:
        json.dump(data, file, indent=4)  # Write updated list back to file


def add(food, day, data):
    x = {
            "name": food,
            "date": day,
            "id": random.randrange(1,999999999999999)

    }
    data.append(x)  # Append new entry
    

def populateMap(data):
    map = {}
    for entry in data:
        dateList = entry['date'].split("-")
        year = int(dateList[0])
        month = int(dateList[1])
        day = int(dateList[2])
        date = datetime.date(year, month, day)
        
        map.setdefault(entry['name'], []).append(date)
        print(map)
    return map

def populateSevMap(data):
    map = {}
    for entry in data:
        map.setdefault(entry["date"], []).append(entry["severity"])
        print(map)
    return map
 
fileName = "c.json"
sFileName  = "severity.json"




foodData = loadData(fileName)
sevData = loadData(sFileName)
map = populateMap(foodData)
sevMap = populateSevMap(sevData)
print(map)

date1 = datetime.date(2025, 6, 21)
date2 = datetime.date(2025, 6, 22)

print(date1 + datetime.timedelta(days=0))

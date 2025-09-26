import json
import random
import datetime
from openai import OpenAI

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
    # print(data)
    with open(fileName, "w+") as file:
        json.dump(data, file, indent=4)  # Write updated list back to file


#takes a food and date and adds it to the data
def add(food, day, data):
    date = str(day.year) + "-"+str(day.month)+"-"+str(day.day)
    x = {
            "name": food.strip(),
            "date": date,
            "id": random.randrange(1,999999999999999)
    }
    data.append(x)  # Append new entry


#adds a list of foods entered on the same day
def addMulti(foods, day, data):
    for food in foods:
        add(food, day, data)



def addSev(sev, date, data):
    x = {
        "date": date,
        "severity": sev
    }
    data.append(x)



def populateMap(data):
    map = {}
    for entry in data:
        dateList = entry['date'].split("-")
        year = int(dateList[0])
        month = int(dateList[1])
        day = int(dateList[2])
        date = datetime.date(year, month, day)
        
        map.setdefault(entry['name'], []).append(date)
    return map



def populateSevMap(data):
    map = {}
    for entry in data:
        map.setdefault(entry["date"], []).append(entry["severity"])
    return map

def parseInput(input, data):
    splitInput = input.split(":")
    splitDate = splitInput[0].split("/")
    day = datetime.date(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))
    foodsInput = splitInput[1]
    foodsInput.replace(', ',',')
    foods = foodsInput.split(',')
    addMulti(foods, day, data)
    


 
fileName = "c.json"
sFileName  = "severity.json"









foodData = loadData(fileName)
print(foodData)
sevData = loadData(sFileName)
map = populateMap(foodData)
sevMap = populateSevMap(sevData)
# print(map)

date1 = datetime.date(2025, 6, 21)
date2 = datetime.date(2025, 6, 22)

# print(date1 + datetime.timedelta(days=0))
c = 0

while c == 0:
    ("yyyy/mm/dd: tomato, apple, juice")
    userInput = input("2001/02/25: tomato, apple, juice")
    parseInput(userInput, foodData)
    saveData(foodData,"c.json")

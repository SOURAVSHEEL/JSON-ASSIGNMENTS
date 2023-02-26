import json


state_capitals = {

    "Uttar Pradesh":"Lucknow",
    "Rajasthan":"Jaipur",
    "Maharashtra":"Mumbai",
    "Punjab":"Chandigrah",
    "Haryana":"Chandigrah",
    "Himachal Pradesh":"Shimla",
    "Uttarakhand":"Dehradun"

}

with open("C:\\Users\\soura\\OneDrive\Desktop\\DATA SCIENCE\\EDYODA ASSIGNMENTS\\Json_assignemt\\state_capitals.json","w") as file:
    json.dump(state_capitals,file)
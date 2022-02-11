import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://uktjaya:<password>@cluster0.q5ruc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["BlackJack"]
dbUsers = db["users"]

def addUser(username, password):
    data = {
        "username": username,
        "password": password,
        "totalMatch": 0,
        "totalWin": 0,
        "totalLose": 0,
        "chip": 5000,
        "firstTimeLogin": 0,
        "lastLogin": 0,
        "claimDate": 0
    }
    dbUsers.insert_one(data)

def isUsernameExist(username):
    if dbUsers.count_documents({"username": username}, limit = 1):
        return True
    else:
        return False

def getPassword(username):
    userData = dbUsers.find_one({"username": username})
    return userData["password"]

def getMatches(username):
    userData = dbUsers.find_one({"username": username})
    return userData["totalMatch"]

def addMatch(username):
    userData = dbUsers.find_one({"username": username})
    dbUsers.update_one({"_id": userData["_id"]}, {"$inc": {"totalMatch": 1}})

def getWins(username):
    userData = dbUsers.find_one({"username": username})
    return userData["totalWin"]

def addWin(username):
    userData = dbUsers.find_one({"username": username})
    dbUsers.update_one({"_id": userData["_id"]}, {"$inc": {"totalWin": 1}})

def getLoses(username):
    userData = dbUsers.find_one({"username": username})
    return userData["totalLose"]

def addLose(username):
    userData = dbUsers.find_one({"username": username})
    dbUsers.update_one({"_id": userData["_id"]}, {"$inc": {"totalLose": 1}})

def getChip(username):
    userData = dbUsers.find_one({"username": username})
    return userData["chip"]

def setChip(username, chip):
    userData = dbUsers.find_one({"username": username})
    dbUsers.update_one({"_id": userData["_id"]}, {"$inc": {"chip": chip}})

def getFirstTimeLogin(username):
    userData = dbUsers.find_one({"username": username})
    return userData["firstTimeLogin"]

def getLastLogin(username):
    userData = dbUsers.find_one({"username": username})
    return userData["lastLogin"]

def addLogin(username):
    userData = dbUsers.find_one({"username": username})
    dateTimeData = datetime.datetime.now()
    if(userData["firstTimeLogin"] == 0):
        dbUsers.update_one({"_id": userData["_id"]}, {"$set": {"firstTimeLogin": dateTimeData}})
    dbUsers.update_one({"_id": userData["_id"]}, {"$set": {"lastLogin": dateTimeData}})

def getClaimDate(username):
    userData = dbUsers.find_one({"username": username})
    return userData["claimDate"]

def addClaimDate(username):
    userData = dbUsers.find_one({"username": username})
    dbUsers.update_one({"_id": userData["_id"]}, {"$set": {"claimDate": datetime.datetime.now()}})

def getUserData(username):
    userData = dbUsers.find_one({"username": username})
    return userData
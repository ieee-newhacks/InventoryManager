from pymongo import MongoClient

client = MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")

print(client.mflix)

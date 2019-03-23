import pymongo
from bson.json_util import dumps
import json

mongo = pymongo.MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")

db = pymongo.database.Database(mongo, 'inventory')
col = pymongo.collection.Collection(db, 'manager')

col_results = json.loads(dumps(col.find().limit(5).sort("time", -1)))



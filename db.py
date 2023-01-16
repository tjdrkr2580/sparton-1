from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.zfuzrjp.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from pymongo import Mongoclient

client = MongoClient('mongodb+srv://test:sparta@cluster0.47veg7d.mongodb.net/?retryWrites=true&w=majority')
db = client.sparton

import pymongo

USERNAME = 'admin'
PASSWORD = 'WVTIRUeAqtOXpAM3'
DATABASE_URL = 'cluster0.niuem.mongodb.net'

client = pymongo.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{DATABASE_URL}/?retryWrites=true&w=majority')

db = client['fastapi_mongo']
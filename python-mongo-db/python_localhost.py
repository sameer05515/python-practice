from pymongo import MongoClient
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'relation-calc'
COLLECTION_NAME = 'relation'

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DB_NAME][COLLECTION_NAME]
projects = collection.find()

# for db in connection.list_databases():
#     print(db)

# for x in collection.find():
#     print(x)

newValue = {
    "name" : "Kaushalya Devi",
    "dob" : "14-08-1946",
    "father" : "Chandu Sah"
}

collection.insert_one(newValue)

for x in collection.find():
    print(x)


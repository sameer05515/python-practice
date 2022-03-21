import pymongo

# mongodb+srv://prem:prem123@cluster0.h9zdm.mongodb.net/pythondb?retryWrites=true&w=majority

myclient = pymongo.MongoClient("mongodb+srv://prem:prem123@cluster0.h9zdm.mongodb.net/pythondb?retryWrites=true&w=majority")

mydb = myclient["pythondb"]

print(myclient.list_database_names())

# Create collection
mycol = mydb["words"]

# ---------------------------------

# mydict = { "word": "Cow", "synonyms": ["Holy Animal"] }

# x = mycol.insert_one(mydict)

# ----------------------------------------------

# mydict = { "word": "Ganga", "synonyms": "Holy River" }

# x = mycol.insert_one(mydict)

# print(x.inserted_id)

# ------------------------------------------

# mylist = [
#   { "word": "Amy", "synonyms": "Apple st 652"},
#   { "word": "Hannah", "synonyms": "Mountain 21"},
#   { "word": "Michael", "synonyms": "Valley 345"},
#   { "word": "Sandy", "synonyms": "Ocean blvd 2"},
#   { "word": "Betty", "synonyms": "Green Grass 1"},
#   { "word": "Richard", "synonyms": "Sky st 331"},
#   { "word": "Susan", "synonyms": "One way 98"},
#   { "word": "Vicky", "synonyms": "Yellow Garden 2"},
#   { "word": "Ben", "synonyms": "Park Lane 38"},
#   { "word": "William", "synonyms": "Central st 954"},
#   { "word": "Chuck", "synonyms": "Main Road 989"},
#   { "word": "Viola", "synonyms": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# -------------------------------



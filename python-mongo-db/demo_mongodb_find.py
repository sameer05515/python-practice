import pymongo

myclient = pymongo.MongoClient("mongodb+srv://prem:prem123@cluster0.h9zdm.mongodb.net/pythondb?retryWrites=true&w=majority")

mydb = myclient["pythondb"]

# print(myclient.list_database_names())

# Create collection
mycol = mydb["words"]

# -------------- find_one()
# x = mycol.find_one()

# print(x)

# ------------- find All
# for x in mycol.find():
#   print(x)
  
# ----------------- Return Only Some Fields
for x in mycol.find({},{ "_id": 0, "word": 1, "synonyms": 1 }):
  print(x)
  
# ----------------- Return Only Some Fields
# You are not allowed to specify both 0 and 1 values in the same object 
# (except if one of the fields is the _id field). 
# If you specify a field with the value 0, all other fields get the value 1, 
# and vice versa:
for x in mycol.find({},{ "_id": 0,  "synonyms": 0 }):
  print(x)
  

# Find documents where the address starts with the letter "C":
myquery = { "word": { "$regex": "^C" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# Sort the result alphabetically by word:  
mydoc = mycol.find().sort("word")
# mydoc = mycol.find().sort("word", -1)

for x in mydoc:
  print(x)

# delete all
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
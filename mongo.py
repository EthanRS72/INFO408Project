#Ethan Smith INFO408 Project
#mongo.py
#Program to read in the formatted data and create references to matching documents
#stored in the main collection being used in MongoDB
#pymongo can be installed using pip install pymongo in a terminal

import pymongo
import json

#Change all instances of {username}, {password}, {dbname} to your own values
# MongoDB connection URI with username and password
uri = "mongodb://{username}:{password}@ismdb.otago.ac.nz:27017/{username}?authMechanism=DEFAULT"

# Connect to MongoDB
client = pymongo.MongoClient(uri)
db = client["{dbname}"]
collection = db["Videos"]

#file to be used (change the two capital letters to whatever file to use)
input = 'USvideos.json'
#open file - must use utf-8 to preserve non-english characters
with open(input, 'r', encoding = 'utf-8') as file:
    data = json.load(file)

#for every document find the matching document from the Videos collection and create a reference
for doc in data:

    matching_id = {"video_id": doc['video_id']}

    matched_document = collection.find_one(matching_id)

    doc["Video"] = {}
    doc["Video"]["$ref"] = "Videos"
    doc["Video"]["$id"] = str(matched_document["_id"])

#write file - must use utf-8 to preserve non-english characters
with open(input, 'w', encoding = 'utf-8') as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)

#close connection
client.close()
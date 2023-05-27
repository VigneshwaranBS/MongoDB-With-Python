import pymongo

#  initailize collections
client = pymongo.MongoClient("mongodb://localhost:27017")

# cretae db
mydb = client["Employee"]

#  create collection
information = mydb.employeeinformation

#  cretae record  (json)
record={
    "first name":"vignesh",
    "last name" : "vicky",
    "age" : "20"
}

#  insert record 
information.insert_one(record)

#  insert many record in array format
record1=[{
    "first name":"vignesh",
    "last name" : "vicky",
    "age" : "20"
},{
    "first name":"vicky",
    "last name" : "vignesh",
    "age" : "21"
    
},{
    "first name":"vignesh",
    "last name" : "vicky",
    "age" : "20"
}]

#  insert record many
information.insert_many(record1)
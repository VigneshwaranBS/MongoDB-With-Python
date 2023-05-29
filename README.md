# MongoDB With Python 

## This readme provides an overview of using MongoDB with Python for performing update queries, general queries, and using aggregate functions.

## Prerequisites
Before getting started, ensure you have the following:

- Python installed on your system
- The pymongo library installed. You can install it using pip:
```
pip install pymongo
```
MongoDB server up and running.
Connecting to MongoDB
To connect to a MongoDB server from Python, you can use the pymongo library. Here's an example of establishing a connection:

```
from pymongo import MongoClient

# Create a MongoClient object
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["mydatabase"]

```

## Updates query

Updates query is used to update the data in MongoDB database. There are two ways to update the data:

1. Using the `update()` method
2. Using the `update_one()` method

The `update()` method takes two arguments:

* The first argument is the collection name
* The second argument is the update document

The update document is a JSON object that contains the following fields:

* `$set`: This field is used to set the new value for a field.
* `$inc`: This field is used to increment the value of a field by a specified amount.
* `$unset`: This field is used to unset a field.

For example, the following code updates the value of the `name` field in the `users` collection:

```
db.users.update({"name": "John Doe"}, {"$set": {"name": "Jane Doe"}})
```

The `update_one()` method takes three arguments:

* The first argument is the collection name
* The second argument is the filter document
* The third argument is the update document

The filter document is a JSON object that is used to select the documents that will be updated. The update document is the same as the update document used with the `update()` method.

For example, the following code updates the value of the `name` field in the `users` collection for all documents where the `age` is greater than 18:

```
db.users.update_one({"age": {"$gt": 18}}, {"$set": {"name": "Adult"}})
```

## General query

General query is used to retrieve data from MongoDB database. There are two ways to retrieve data:

1. Using the `find()` method
2. Using the `find_one()` method

The `find()` method takes two arguments:

* The first argument is the collection name
* The second argument is the filter document

The filter document is a JSON object that is used to select the documents that will be retrieved.

For example, the following code retrieves all documents from the `users` collection:

```
db.users.find()
```

The `find_one()` method takes two arguments:

* The first argument is the collection name
* The second argument is the filter document

The filter document is the same as the filter document used with the `find()` method.

For example, the following code retrieves the first document from the `users` collection:

```
db.users.find_one()
```

## Aggregate function

Aggregate function is used to aggregate data from MongoDB database. There are a variety of aggregate functions available, including:

* `count()`: This function returns the number of documents in a collection.
* `sum()`: This function returns the sum of a field in a collection.
* `avg()`: This function returns the average of a field in a collection.
* `min()`: This function returns the minimum value of a field in a collection.
* `max()`: This function returns the maximum value of a field in a collection.

For example, the following code returns the number of documents in the `users` collection:

```
db.users.count()
```

The following code returns the sum of the `age` field in the `users` collection:

```
db.users.aggregate([
  {"$group": {"_id": null, "total_age": {"$sum": "$age"}}}
])
```

The following code returns the average of the `age` field in the `users` collection:

```
db.users.aggregate([
  {"$group": {"_id": null, "average_age": {"$avg": "$age"}}}
])
```

The following code returns the minimum value of the `age` field in the `users` collection:

```
db.users.aggregate([
  {"$group": {"_id": null, "min_age": {"$min": "$age"}}}
])
```

The following code returns the maximum value of the `age` field in the `users` collection:

```
db.users.aggregate([
  {"$group": {"_id": null, "max_age": {"$max": "$age"}}}
])
```

## Conclusion
This readme covered the basics of using MongoDB with Python. It demonstrated how to connect to MongoDB, perform update queries, general queries, and utilize aggregate functions. With this knowledge, you can start building powerful applications that interact with MongoDB using Python.

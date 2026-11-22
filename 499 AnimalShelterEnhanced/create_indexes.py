
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")
collection = client["aac"]["animals"]

# Index fields used for filtering and searching
indexes = [
    "Animal ID",
    "Animal Type",
    "Breed",
    "Outcome Type",
    "DateTime"
]

for field in indexes:
    name = collection.create_index(field)
    print(f"Created/verified index: {name}")

print("\nTotal records:", collection.count_documents({}))
print("Available indexes:", list(collection.index_information()))

client.close()



import csv
import glob
from pymongo import MongoClient

files = glob.glob("Austin_Animal_Center_Outcomes*.csv")

if not files:
    raise FileNotFoundError("Animal outcomes CSV not found.")

client = MongoClient("mongodb://127.0.0.1:27017/")
collection = client["aac"]["animals"]

# Clear the test collection before importing the full dataset.
collection.delete_many({})

total = 0
batch = []

with open(files[0], encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for record in reader:
        batch.append(record)

        if len(batch) == 1000:
            collection.insert_many(batch)
            total += len(batch)
            batch = []
            print(f"Imported {total} records")

    if batch:
        collection.insert_many(batch)
        total += len(batch)

print(f"\nImport complete: {total} records")
print(f"MongoDB total: {collection.count_documents({})}")

client.close()

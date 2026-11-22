# CRUD Python module for the Austin Animal Center database
import os
from pymongo import MongoClient


class AnimalShelter:
    """Provide create, read, update, and delete operations."""

    def __init__(self):
        """Initialize MongoDB using environment variables."""

        HOST = os.getenv("MONGO_HOST", "localhost")
        PORT = int(os.getenv("MONGO_PORT", "27017"))
        DB = os.getenv("MONGO_DB", "aac")
        COL = os.getenv("MONGO_COLLECTION", "animals")

        
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")

        connection_options = {
            "host": HOST,
            "port": PORT,
            "serverSelectionTimeoutMS": 5000
        }

        # Use authentication only when credentials are supplied.
        if username and password:
            connection_options["username"] = username
            connection_options["password"] = password
            connection_options["authSource"] = os.getenv(
                "MONGO_AUTH_SOURCE", "admin"
            )
        elif username or password:
            raise ValueError(
                "Both MongoDB username and password are required."
            )

        self.client = MongoClient(**connection_options)


        self.database = self.client[DB]
        self.collection = self.database[COL]


    def create(self, data):
        """Insert one document and return True when successful."""

        if data is None or not isinstance(data, dict):
            raise ValueError("Data must be provided as a dictionary.")

        try:
            self.collection.insert_one(data)
            return True

        except Exception as error:
            print(f"Create operation failed: {error}")
            return False

    def read(self, query):
        """Return matching documents as a list."""

        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be provided as a dictionary.")

        try:
            results = self.collection.find(query)
            return list(results)

        except Exception as error:
            print(f"Read operation failed: {error}")
            return []

    def update(self, query, new_data):
        """Update matching documents and return the modified count."""

        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be provided as a dictionary.")

        if new_data is None or not isinstance(new_data, dict):
            raise ValueError("New data must be provided as a dictionary.")

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_data}
            )

            return result.modified_count

        except Exception as error:
            print(f"Update operation failed: {error}")
            return 0

    def delete(self, query):
        """Delete matching documents and return the deleted count."""

        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be provided as a dictionary.")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except Exception as error:
            print(f"Delete operation failed: {error}")
            return 0


    def search_animals(self, filters=None, limit=100, skip=0):
        """Search animal records with filtering and pagination."""
        if filters is None:
            filters = {}

        if not isinstance(filters, dict):
            raise ValueError("Filters must be a dictionary.")

        if not isinstance(limit, int) or not 1 <= limit <= 1000:
            raise ValueError("Limit must be between 1 and 1000.")

        if not isinstance(skip, int) or skip < 0:
            raise ValueError("Skip must be zero or greater.")

        allowed_fields = {
            "Animal ID",
            "Animal Type",
            "Breed",
            "Outcome Type",
            "DateTime"
        }

        if any(field not in allowed_fields for field in filters):
            raise ValueError("Unsupported search field.")

        if any(
            not isinstance(value, str)
            for value in filters.values()
        ):
            raise ValueError("Filter values must be strings.")

        return list(
            self.collection.find(
                filters, {"_id": 0}
            ).sort("_id", 1).skip(skip).limit(limit)
        )

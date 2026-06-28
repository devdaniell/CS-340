from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """CRUD operations for the Austin Animal Center database."""

    def __init__(self, username, password):
        """Initialize MongoDB connection."""

        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin"
            )

            self.database = self.client[DB]
            self.collection = self.database[COL]

        except PyMongoError as e:
            print("Connection Error:", e)

    # ------------------------
    # CREATE
    # ------------------------

    def create(self, data):

        if data is None:
            return False

        try:
            self.collection.insert_one(data)
            return True

        except PyMongoError as e:
            print("Create Error:", e)
            return False

    # ------------------------
    # READ
    # ------------------------

    def read(self, query):

        try:
            return list(self.collection.find(query))

        except PyMongoError as e:
            print("Read Error:", e)
            return []

    # ------------------------
    # UPDATE
    # ------------------------

    def update(self, query, values):

        try:
            result = self.collection.update_many(
                query,
                {"$set": values}
            )

            return result.modified_count

        except PyMongoError as e:
            print("Update Error:", e)
            return 0

    # ------------------------
    # DELETE
    # ------------------------

    def delete(self, query):

        try:
            result = self.collection.delete_many(query)

            return result.deleted_count

        except PyMongoError as e:
            print("Delete Error:", e)
            return 0
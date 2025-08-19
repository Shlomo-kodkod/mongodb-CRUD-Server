
from pymongo import MongoClient
import logging
from service import config  
from service.model import Soldier

logger = logging.getLogger(__name__)

class DAL:

    @staticmethod
    def connect(self):
        """
        Create a connection to the MongoDB database using the configuration settings.
        """
        try:
            client = MongoClient(host=config.host, port=config.port, username=config.username, password=config.password)
            db = client[config.db]
            logger.info(f"Connected to MongoDB at {config.host}:{config.port}")
            return db
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise e
    
    @staticmethod
    def read_collection(collection_name=config.collection):
        """""
        Read a collection from the MongoDB database.
        """
        try:
            db = DAL.connect()
            collection = db[collection_name]
            data = list(collection.find({}, {"_id": 0}))  
            logger.info(f"Data loaded successfully from {collection.name} collection.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve collection {collection_name}: {e}")
            raise e
        
    @staticmethod
    def create_soldier(soldier: Soldier):
        """
        Create a soldier document and insert into the MongoDB collection.
        """
        try:
            db = DAL.connect()
            collection = db[config.collection]
            result = collection.insert_one(soldier.__dict__)
            logger.info(f"Soldier {soldier.soldier_id} inserted successfully.")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Failed to insert soldier: {e}")
            raise e
        
    @staticmethod
    def update_soldier(soldier_id, updated_data: dict):
        """
        Update a soldier document in the MongoDB collection.
        """
        try:
            db = DAL.connect()
            collection = db[config.collection]
            result = collection.update_one({"soldier_id": soldier_id}, {"$set": updated_data})
            if result.modified_count > 0:
                logger.info(f"Soldier {soldier_id} updated successfully.")
            else:
                logger.warning(f"No changes made for soldier {soldier_id}.")
            return result.modified_count
        except Exception as e:
            logger.error(f"Failed to update soldier {soldier_id}: {e}")
            raise e 

    @staticmethod
    def delete_soldier(soldier_id):
        """
        Delete a soldier document from the MongoDB collection.
        """
        try:
            db = DAL.connect()
            collection = db[config.collection]
            result = collection.delete_one({"soldier_id": soldier_id})
            if result.deleted_count > 0:
                logger.info(f"Soldier {soldier_id} deleted successfully.")
            else:
                logger.warning(f"No soldier found with ID {soldier_id}.")
            return result.deleted_count
        except Exception as e:
            logger.error(f"Failed to delete soldier {soldier_id}: {e}")
            raise e

    

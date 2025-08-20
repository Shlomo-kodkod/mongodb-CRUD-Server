
from pymongo import MongoClient
import logging
from service import config  
from service.model import Soldier

logger = logging.getLogger(__name__)

class DAL:

    def connect(self):
        """
        Connect to the mongodb database.
        """
        try:
            uri = f"mongodb://{config.username}:{config.password}@{config.host}:{config.port}/?authSource=admin"
            self.__client = MongoClient(uri)
            self.__db = self.__client[config.db]
            logger.info(f"Connected to mongodb at {config.host}:{config.port}")
        except Exception as e:
            logger.error(f"Failed to connect to mongodb: {e}")
            raise e
    
    def disconnect(self):
        """
        Disconnect from the mongodb database.
        """ 
        if self.__client is not None:
            self.__client.close()
            logger.info("Database connection closed.")

    def read_collection(self, collection_name=config.collection) -> list:
        """""
        Read a collection from the mongodb database.
        """
        try:
            self.connect()
            collection = self.__db[collection_name]
            data = list(collection.find({}, {"_id": 0}))  
            logger.info(f"Data loaded successfully.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve collection: {e}")
            raise e
        finally:
            self.disconnect()
        
    def create_soldier(self, soldier: Soldier):
        """
        Create a soldier document and insert into the mongodb collection.
        """
        try:
            self.connect()
            collection = self.__db[config.collection]
            result = collection.insert_one(soldier.__dict__)
            logger.info(f"Soldier inserted successfully.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to insert soldier: {e}")
            raise e
        finally:
            self.disconnect()
        
    def update_soldier(self, soldier_id, updated_data: dict):
        """
        Update a soldier document in the mongodb collection.
        """
        try:
            self.connect()
            collection = self.__db[config.collection]
            result = collection.update_one({"soldier_id": soldier_id}, {"$set": updated_data})
            if result.modified_count > 0:
                logger.info(f"Soldier updated successfully.")
            else:
                logger.warning(f"No changes made.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to update soldier : {e}")
            raise e 
        finally:
            self.disconnect()

    def delete_soldier(self, soldier_id):
        """
        Delete a soldier document from the mongodb collection.
        """
        try:
            self.connect()
            collection = self.__db[config.collection]
            result = collection.delete_one({"soldier_id": soldier_id})
            if result.deleted_count > 0:
                logger.info(f"Soldier deleted successfully.")
            else:
                logger.warning(f"Soldier not found.")
            return result.acknowledged
        except Exception as e:
            logger.error(f"Failed to delete soldier : {e}")
            raise e
        finally:
            self.disconnect()

    

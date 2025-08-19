from pymongo import MongoClient
import logging
from service import config  

logger = logging.getLogger(__name__)

class DAL:

    @staticmethod
    def connect(self):
        try:
            client = MongoClient(host=config.host, port=config.port, username=config.username, password=config.password)
            db = client[config.db]
            logger.info(f"Connected to MongoDB at {config.host}:{config.port}")
            return db
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise e
    
    @staticmethod
    def get_collection(collection_name=config.collection):
        try:
            db = DAL.connect()
            collection = db[collection_name]
            data = list(collection.find({}, {"_id": 0}))  
            logger.info(f"Data loaded successfully from {collection.name} collection.")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve collection {collection_name}: {e}")
            raise e
        
        
        

    

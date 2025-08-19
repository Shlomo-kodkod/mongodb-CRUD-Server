from pymongo import MongoClient
from service import config  

class DAL:

    @staticmethod
    def connect(self):
        client = MongoClient(host=config.host, port=config.port, username=config.username, password=config.password)
        db = client[config.db]
        return db
    

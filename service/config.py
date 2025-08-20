import os



host=os.getenv("MONGO_HOST", "mongodb:// mongodb-community-server")
port=int(os.getenv("MONGO_PORT", 27017))
username=os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
password=os.getenv("MONGO_INITDB_ROOT_PASSWORD", "pass")
db = os.getenv("MONGO_INITDB_DATABASE", "mongodb-crud-server")
collection = os.getenv("MONGO_COLLECTION", "soldiers")

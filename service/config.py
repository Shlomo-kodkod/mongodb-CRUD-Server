import os



host=os.getenv("MONGO_HOST", "mongodb://localhost"),
port=int(os.getenv("MONGO_PORT", 27017)),
username=os.getenv("MONGO_USER", "admin"),
password=os.getenv("MONGO_PASSWORD", "pass")
db = os.getenv("MONGO_DATABASE", "mongodb-crud-server")
collection = os.getenv("MONGO_COLLECTION", "soldiers")
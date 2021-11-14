import os


SETTINGS = {
    "MONGODB_SETTINGS": {
        "db": os.environ.get("MONGO_DB_NAME"),
        "host": os.environ.get("MONGO_DB_HOST"),
        "port": int(os.environ.get("MONGO_DB_PORT")),
        "username": os.environ.get("MONGO_DB_USER"),
        "password": os.environ.get("MONGO_DB_PASSWORD"),
        "authentication_source": os.environ.get("MONGO_DB_AUTH_SOURCE")
    },
    "PERSPECTIVE_API": os.environ.get("PERSPECTIVE_API_KEY"),
    "TOXICITY_THRESHOLD": 0.7
}

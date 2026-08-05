from typing import Any, Mapping
from pymongo import MongoClient
from configs import Configs
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

try:
    client: MongoClient[Mapping[str, Any]] = MongoClient(
        Configs.URI, timeoutMS=5000, serverSelectionTimeoutMS=5000, maxIdleTimeMS=45000
    )
    client.admin.command("ping")
    db = client[Configs.DB_NAME]
    print("Successfully connected to MongoDB", flush=True)
except ServerSelectionTimeoutError:
    print("Error: Connection timed out (check your IP or permissions)", flush=True)
except ConnectionFailure:
    print("Error: Could not connect to the MongoDB server", flush=True)
except Exception as e:
    print(f"An unexpected error occurred: {e}", flush=True)

__all__ = ["db"]

import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient

from backend.common import log
from backend.core.conf import settings


def create_mongo_client() -> AsyncIOMotorClient:
    try:
        return AsyncIOMotorClient(
            settings.MONGODB_URI,
            serverSelectionTimeoutMS=settings.MONGODB_CONNECTION_TIMEOUT,
        )
    except Exception as e:
        log.error("❌ Failed to connect to MongoDB: %s", e)
        sys.exit()


mongo_client = create_mongo_client()


async def check_mongo_connection(max_retries: int = 3, retry_interval: str = 1) -> None:
    try:
        await mongo_client.admin.command("ping")
        log.success("MongoDB connection successful")
    except Exception:
        if max_retries <= 0:
            log.error("❌ Failed to connect to MongoDB")
            sys.exit()
        else:
            log.warning(
                f"Retrying MongoDB connection... {max_retries}",
            )
            time.sleep(retry_interval)
            return await check_mongo_connection(max_retries - 1)

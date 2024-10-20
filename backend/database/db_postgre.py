import sys
import time

import asyncpg

from backend.core import log
from backend.core.conf import settings


async def create_postgres_client():
    """Create a connection pool to PostgreSQL"""
    try:
        return await asyncpg.create_pool(
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DB,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
        )
    except Exception as e:
        log.error("❌ Failed to connect to PostgreSQL: %s", e)
        sys.exit()


postgres_client = create_postgres_client()


async def check_postgres_connection(
    max_retries: int = 3, retry_interval: int = 1
) -> None:
    """Check connection to PostgreSQL, retry if necessary"""
    try:
        async with postgres_client.acquire() as connection:
            await connection.execute("SELECT 1")
            log.success("PostgreSQL connection successful")
    except Exception as e:
        if max_retries <= 0:
            log.error("❌ Failed to connect to PostgreSQL after retries: %s", e)
            sys.exit()
        else:
            log.warning(f"Retrying PostgreSQL connection... {max_retries} retries left")
            time.sleep(retry_interval)
            await check_postgres_connection(max_retries - 1)

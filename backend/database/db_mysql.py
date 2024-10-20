import sys

from typing import Annotated
from uuid import uuid4

from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from backend.common.log import log
from backend.common.model import MappedBase
from backend.core.conf import settings


def create_engine_and_session(url: str | URL):
    try:
        engine = create_async_engine(
            url, echo=settings.MYSQL_ECHO, future=True, pool_pre_ping=True
        )
    except Exception as e:
        log.error("❌ Database connection failed {}", e)
        sys.exit()
    else:
        db_session = async_sessionmaker(
            bind=engine, autoflush=False, expire_on_commit=False
        )
        return engine, db_session


SQLALCHEMY_DATABASE_URL = settings.MYSQL_DATABASE_URL

async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)


async def get_db() -> AsyncSession:
    session = async_db_session()
    try:
        yield session
    except Exception as se:
        await session.rollback()
        raise se
    finally:
        await session.close()


# Session Annotated
CurrentSession = Annotated[AsyncSession, Depends(get_db)]


async def create_table():
    """Create database table"""
    async with async_engine.begin() as coon:
        await coon.run_sync(MappedBase.metadata.create_all)


def uuid4_str() -> str:
    """Database Engine UUID Type Compatibility Solution"""
    return str(uuid4())

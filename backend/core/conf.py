from functools import lru_cache
from typing import Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.core.path_conf import BasePath


class Settings(BaseSettings):
    """Global Settings"""

    model_config = SettingsConfigDict(
        env_file=f"{BasePath}/.env", env_file_encoding="utf-8", extra="ignore"
    )

    # Env Config
    ENVIRONMENT: Literal["dev", "pro"]

    # Env MySQL
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    # Env Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DATABASE: int

    # Env Token
    TOKEN_SECRET_KEY: str

    # Env Opera Log
    OPERA_LOG_ENCRYPT_SECRET_KEY: str

    # FastAPI
    FASTAPI_API_V1_PATH: str = "/api/v1"
    FASTAPI_TITLE: str = "FastAPI"
    FASTAPI_VERSION: str = "0.0.1"
    FASTAPI_DESCRIPTION: str = ""
    FASTAPI_DOCS_URL: str | None = f"{FASTAPI_API_V1_PATH}/docs"
    FASTAPI_REDOCS_URL: str | None = f"{FASTAPI_API_V1_PATH}/redocs"
    FASTAPI_OPENAPI_URL: str | None = f"{FASTAPI_API_V1_PATH}/openapi"
    FASTAPI_STATIC_FILES: bool = False

    @model_validator(mode="before")
    @classmethod
    def validate_openapi_url(cls, values):
        if values["ENVIRONMENT"] == "pro":
            values["OPENAPI_URL"] = None
        return values

    # MySQL
    MYSQL_ECHO: bool = False
    MYSQL_DATABASE: str = "fba"
    MYSQL_CHARSET: str = "utf8mb4"

    # Redis
    REDIS_TIMEOUT: int = 5

    # Token
    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1
    TOKEN_REFRESH_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
    TOKEN_REDIS_PREFIX: str = "fba:token"
    TOKEN_REFRESH_REDIS_PREFIX: str = "fba:refresh_token"
    TOKEN_REQUEST_PATH_EXCLUDE: list[str] = [
        f"{FASTAPI_API_V1_PATH}/auth/login",
    ]

    # JWT
    JWT_USER_REDIS_PREFIX: str = ""
    JWT_USER_REDIS_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7

    # Permission (RBAC)
    PERMISSION_MODE: Literal["casbin", "role-menu"] = "casbin"
    PERMISSION_REDIS_PREFIX: str = "fba:permission"

    # RBAC
    # Casbin
    RBAC_CASBIN_EXCLUDE: set[tuple[str, str]] = {
        ("POST", f"{FASTAPI_API_V1_PATH}/auth/logout"),
        ("POST", f"{FASTAPI_API_V1_PATH}/auth/token/new"),
    }

    # Role-Menu
    RBAC_ROLE_MENU_EXCLUDE: list[str] = [
        "sys:monitor:redis",
        "sys:monitor:server",
    ]

    # Cookies
    COOKIE_REFRESH_TOKEN_KEY: str = ""
    COOKIE_REFRESH_TOKEN_EXPIRE_SECONDS: int = TOKEN_REFRESH_EXPIRE_SECONDS

    # Log
    LOG_ROOT_LEVEL: str = "NOTSET"
    LOG_STD_FORMAT: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</> | <lvl>{level: <8}</> | "
        "<cyan> {correlation_id} </> | <lvl>{message}</>"
    )
    LOG_LOGURU_FORMAT: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</> | <lvl>{level: <8}</> | "
        "<cyan> {correlation_id} </> | <lvl>{message}</>"
    )
    LOG_CID_DEFAULT_VALUE: str = "-"
    LOG_CID_UUID_LENGTH: int = 32
    LOG_STDOUT_LEVEL: str = "INFO"
    LOG_STDERR_LEVEL: str = "ERROR"
    LOG_STDOUT_FILENAME: str = "fba_access.log"
    LOG_STDERR_FILENAME: str = "fba_error.log"

    # Middleware
    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_ACCESS: bool = True

    # Trace ID
    TRACE_ID_REQUEST_HEADER_KEY: str = "X-Request-ID"

    # CORS
    CORS_ALLOWED_ORIGINS: list[str] = [
        "http://localhost:5173",
    ]
    CORS_EXPOSE_HEADERS: list[str] = [
        TRACE_ID_REQUEST_HEADER_KEY,
    ]

    # DateTime
    DATETIME_TIMEZONE: str = "UTC"
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    # Request limiter
    REQUEST_LIMITER_REDIS_PREFIX: str = ""

    # Demo mode (Only GET, OPTIONS requests are allowed)
    DEMO_MODE: bool = False
    DEMO_MODE_EXCLUDE: set[tuple[str, str]] = {
        ("POST", f"{FASTAPI_API_V1_PATH}/auth/login"),
        ("POST", f"{FASTAPI_API_V1_PATH}/auth/logout"),
        ("GET", f"{FASTAPI_API_V1_PATH}/auth/captcha"),
    }

    # Ip location
    IP_LOCATION_PARSE: Literal["online", "offline", "false"] = "offline"
    IP_LOCATION_REDIS_PREFIX: str = "fba:ip:location"
    IP_LOCATION_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1

    # Opera log
    OPERA_LOG_PATH_EXCLUDE: list[str] = [
        "/favicon.ico",
        FASTAPI_DOCS_URL,
        FASTAPI_REDOCS_URL,
        FASTAPI_OPENAPI_URL,
        f"{FASTAPI_API_V1_PATH}/auth/login/swagger",
        f"{FASTAPI_API_V1_PATH}/oauth2/github/callback",
        f"{FASTAPI_API_V1_PATH}/oauth2/linux-do/callback",
    ]
    OPERA_LOG_ENCRYPT_TYPE: int = 1
    OPERA_LOG_ENCRYPT_KEY_INCLUDE: list[str] = [
        "password",
        "old_password",
        "new_password",
        "confirm_password",
    ]


@lru_cache
def get_settings() -> Settings:
    """Get settings"""
    return Settings()


# Global settings
settings = get_settings()

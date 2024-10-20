from fast_captcha import img_captcha
from fastapi import APIRouter, Depends, Request
from fastapi_limiter.depends import RateLimiter
from starlette.concurrency import run_in_threadpool

from backend.app.admin.conf import admin_settings
from backend.common.response.response_schema import ResponseModel, response_base
from backend.database.db_redis import redis_client

router = APIRouter()


@router.get(
    "",
    summary="Get captcha",
    dependencies=[Depends(RateLimiter(times=5, seconds=10))],
)
async def get_captcha(request: Request) -> ResponseModel:
    """
    Get captcha
    """
    img_type: str = "base64"
    img, code = await run_in_threadpool(img_captcha, img_byte=img_type)
    ip = request.state.ip
    await redis_client.set(
        f"{admin_settings.CAPTCHA_LOGIN_REDIS_PREFIX}:{ip}",
        code,
        ex=admin_settings.CAPTCHA_LOGIN_EXPIRE_SECONDS,
    )
    return response_base.success(data={"image_type": img_type, "image": img})

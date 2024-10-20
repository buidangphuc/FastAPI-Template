from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import HTTPBasicCredentials
from fastapi_limiter.depends import RateLimiter
from starlette.background import BackgroundTasks

from backend.app.admin.schema.token import GetSwaggerToken
from backend.app.admin.schema.user import AuthLoginParam
from backend.app.admin.service.auth_service import auth_service
from backend.common.response.response_schema import ResponseModel, response_base
from backend.common.security.jwt import DependsJwtAuth

router = APIRouter()


@router.post(
    "/login/swagger",
    summary="swagger debug only",
    description="Used to quickly obtain token for swagger authentication",
)
async def swagger_login(
    obj: Annotated[HTTPBasicCredentials, Depends()]
) -> GetSwaggerToken:
    token, user = await auth_service.swagger_login(obj=obj)
    return GetSwaggerToken(access_token=token, user=user)  # type: ignore


@router.post(
    "/login",
    summary="User login",
    description="Login in json format, only supports debugging with third-party API tools",  # Postman
    dependencies=[Depends(RateLimiter(times=5, minutes=1))],
)
async def user_login(
    request: Request,
    response: Response,
    obj: AuthLoginParam,
    background_tasks: BackgroundTasks,
) -> ResponseModel:
    data = await auth_service.login(
        request=request, response=response, obj=obj, background_tasks=background_tasks
    )
    return response_base.success(data=data)


@router.post("/token/new", summary="Create new token", dependencies=[DependsJwtAuth])
async def create_new_token(request: Request, response: Response) -> ResponseModel:
    data = await auth_service.new_token(request=request, response=response)
    return response_base.success(data=data)


@router.post("/logout", summary="User logout", dependencies=[DependsJwtAuth])
async def user_logout(request: Request, response: Response) -> ResponseModel:
    await auth_service.logout(request=request, response=response)
    return response_base.success()

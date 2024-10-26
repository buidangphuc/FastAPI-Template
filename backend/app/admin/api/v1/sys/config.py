from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from backend.app.admin.schema.config import CreateConfigParam, UpdateConfigParam
from backend.app.admin.service.config_service import config_service
from backend.common.response.response_schema import ResponseModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC

router = APIRouter()


@router.get(
    "", summary="Get system configuration details", dependencies=[DependsJwtAuth]
)
async def get_config() -> ResponseModel:
    config = await config_service.get()
    return response_base.success(data=config)


@router.post(
    "",
    summary="Create system configuration",
    dependencies=[
        Depends(RequestPermission("sys:config:add")),
        DependsRBAC,
    ],
)
async def create_config(obj: CreateConfigParam) -> ResponseModel:
    await config_service.create(obj=obj)
    return response_base.success()


@router.put(
    "/{pk}",
    summary="Update system configuration",
    dependencies=[
        Depends(RequestPermission("sys:config:edit")),
        DependsRBAC,
    ],
)
async def update_config(
    pk: Annotated[int, Path(...)], obj: UpdateConfigParam
) -> ResponseModel:
    count = await config_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    "",
    summary="Delete system configuration",
    dependencies=[
        Depends(RequestPermission("sys:config:del")),
        DependsRBAC,
    ],
)
async def delete_config(pk: Annotated[list[int], Query(...)]) -> ResponseModel:
    count = await config_service.delete(pk=pk)
    if count > 0:
        return response_base.success()
    return response_base.fail()

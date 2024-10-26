from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Request

from backend.app.admin.schema.menu import (
    CreateMenuParam,
    GetMenuListDetails,
    UpdateMenuParam,
)
from backend.app.admin.service.menu_service import menu_service
from backend.common.response.response_schema import ResponseModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.utils.serializers import select_as_dict

router = APIRouter()


@router.get(
    "/sidebar", summary="Get user menu display tree", dependencies=[DependsJwtAuth]
)
async def get_user_sidebar_tree(request: Request) -> ResponseModel:
    menu = await menu_service.get_user_menu_tree(request=request)
    return response_base.success(data=menu)


@router.get("/{pk}", summary="Get menu details", dependencies=[DependsJwtAuth])
async def get_menu(pk: Annotated[int, Path(...)]) -> ResponseModel:
    menu = await menu_service.get(pk=pk)
    data = GetMenuListDetails(**select_as_dict(menu))
    return response_base.success(data=data)


@router.get("", summary="Get all menu display trees", dependencies=[DependsJwtAuth])
async def get_all_menus(
    title: Annotated[str | None, Query()] = None,
    status: Annotated[int | None, Query()] = None,
) -> ResponseModel:
    menu = await menu_service.get_menu_tree(title=title, status=status)
    return response_base.success(data=menu)


@router.post(
    "",
    summary="Create menu",
    dependencies=[
        Depends(RequestPermission("sys:menu:add")),
        DependsRBAC,
    ],
)
async def create_menu(obj: CreateMenuParam) -> ResponseModel:
    await menu_service.create(obj=obj)
    return response_base.success()


@router.put(
    "/{pk}",
    summary="Update menu",
    dependencies=[
        Depends(RequestPermission("sys:menu:edit")),
        DependsRBAC,
    ],
)
async def update_menu(
    pk: Annotated[int, Path(...)], obj: UpdateMenuParam
) -> ResponseModel:
    count = await menu_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    "/{pk}",
    summary="Delete menu",
    dependencies=[
        Depends(RequestPermission("sys:menu:del")),
        DependsRBAC,
    ],
)
async def delete_menu(pk: Annotated[int, Path(...)]) -> ResponseModel:
    count = await menu_service.delete(pk=pk)
    if count > 0:
        return response_base.success()
    return response_base.fail()

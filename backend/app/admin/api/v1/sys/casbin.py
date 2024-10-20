from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from backend.app.admin.schema.casbin_rule import (
    CreatePolicyParam,
    CreateUserRoleParam,
    DeleteAllPoliciesParam,
    DeletePolicyParam,
    DeleteUserRoleParam,
    GetPolicyListDetails,
    UpdatePolicyParam,
)
from backend.app.admin.service.casbin_service import casbin_service
from backend.common.pagination import DependsPagination, paging_data
from backend.common.response.response_schema import ResponseModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.database.db_mysql import CurrentSession

router = APIRouter()


@router.get(
    "",
    summary="Get all casbin policies",
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_pagination_casbin(
    db: CurrentSession,
    ptype: Annotated[str | None, Query(description="Strategy Type")] = None,
    sub: Annotated[str | None, Query(description="User uuid/ Role ID")] = None,
) -> ResponseModel:
    casbin_select = await casbin_service.get_casbin_list(ptype=ptype, sub=sub)
    page_data = await paging_data(db, casbin_select, GetPolicyListDetails)
    return response_base.success(data=page_data)


@router.get(
    "/policies", summary="Get all casbin policies", dependencies=[DependsJwtAuth]
)
async def get_all_policies(
    role: Annotated[int | None, Query(description="角色ID")] = None
) -> ResponseModel:
    policies = await casbin_service.get_policy_list(role=role)
    return response_base.success(data=policies)


@router.post(
    "/policy",
    summary="Add P permission policy",
    dependencies=[
        Depends(RequestPermission("casbin:p:add")),
        DependsRBAC,
    ],
)
async def create_policy(p: CreatePolicyParam) -> ResponseModel:
    data = await casbin_service.create_policy(p=p)
    return response_base.success(data=data)


@router.post(
    "/policies",
    summary="Add multiple P permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:p:group:add")),
        DependsRBAC,
    ],
)
async def create_policies(ps: list[CreatePolicyParam]) -> ResponseModel:
    data = await casbin_service.create_policies(ps=ps)
    return response_base.success(data=data)


@router.put(
    "/policy",
    summary="Update P permission policy",
    dependencies=[
        Depends(RequestPermission("casbin:p:edit")),
        DependsRBAC,
    ],
)
async def update_policy(
    old: UpdatePolicyParam, new: UpdatePolicyParam
) -> ResponseModel:
    data = await casbin_service.update_policy(old=old, new=new)
    return response_base.success(data=data)


@router.put(
    "/policies",
    summary="Update multiple P permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:p:group:edit")),
        DependsRBAC,
    ],
)
async def update_policies(
    old: list[UpdatePolicyParam], new: list[UpdatePolicyParam]
) -> ResponseModel:
    data = await casbin_service.update_policies(old=old, new=new)
    return response_base.success(data=data)


@router.delete(
    "/policy",
    summary="Delete P permission policy",
    dependencies=[
        Depends(RequestPermission("casbin:p:del")),
        DependsRBAC,
    ],
)
async def delete_policy(p: DeletePolicyParam) -> ResponseModel:
    data = await casbin_service.delete_policy(p=p)
    return response_base.success(data=data)


@router.delete(
    "/policies",
    summary="Delete multiple P permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:p:group:del")),
        DependsRBAC,
    ],
)
async def delete_policies(ps: list[DeletePolicyParam]) -> ResponseModel:
    data = await casbin_service.delete_policies(ps=ps)
    return response_base.success(data=data)


@router.delete(
    "/policies/all",
    summary="Delete all P permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:p:empty")),
        DependsRBAC,
    ],
)
async def delete_all_policies(sub: DeleteAllPoliciesParam) -> ResponseModel:
    count = await casbin_service.delete_all_policies(sub=sub)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.get(
    "/groups", summary="Get all G permission policies", dependencies=[DependsJwtAuth]
)
async def get_all_groups() -> ResponseModel:
    data = await casbin_service.get_group_list()
    return response_base.success(data=data)


@router.post(
    "/group",
    summary="Add G permission policy",
    dependencies=[
        Depends(RequestPermission("casbin:g:add")),
        DependsRBAC,
    ],
)
async def create_group(g: CreateUserRoleParam) -> ResponseModel:
    data = await casbin_service.create_group(g=g)
    return response_base.success(data=data)


@router.post(
    "/groups",
    summary="Add multiple G permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:g:group:add")),
        DependsRBAC,
    ],
)
async def create_groups(gs: list[CreateUserRoleParam]) -> ResponseModel:
    data = await casbin_service.create_groups(gs=gs)
    return response_base.success(data=data)


@router.delete(
    "/group",
    summary="Delete G permission policy",
    dependencies=[
        Depends(RequestPermission("casbin:g:del")),
        DependsRBAC,
    ],
)
async def delete_group(g: DeleteUserRoleParam) -> ResponseModel:
    data = await casbin_service.delete_group(g=g)
    return response_base.success(data=data)


@router.delete(
    "/groups",
    summary="Delete multiple G permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:g:group:del")),
        DependsRBAC,
    ],
)
async def delete_groups(gs: list[DeleteUserRoleParam]) -> ResponseModel:
    data = await casbin_service.delete_groups(gs=gs)
    return response_base.success(data=data)


@router.delete(
    "/groups/all",
    summary="Delete all G permission policies",
    dependencies=[
        Depends(RequestPermission("casbin:g:empty")),
        DependsRBAC,
    ],
)
async def delete_all_groups(uuid: Annotated[UUID, Query(...)]) -> ResponseModel:
    count = await casbin_service.delete_all_groups(uuid=uuid)
    if count > 0:
        return response_base.success()
    return response_base.fail()

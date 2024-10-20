from datetime import datetime

from pydantic import ConfigDict, Field

from backend.app.admin.schema.menu import GetMenuListDetails
from backend.common.enums import RoleDataScopeType, StatusType
from backend.common.schema import SchemaBase


class RoleSchemaBase(SchemaBase):
    name: str
    data_scope: RoleDataScopeType = Field(
        default=RoleDataScopeType.custom,
        description="Permission scope (1: All data permissions 2: Custom data permissions",
    )
    status: StatusType = Field(default=StatusType.enable)
    remark: str | None = None


class CreateRoleParam(RoleSchemaBase):
    pass


class UpdateRoleParam(RoleSchemaBase):
    pass


class UpdateRoleMenuParam(SchemaBase):
    menus: list[int]


class GetRoleListDetails(RoleSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None
    menus: list[GetMenuListDetails]

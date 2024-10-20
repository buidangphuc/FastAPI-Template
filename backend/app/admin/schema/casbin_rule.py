from pydantic import ConfigDict, Field

from backend.common.enums import MethodType
from backend.common.schema import SchemaBase


class CreatePolicyParam(SchemaBase):
    sub: str = Field(..., description="User uuid/role ID")
    path: str = Field(..., description="Request path")
    method: MethodType = Field(default=MethodType.GET, description="Request method")


class UpdatePolicyParam(CreatePolicyParam):
    pass


class DeletePolicyParam(CreatePolicyParam):
    pass


class DeleteAllPoliciesParam(SchemaBase):
    uuid: str | None = None
    role: str


class CreateUserRoleParam(SchemaBase):
    uuid: str = Field(..., description="User uuid")
    role: str = Field(..., description="Role ID")


class DeleteUserRoleParam(CreateUserRoleParam):
    pass


class GetPolicyListDetails(SchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ptype: str = Field(..., description="Policy type")
    v0: str = Field(..., description="User uuid/role ID")
    v1: str = Field(..., description="Request path")
    v2: str | None = None
    v3: str | None = None
    v4: str | None = None
    v5: str | None = None

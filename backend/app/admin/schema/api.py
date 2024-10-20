from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.enums import MethodType
from backend.common.schema import SchemaBase


class ApiSchemaBase(SchemaBase):
    name: str
    method: MethodType = Field(default=MethodType.GET, description="Request method")
    path: str = Field(..., description="Request path")
    remark: str | None = None


class CreateApiParam(ApiSchemaBase):
    pass


class UpdateApiParam(ApiSchemaBase):
    pass


class GetApiListDetails(ApiSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

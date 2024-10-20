from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.schema import SchemaBase


class ConfigSchemaBase(SchemaBase):
    login_title: str = Field()
    login_sub_title: str = Field()
    footer: str = Field()
    logo: str = Field()
    system_title: str = Field()
    system_comment: str = Field()


class CreateConfigParam(ConfigSchemaBase):
    pass


class UpdateConfigParam(ConfigSchemaBase):
    pass


class GetConfigListDetails(ConfigSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

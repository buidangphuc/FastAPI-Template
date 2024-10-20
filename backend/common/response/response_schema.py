from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict

from common import settings
from common.response.response_code import CustomResponse, CustomResponseCode

_ExcludeData = set[int | str] | dict[int | str, Any]


class ResponseModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: lambda x: x.strftime(settings.DATETIME_FORMAT)}
    )
    code: int = CustomResponseCode.HTTP_200.code
    message: str = CustomResponseCode.HTTP_200.message
    data: Any | None = None


class ResponseBase:

    @staticmethod
    async def __response(
        *, res: CustomResponseCode | CustomResponse = None, data: Any | None = None
    ):
        return ResponseModel(code=res.code, message=res.message, data=data)

    async def success(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_200,
        data: Any | None = None,
    ) -> ResponseModel:
        return await self.__response(res=res, data=data)

    async def fail(
        self,
        *,
        res: CustomResponseCode | CustomResponse = CustomResponseCode.HTTP_400,
        data: Any = None,
    ) -> ResponseModel:
        return await self.__response(res=res, data=data)


response_base = ResponseBase()

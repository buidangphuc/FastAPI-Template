from sqlalchemy import Select

from backend.app.admin.crud.crud_dict_type import dict_type_dao
from backend.app.admin.schema.dict_type import (
    CreateDictTypeParam,
    UpdateDictTypeParam,
)
from backend.common.exception import errors
from backend.database.db_mysql import async_db_session


class DictTypeService:

    @staticmethod
    async def get_select(
        *, name: str = None, code: str = None, status: int = None
    ) -> Select:
        return await dict_type_dao.get_list(name=name, code=code, status=status)

    @staticmethod
    async def create(*, obj: CreateDictTypeParam) -> None:
        async with async_db_session.begin() as db:
            dict_type = await dict_type_dao.get_by_code(db, obj.code)
            if dict_type:
                raise errors.ForbiddenError(msg="Dictionary type already exists")
            await dict_type_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateDictTypeParam) -> int:
        async with async_db_session.begin() as db:
            dict_type = await dict_type_dao.get(db, pk)
            if not dict_type:
                raise errors.NotFoundError(msg="Dictionary type does not exist")
            if dict_type.code != obj.code:
                if await dict_type_dao.get_by_code(db, obj.code):
                    raise errors.ForbiddenError(msg="Dictionary type already exists")
            count = await dict_type_dao.update(db, pk, obj)
            return count

    @staticmethod
    async def delete(*, pk: list[int]) -> int:
        async with async_db_session.begin() as db:
            count = await dict_type_dao.delete(db, pk)
            return count


dict_type_service = DictTypeService()

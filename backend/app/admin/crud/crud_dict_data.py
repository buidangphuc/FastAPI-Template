from sqlalchemy import Select, and_, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.admin.model import DictData
from backend.app.admin.schema.dict_data import (
    CreateDictDataParam,
    UpdateDictDataParam,
)


class CRUDDictData(CRUDPlus[DictData]):

    async def get(self, db: AsyncSession, pk: int) -> DictData | None:
        """
        Get dict data by id

        :param db:
        :param pk:
        :return:
        """
        return await self.select_model(db, pk)

    async def get_list(
        self, label: str = None, value: str = None, status: int = None
    ) -> Select:
        """
        Get dict data list

        :param label:
        :param value:
        :param status:
        :return:
        """
        stmt = (
            select(self.model)
            .options(selectinload(self.model.type))
            .order_by(desc(self.model.sort))
        )
        where_list = []
        if label is not None:
            where_list.append(self.model.label.like(f"%{label}%"))
        if value is not None:
            where_list.append(self.model.value.like(f"%{value}%"))
        if status is not None:
            where_list.append(self.model.status == status)
        if where_list:
            stmt = stmt.where(and_(*where_list))
        return stmt

    async def get_by_label(self, db: AsyncSession, label: str) -> DictData | None:
        """
        Get dict data by label

        :param db:
        :param label:
        :return:
        """
        return await self.select_model_by_column(db, label=label)

    async def create(self, db: AsyncSession, obj_in: CreateDictDataParam) -> None:
        """
        Create dict data

        :param db:
        :param obj_in:
        :return:
        """
        await self.create_model(db, obj_in)

    async def update(
        self, db: AsyncSession, pk: int, obj_in: UpdateDictDataParam
    ) -> int:
        """
        Update dict data

        :param db:
        :param pk:
        :param obj_in:
        :return:
        """
        return await self.update_model(db, pk, obj_in)

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        """
        Delete dict data

        :param db:
        :param pk:
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pk)

    async def get_with_relation(self, db: AsyncSession, pk: int) -> DictData | None:
        """
        Get dict data with relation

        :param db:
        :param pk:
        :return:
        """
        stmt = (
            select(self.model)
            .options(selectinload(self.model.type))
            .where(self.model.id == pk)
        )
        dict_data = await db.execute(stmt)
        return dict_data.scalars().first()


dict_data_dao: CRUDDictData = CRUDDictData(DictData)

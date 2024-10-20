from typing import Sequence

from sqlalchemy import Select, desc, select
from sqlalchemy.orm import selectinload
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.admin.model import Menu, Role, User
from backend.app.admin.schema.role import (
    CreateRoleParam,
    UpdateRoleMenuParam,
    UpdateRoleParam,
)


class CRUDRole(CRUDPlus[Role]):

    async def get(self, db, role_id: int) -> Role | None:
        """
        Get role by id

        :param db:
        :param role_id:
        :return:
        """
        return await self.select_model(db, role_id)

    async def get_with_relation(self, db, role_id: int) -> Role | None:
        """
        Get role with relation by id

        :param db:
        :param role_id:
        :return:
        """
        stmt = (
            select(self.model)
            .options(selectinload(self.model.menus))
            .where(self.model.id == role_id)
        )
        role = await db.execute(stmt)
        return role.scalars().first()

    async def get_all(self, db) -> Sequence[Role]:
        """
        Get all roles

        :param db:
        :return:
        """
        return await self.select_models(db)

    async def get_user_roles(self, db, user_id: int) -> Sequence[Role]:
        """
        Get user roles

        :param db:
        :param user_id:
        :return:
        """
        stmt = select(self.model).join(self.model.users).where(User.id == user_id)
        roles = await db.execute(stmt)
        return roles.scalars().all()

    async def get_list(
        self, name: str = None, data_scope: int = None, status: int = None
    ) -> Select:
        """
        Get role list

        :param name:
        :param data_scope:
        :param status:
        :return:
        """
        stmt = (
            select(self.model)
            .options(selectinload(self.model.menus))
            .order_by(desc(self.model.created_time))
        )
        where_list = []
        if name:
            where_list.append(self.model.name.like(f"%{name}%"))
        if data_scope:
            where_list.append(self.model.data_scope == data_scope)
        if status is not None:
            where_list.append(self.model.status == status)
        if where_list:
            stmt = stmt.where(*where_list)
        return stmt

    async def get_by_name(self, db, name: str) -> Role | None:
        """
        Get role by name

        :param db:
        :param name:
        :return:
        """
        return await self.select_model_by_column(db, name=name)

    async def create(self, db, obj_in: CreateRoleParam) -> None:
        """
        Create role

        :param db:
        :param obj_in:
        :return:
        """
        await self.create_model(db, obj_in)

    async def update(self, db, role_id: int, obj_in: UpdateRoleParam) -> int:
        """
        Update role

        :param db:
        :param role_id:
        :param obj_in:
        :return:
        """
        return await self.update_model(db, role_id, obj_in)

    async def update_menus(
        self, db, role_id: int, menu_ids: UpdateRoleMenuParam
    ) -> int:
        """
        Update role menus

        :param db:
        :param role_id:
        :param menu_ids:
        :return:
        """
        current_role = await self.get_with_relation(db, role_id)
        stmt = select(Menu).where(Menu.id.in_(menu_ids.menus))
        menus = await db.execute(stmt)
        current_role.menus = menus.scalars().all()
        return len(current_role.menus)

    async def delete(self, db, role_id: list[int]) -> int:
        """
        Delete role

        :param db:
        :param role_id:
        :return:
        """
        return await self.delete_model_by_column(
            db, allow_multiple=True, id__in=role_id
        )


role_dao: CRUDRole = CRUDRole(Role)

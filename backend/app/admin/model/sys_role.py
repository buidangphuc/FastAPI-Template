from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.admin.model.sys_role_menu import sys_role_menu
from backend.app.admin.model.sys_user_role import sys_user_role
from backend.common.model import Base, id_key


class Role(Base):
    """Role"""

    __tablename__ = "sys_role"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(20), unique=True, comment="Role name")
    data_scope: Mapped[int | None] = mapped_column(
        default=2, comment="Permission scope"
    )  # 1: All data permissions 2: Custom data permissions
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 1: Enable 2: Disable
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT, default=None, comment="Description"
    )

    users: Mapped[list["User"]] = relationship(
        init=False, secondary=sys_user_role, back_populates="roles"
    )

    menus: Mapped[list["Menu"]] = relationship(
        init=False, secondary=sys_role_menu, back_populates="roles"
    )

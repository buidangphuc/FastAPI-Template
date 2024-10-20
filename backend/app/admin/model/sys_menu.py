from typing import Union

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.admin.model.sys_role_menu import sys_role_menu
from backend.common.model import Base, id_key


class Menu(Base):
    """System menu"""

    __tablename__ = "sys_menu"

    id: Mapped[id_key] = mapped_column(init=False)
    title: Mapped[str] = mapped_column(String(50), comment="Menu title")
    name: Mapped[str] = mapped_column(String(50), comment="Menu name")
    level: Mapped[int] = mapped_column(default=0, comment="Menu level")
    sort: Mapped[int] = mapped_column(default=0, comment="Sort")
    icon: Mapped[str | None] = mapped_column(String(100), default=None, comment="Icon")
    path: Mapped[str | None] = mapped_column(String(200), default=None, comment="Path")
    menu_type: Mapped[int] = mapped_column(
        default=0, comment="Menu type"
    )  # 0: Directory, 1: Menu, 2: Button
    component: Mapped[str | None] = mapped_column(
        String(255), default=None, comment="Component"
    )
    perms: Mapped[str | None] = mapped_column(
        String(100), default=None, comment="Permission"
    )
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 0: Disable, 1: Enable
    show: Mapped[int] = mapped_column(default=1, comment="Show")  # 0: Hide, 1: Show
    cache: Mapped[int] = mapped_column(default=1, comment="Cache")  # 0: No, 1: Yes
    remark: Mapped[str | None] = mapped_column(LONGTEXT, default=None, comment="Remark")
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("sys_menu.id", ondelete="SET NULL"),
        default=None,
        index=True,
        comment="Parent ID",
    )
    parent: Mapped[Union["Menu", None]] = relationship(
        init=False, back_populates="children", remote_side=[id]
    )
    children: Mapped[list["Menu"] | None] = relationship(
        init=False, back_populates="parent"
    )
    roles: Mapped[list["Role"]] = relationship(  # noqa: F821
        init=False, secondary=sys_role_menu, back_populates="menus"
    )

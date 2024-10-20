from datetime import datetime
from typing import Union

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.admin.model.sys_user_role import sys_user_role
from backend.common.model import Base, id_key
from backend.database.db_mysql import uuid4_str
from backend.utils.timezone import timezone


class User(Base):
    """User"""

    __tablename__ = "sys_user"

    id: Mapped[id_key] = mapped_column(init=False)
    uuid: Mapped[str] = mapped_column(
        String(50), init=False, default_factory=uuid4_str, unique=True
    )
    username: Mapped[str] = mapped_column(
        String(20), unique=True, index=True, comment="Username"
    )
    nickname: Mapped[str] = mapped_column(String(20), unique=True, comment="Nickname")
    password: Mapped[str | None] = mapped_column(String(255), comment="Password")
    salt: Mapped[str | None] = mapped_column(String(5), comment="Salt")
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, comment="Email"
    )
    is_superuser: Mapped[bool] = mapped_column(
        default=False, comment="Superuser"
    )  # 0: No 1: Yes
    is_staff: Mapped[bool] = mapped_column(
        default=False, comment="Staff"
    )  # 0: No 1: Yes
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 1: Enable 2: Disable
    is_multi_login: Mapped[bool] = mapped_column(
        default=False, comment="Multiple login"
    )  # 0: No 1: Yes
    avatar: Mapped[str | None] = mapped_column(
        String(255), default=None, comment="Avatar"
    )
    phone: Mapped[str | None] = mapped_column(String(11), default=None, comment="Phone")
    join_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=timezone.now, comment="Join time"
    )
    last_login_time: Mapped[datetime | None] = mapped_column(
        init=False, onupdate=timezone.now, comment="Last login time"
    )
    dept_id: Mapped[int | None] = mapped_column(
        ForeignKey("sys_dept.id", ondelete="SET NULL"),
        default=None,
        comment="Department ID",
    )
    dept: Mapped[Union["Dept", None]] = relationship(init=False, back_populates="users")  # noqa: F821
    roles: Mapped[list["Role"]] = relationship(  # noqa: F821
        init=False, secondary=sys_user_role, back_populates="users"
    )
    socials: Mapped[list["UserSocial"]] = relationship(init=False, back_populates="user")  # noqa: F821

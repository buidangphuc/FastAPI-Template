from typing import Union

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.common.model import Base, id_key


class Dept(Base):
    """Department"""

    __tablename__ = "sys_dept"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), comment="Department name")
    level: Mapped[int] = mapped_column(default=0, comment="Level")
    sort: Mapped[int] = mapped_column(default=0, comment="Sort")
    leader: Mapped[str | None] = mapped_column(
        String(20), default=None, comment="Leader"
    )
    phone: Mapped[str | None] = mapped_column(String(11), default=None, comment="Phone")
    email: Mapped[str | None] = mapped_column(String(50), default=None, comment="Email")
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 0: Disable, 1: Enable
    del_flag: Mapped[bool] = mapped_column(
        default=False, comment="Delete flag"
    )  # 0: Not deleted, 1: Deleted
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("sys_dept.id", ondelete="SET NULL"),
        default=None,
        index=True,
        comment="Parent ID",
    )
    parent: Mapped[Union["Dept", None]] = relationship(
        init=False, back_populates="children", remote_side=[id]
    )
    children: Mapped[list["Dept"] | None] = relationship(
        init=False, back_populates="parent"
    )
    users: Mapped[list["User"]] = relationship(init=False, back_populates="dept")  # noqa: F821

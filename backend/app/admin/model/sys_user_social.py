from typing import Union

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.common.model import Base, id_key


class UserSocial(Base):
    """User social"""

    __tablename__ = "sys_user_social"

    id: Mapped[id_key] = mapped_column(init=False)
    source: Mapped[str] = mapped_column(String(20), comment="Source")
    open_id: Mapped[str | None] = mapped_column(
        String(20), default=None, comment="Third-party open id"
    )
    uid: Mapped[str | None] = mapped_column(
        String(20), default=None, comment="Third-party ID"
    )
    union_id: Mapped[str | None] = mapped_column(
        String(20), default=None, comment="Third-party union id"
    )
    scope: Mapped[str | None] = mapped_column(
        String(120), default=None, comment="Scope"
    )
    code: Mapped[str | None] = mapped_column(
        String(50), default=None, comment="User's authorization code"
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("sys_user.id", ondelete="SET NULL"),
        default=None,
        comment="用户关联ID",
    )
    user: Mapped[Union["User", None]] = relationship(init=False, back_populates="socials")  # noqa: F821

from datetime import datetime

from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import DataClassBase, id_key
from backend.utils.timezone import timezone


class LoginLog(DataClassBase):
    """Login log"""

    __tablename__ = "sys_login_log"

    id: Mapped[id_key] = mapped_column(init=False)
    user_uuid: Mapped[str] = mapped_column(String(50), comment="User UUID")
    username: Mapped[str] = mapped_column(String(20), comment="Username")
    status: Mapped[int] = mapped_column(
        insert_default=0, comment="Status"
    )  # 0: Fail, 1: Success
    ip: Mapped[str] = mapped_column(String(50), comment="IP")
    country: Mapped[str | None] = mapped_column(String(50), comment="Country")
    region: Mapped[str | None] = mapped_column(String(50), comment="Region")
    city: Mapped[str | None] = mapped_column(String(50), comment="City")
    user_agent: Mapped[str] = mapped_column(String(255), comment="User agent")
    os: Mapped[str | None] = mapped_column(String(50), comment="OS")
    browser: Mapped[str | None] = mapped_column(String(50), comment="Browser")
    device: Mapped[str | None] = mapped_column(String(50), comment="Device")
    msg: Mapped[str] = mapped_column(LONGTEXT, comment="Message")
    login_time: Mapped[datetime] = mapped_column(comment="Login time")
    created_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=timezone.now, comment="Created time"
    )

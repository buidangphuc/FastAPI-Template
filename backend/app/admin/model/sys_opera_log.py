from datetime import datetime

from sqlalchemy import String
from sqlalchemy.dialects.mysql import JSON, LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import DataClassBase, id_key
from backend.utils.timezone import timezone


class OperaLog(DataClassBase):
    """Operation log"""

    __tablename__ = "sys_opera_log"

    id: Mapped[id_key] = mapped_column(init=False)
    trace_id: Mapped[str] = mapped_column(String(32), comment="Trace ID")
    username: Mapped[str | None] = mapped_column(String(20), comment="Username")
    method: Mapped[str] = mapped_column(String(20), comment="Request method")
    title: Mapped[str] = mapped_column(String(255), comment="Operation title")
    path: Mapped[str] = mapped_column(String(500), comment="Request path")
    ip: Mapped[str] = mapped_column(String(50), comment="IP")
    country: Mapped[str | None] = mapped_column(String(50), comment="Country")
    region: Mapped[str | None] = mapped_column(String(50), comment="Region")
    city: Mapped[str | None] = mapped_column(String(50), comment="City")
    user_agent: Mapped[str] = mapped_column(String(255), comment="User agent")
    os: Mapped[str | None] = mapped_column(String(50), comment="OS")
    browser: Mapped[str | None] = mapped_column(String(50), comment="Browser")
    device: Mapped[str | None] = mapped_column(String(50), comment="Device")
    args: Mapped[str | None] = mapped_column(JSON(), comment="Request parameters")
    status: Mapped[int] = mapped_column(
        comment="Operation status"
    )  # 0: Fail, 1: Success
    code: Mapped[str] = mapped_column(
        String(20), insert_default="200", comment="Response code"
    )
    msg: Mapped[str | None] = mapped_column(LONGTEXT, comment="Message")
    cost_time: Mapped[float] = mapped_column(
        insert_default=0.0, comment="Cost time"
    )  # Unit: s
    opera_time: Mapped[datetime] = mapped_column(comment="Operation time")
    created_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=timezone.now, comment="Created time"
    )

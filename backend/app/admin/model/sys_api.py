from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class Api(Base):
    """System API"""

    __tablename__ = "sys_api"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), unique=True, comment="API Name")
    method: Mapped[str] = mapped_column(String(16), comment="Request method")
    path: Mapped[str] = mapped_column(String(500), comment="Request path")
    remark: Mapped[str | None] = mapped_column(LONGTEXT, comment="Remark")

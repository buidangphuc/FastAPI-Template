from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.common.model import Base, id_key


class DictType(Base):
    """Data dictionary type"""

    __tablename__ = "sys_dict_type"

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(
        String(32), unique=True, comment="Dictionary type name"
    )
    code: Mapped[str] = mapped_column(
        String(32), unique=True, comment="Dictionary type code"
    )
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 0: Disable, 1: Enable
    remark: Mapped[str | None] = mapped_column(LONGTEXT, default=None, comment="Remark")
    datas: Mapped[list["DictData"]] = relationship(init=False, back_populates="type")  # noqa: F821

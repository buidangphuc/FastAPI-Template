from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.common.model import Base, id_key


class DictData(Base):
    """Data dictionary"""

    __tablename__ = "sys_dict_data"

    id: Mapped[id_key] = mapped_column(init=False)
    label: Mapped[str] = mapped_column(
        String(32), unique=True, comment="Dictionary label"
    )
    value: Mapped[str] = mapped_column(
        String(32), unique=True, comment="Dictionary value"
    )
    sort: Mapped[int] = mapped_column(default=0, comment="Sort")
    status: Mapped[int] = mapped_column(
        default=1, comment="Status"
    )  # 0: Disable, 1: Enable
    remark: Mapped[str | None] = mapped_column(LONGTEXT, default=None, comment="Remark")
    type_id: Mapped[int] = mapped_column(
        ForeignKey("sys_dict_type.id"), default=0, comment="Dictionary type ID"
    )
    type: Mapped["DictType"] = relationship(init=False, back_populates="datas")  # noqa: F821

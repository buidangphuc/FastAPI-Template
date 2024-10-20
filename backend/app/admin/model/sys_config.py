from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class Config(Base):
    """System configuration"""

    __tablename__ = "sys_config"

    id: Mapped[id_key] = mapped_column(init=False)
    login_title: Mapped[str] = mapped_column(String(20), comment="Login page title")
    login_sub_title: Mapped[str] = mapped_column(
        String(50), comment="Login page subtitle"
    )
    footer: Mapped[str] = mapped_column(String(50), comment="Footer")
    logo: Mapped[str] = mapped_column(LONGTEXT, comment="Logo")
    system_title: Mapped[str] = mapped_column(String(20), comment="System title")
    system_comment: Mapped[str] = mapped_column(
        LONGTEXT,
        comment="System description",
    )

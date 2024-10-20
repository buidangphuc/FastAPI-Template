from sqlalchemy import String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import MappedBase, id_key


class CasbinRule(MappedBase):
    """Rewrite the CasbinRule model class in casbin and use a custom Base to avoid alembic migration problems"""

    __tablename__ = "sys_casbin_rule"

    id: Mapped[id_key]
    ptype: Mapped[str] = mapped_column(String(255), comment="Policy type")
    v0: Mapped[str] = mapped_column(String(255), comment="User uuid/ Role ID")
    v1: Mapped[str] = mapped_column(LONGTEXT, comment="API path/ Role name")
    v2: Mapped[str | None] = mapped_column(String(255), comment="Request method")
    v3: Mapped[str | None] = mapped_column(String(255))
    v4: Mapped[str | None] = mapped_column(String(255))
    v5: Mapped[str | None] = mapped_column(String(255))

    def __str__(self):
        arr = [self.ptype]
        for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
            if v is None:
                break
            arr.append(v)
        return ", ".join(arr)

    def __repr__(self):
        return '<CasbinRule {}: "{}">'.format(self.id, str(self))

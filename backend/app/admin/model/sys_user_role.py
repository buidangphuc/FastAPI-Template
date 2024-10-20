from sqlalchemy import INT, Column, ForeignKey, Integer, Table

from backend.common.model import MappedBase

sys_user_role = Table(
    "sys_user_role",
    MappedBase.metadata,
    Column(
        "id",
        INT,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True,
        comment="ID",
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("sys_user.id", ondelete="CASCADE"),
        primary_key=True,
        comment="User ID",
    ),
    Column(
        "role_id",
        Integer,
        ForeignKey("sys_role.id", ondelete="CASCADE"),
        primary_key=True,
        comment="Role ID",
    ),
)

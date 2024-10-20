from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    declared_attr,
    mapped_column,
)

from backend.utils.timezone import timezone

# Common Mapped type primary key, needs to be manually added, refer to the usage below
# MappedBase -> id: Mapped[id_key]
# DataClassBase && Base -> id: Mapped[id_key] = mapped_column(init=False)
id_key = Annotated[
    int,
    mapped_column(
        init=False,  # Automatically generated primary key
        primary_key=True,
        index=True,
        autoincrement=True,
        sort_order=-999,
        comment="Primary key id",
    ),
]


# Mixin: A concept in object-oriented programming that makes the structure clearer, `Wiki <https://en.wikipedia.org/wiki/Mixin/>`__
class UserMixin(MappedAsDataclass):
    """User Mixin data class."""

    create_user: Mapped[int] = mapped_column(sort_order=998, comment="Creator")
    update_user: Mapped[int | None] = mapped_column(
        init=False, default=None, sort_order=998, comment="Modifier"
    )


class DateTimeMixin(MappedAsDataclass):
    """Date and time Mixin data class."""

    created_time: Mapped[datetime] = mapped_column(
        init=False,
        default_factory=timezone.now,
        sort_order=999,
        comment="Creation time",
    )
    updated_time: Mapped[datetime | None] = mapped_column(
        init=False, onupdate=timezone.now, sort_order=999, comment="Update time"
    )


class MappedBase(DeclarativeBase):
    """
    Declarative base class, the original DeclarativeBase class, serves as the parent class for all base classes or data model classes.

    `DeclarativeBase <https://docs.sqlalchemy.org/en/20/orm/declarative_config.html>`__
    `mapped_column() <https://docs.sqlalchemy.org/en/20/orm/mapping_api.html#sqlalchemy.orm.mapped_column>`__
    """  # noqa: E501

    @declared_attr.directive
    def __tablename__(self) -> str:
        return self.__name__.lower()


class DataClassBase(MappedAsDataclass, MappedBase):
    """
    Declarative data class base class, it integrates with data classes, allowing for more advanced configurations, but you need to be aware of some of its features, especially when used with DeclarativeBase.

    `MappedAsDataclass <https://docs.sqlalchemy.org/en/20/orm/dataclasses.html#orm-declarative-native-dataclasses>`__
    """  # noqa: E501

    __abstract__ = True


class Base(DataClassBase, DateTimeMixin):
    """Declarative Mixin data class base class, with data class integration, and includes the MiXin data class basic table structure, you can simply understand it as a data class base class with basic table structure."""  # noqa: E501

    __abstract__ = True

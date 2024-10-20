from enum import Enum
from enum import IntEnum as SourceIntEnum
from typing import Type

class _EnumBase:
    @classmethod
    def get_member_keys(cls: Type[Enum]) -> list[str]:
        """Retrieve the keys (names) of enum members."""
        return [name for name in cls.__members__.keys()]

    @classmethod
    def get_member_values(cls: Type[Enum]) -> list:
        """Retrieve the values of enum members."""
        return [item.value for item in cls.__members__.values()]

class IntEnum(_EnumBase, SourceIntEnum):
    """Integer-based enum."""
    pass

class StrEnum(_EnumBase, str, Enum):
    """String-based enum."""
    pass

class MenuType(IntEnum):
    """Types of menu components."""
    directory = 0
    menu = 1
    button = 2

class RoleDataScopeType(IntEnum):
    """Scope of role data access."""
    all = 1
    custom = 2

class MethodType(StrEnum):
    """HTTP request methods."""
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    OPTIONS = 'OPTIONS'

class LoginLogStatusType(IntEnum):
    """Status of login logs."""
    fail = 0
    success = 1

class BuildTreeType(StrEnum):
    """Types of tree-building algorithms."""
    traversal = 'traversal'
    recursive = 'recursive'

class OperaLogCipherType(IntEnum):
    """Encryption types for operation logs."""
    aes = 0
    md5 = 1
    itsdangerous = 2
    plan = 3

class StatusType(IntEnum):
    """General status types."""
    disable = 0
    enable = 1

class UserSocialType(StrEnum):
    """Types of user social platforms."""
    github = 'GitHub'
    linuxdo = 'LinuxDo'

class GenModelMySQLColumnType(StrEnum):
    """MySQL column types for code generation models."""
    
    # Python type mappings
    BIGINT = 'int'
    BigInteger = 'int'
    BINARY = 'bytes'
    BLOB = 'bytes'
    BOOLEAN = 'bool'
    CHAR = 'str'
    DATE = 'date'
    DATETIME = 'datetime'
    DECIMAL = 'Decimal'
    DOUBLE = 'float'
    FLOAT = 'float'
    INT = 'int'
    JSON = 'dict'
    TEXT = 'str'
    TIME = 'time'
    UUID = 'str | UUID'
    VARCHAR = 'str'
    
    # MySQL-specific types
    BIT = 'bool'
    ENUM = 'Enum'
    LONGBLOB = 'bytes'
    LONGTEXT = 'str'
    TINYINT = 'int'
    YEAR = 'int'

class GenModelPostgreSQLColumnType(StrEnum):
    """PostgreSQL column types for code generation models."""
    
    # Python type mappings
    BIGINT = 'int'
    BOOLEAN = 'bool'
    CHAR = 'str'
    DATE = 'date'
    DATETIME = 'datetime'
    DECIMAL = 'Decimal'
    DOUBLE = 'float'
    FLOAT = 'float'
    INT = 'int'
    JSONB = 'dict'
    TEXT = 'str'
    TIME = 'time'
    UUID = 'str | UUID'
    
    # PostgreSQL-specific types
    ARRAY = 'list'
    BYTEA = 'bytes'
    CIDR = 'str'
    DATERANGE = 'tuple[date, date]'
    ENUM = 'Enum'
    HSTORE = 'dict'
    INET = 'str'
    MONEY = 'Decimal'
    NUMRANGE = 'tuple[Decimal, Decimal]'
    TSRANGE = 'tuple[datetime, datetime]'

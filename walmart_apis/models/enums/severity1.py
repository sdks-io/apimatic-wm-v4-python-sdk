from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Severity1(str, Enum):
    """Severity level of the error."""

    EMERG = "EMERG"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARN = "WARN"

    __str__ = str.__str__


Severity1OrStr: TypeAlias = Annotated[Severity1 | str, open_enum_validator(Severity1)]

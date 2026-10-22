from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProcessMode2(str, Enum):
    UPSERT = "UPSERT"
    DELETE = "DELETE"

    __str__ = str.__str__


ProcessMode2OrStr: TypeAlias = Annotated[ProcessMode2 | str, open_enum_validator(ProcessMode2)]

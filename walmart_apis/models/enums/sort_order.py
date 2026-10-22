from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortOrder(str, Enum):
    ACS = "ACS"
    DESC = "DESC"

    __str__ = str.__str__


SortOrderOrStr: TypeAlias = Annotated[SortOrder | str, open_enum_validator(SortOrder)]

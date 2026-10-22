from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type4(str, Enum):
    """The type of filter to apply.

    <strong style="color: green;">Market availability: Global</strong>"""

    RANGE_FILTER = "rangeFilter"
    ENUM_FILTER = "enumFilter"
    MULTI_VALUE_FILTER = "multiValueFilter"

    __str__ = str.__str__


Type4OrStr: TypeAlias = Annotated[Type4 | str, open_enum_validator(Type4)]

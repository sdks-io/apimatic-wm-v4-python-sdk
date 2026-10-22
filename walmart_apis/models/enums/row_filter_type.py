from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RowFilterType(str, Enum):
    """The type of filter to apply.

    <strong style="color: green;">Market availability: Global</strong>"""

    RANGE_FILTER = "rangeFilter"
    ENUM_FILTER = "enumFilter"
    MULTI_VALUE_FILTER = "multiValueFilter"

    __str__ = str.__str__


RowFilterTypeOrStr: TypeAlias = Annotated[RowFilterType | str, open_enum_validator(RowFilterType)]

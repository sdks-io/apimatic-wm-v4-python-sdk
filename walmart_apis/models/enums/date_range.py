from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DateRange(str, Enum):
    """Date range to filter impressions, page views, and sales."""

    _7_DAYS = "7DAYS"
    _14_DAYS = "14DAYS"
    _30_DAYS = "30DAYS"

    __str__ = str.__str__


DateRangeOrStr: TypeAlias = Annotated[DateRange | str, open_enum_validator(DateRange)]

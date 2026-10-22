from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DateRange4(str, Enum):
    """Date range to filter impressions, page views, and sales.<br><b style='color:green;'>Market availability: US
    only</b>"""

    _7_DAYS = "7DAYS"
    _14_DAYS = "14DAYS"
    _30_DAYS = "30DAYS"

    __str__ = str.__str__


DateRange4OrStr: TypeAlias = Annotated[DateRange4 | str, open_enum_validator(DateRange4)]

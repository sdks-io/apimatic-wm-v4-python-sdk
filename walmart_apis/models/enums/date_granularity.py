from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DateGranularity(str, Enum):
    """Specifies the date granularity for aggregating report data. Required when using ``reportType=ITEM_PERFORMANCE``
    and ``reportVersion=v3``. Valid values are ``DAILY``, ``WEEKLY``, ``MONTHLY``, or ``QUARTERLY``. Ignored for all
    other report types and versions.

    <strong style="color: green;">Market availability: Global</strong>"""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"

    __str__ = str.__str__


DateGranularityOrStr: TypeAlias = Annotated[DateGranularity | str, open_enum_validator(DateGranularity)]

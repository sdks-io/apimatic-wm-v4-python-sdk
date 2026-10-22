from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskLevel(str, Enum):
    """Risk level as per Walmart standards"""

    MEETS_STANDARD = "Meets standard"
    MONITOR = "Monitor"
    URGENT = "Urgent"

    __str__ = str.__str__


RiskLevelOrStr: TypeAlias = Annotated[RiskLevel | str, open_enum_validator(RiskLevel)]

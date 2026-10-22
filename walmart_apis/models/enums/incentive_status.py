from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncentiveStatus(str, Enum):
    ELIGIBLE = "ELIGIBLE"
    ENROLLED = "ENROLLED"

    __str__ = str.__str__


IncentiveStatusOrStr: TypeAlias = Annotated[IncentiveStatus | str, open_enum_validator(IncentiveStatus)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncentiveType(str, Enum):
    REDUCED_REFERRAL = "REDUCED_REFERRAL"
    WALMART_FUNDED = "WALMART_FUNDED"

    __str__ = str.__str__


IncentiveTypeOrStr: TypeAlias = Annotated[IncentiveType | str, open_enum_validator(IncentiveType)]

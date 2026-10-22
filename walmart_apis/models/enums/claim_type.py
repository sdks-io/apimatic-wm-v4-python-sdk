from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ClaimType(str, Enum):
    """Claim category: LIT (lost in transit), LAD (lost after delivery), or DAMAGED."""

    LIT = "LIT"
    LAD = "LAD"
    DAMAGED = "DAMAGED"

    __str__ = str.__str__


ClaimTypeOrStr: TypeAlias = Annotated[ClaimType | str, open_enum_validator(ClaimType)]

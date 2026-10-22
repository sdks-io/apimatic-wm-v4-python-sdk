from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType(str, Enum):
    """Allowed Values"""

    FITMENT_ACES = "FITMENT_ACES"
    FITMENT_PIES = "FITMENT_PIES"

    __str__ = str.__str__


FeedTypeOrStr: TypeAlias = Annotated[FeedType | str, open_enum_validator(FeedType)]

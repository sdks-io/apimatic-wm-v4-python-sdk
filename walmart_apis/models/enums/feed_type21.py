from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType21(str, Enum):
    PRICE_AND_PROMOTION = "PRICE_AND_PROMOTION"

    __str__ = str.__str__


FeedType21OrStr: TypeAlias = Annotated[FeedType21 | str, open_enum_validator(FeedType21)]

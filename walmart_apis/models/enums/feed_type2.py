from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType2(str, Enum):
    WALMART_FUNDED_INCENTIVES_ENROLLMENT = "WALMART_FUNDED_INCENTIVES_ENROLLMENT"

    __str__ = str.__str__


FeedType2OrStr: TypeAlias = Annotated[FeedType2 | str, open_enum_validator(FeedType2)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType11(str, Enum):
    INCENTIVE_ENROLLMENT = "INCENTIVE_ENROLLMENT"

    __str__ = str.__str__


FeedType11OrStr: TypeAlias = Annotated[FeedType11 | str, open_enum_validator(FeedType11)]

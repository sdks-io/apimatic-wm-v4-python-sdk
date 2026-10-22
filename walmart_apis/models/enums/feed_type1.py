from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeedType1(str, Enum):
    INVENTORY = "inventory"
    MP_INVENTORY = "MP_INVENTORY"

    __str__ = str.__str__


FeedType1OrStr: TypeAlias = Annotated[FeedType1 | str, open_enum_validator(FeedType1)]

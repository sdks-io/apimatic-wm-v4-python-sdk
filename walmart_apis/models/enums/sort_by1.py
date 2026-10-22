from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortBy1(str, Enum):
    ITEM_ID = "ITEM_ID"
    PRODUCT_NAME = "PRODUCT_NAME"
    CURRENT_PRICE = "CURRENT_PRICE"
    EXPIRATION_DATE = "EXPIRATION_DATE"
    ENROLLMENT_DATE = "ENROLLMENT_DATE"

    __str__ = str.__str__


SortBy1OrStr: TypeAlias = Annotated[SortBy1 | str, open_enum_validator(SortBy1)]

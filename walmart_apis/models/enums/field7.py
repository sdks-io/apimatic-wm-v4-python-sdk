from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field7(str, Enum):
    SKU = "sku"
    ITEM_ID = "itemId"
    PRODUCT_NAME = "productName"

    __str__ = str.__str__


Field7OrStr: TypeAlias = Annotated[Field7 | str, open_enum_validator(Field7)]

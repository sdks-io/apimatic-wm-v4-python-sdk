from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field12(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_PRIORITY | Recommended priority of the item by Walmart. | integer |
    | PRICE | Item price | integer |"""

    ITEM_PRIORITY = "ITEM_PRIORITY"
    PRICE = "PRICE"

    __str__ = str.__str__


Field12OrStr: TypeAlias = Annotated[Field12 | str, open_enum_validator(Field12)]

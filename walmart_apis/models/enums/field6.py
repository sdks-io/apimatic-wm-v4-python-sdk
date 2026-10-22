from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field6(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_NAME | Product name | string |
    | SKU | Specifies the item identified. This value is defined by the seller. | string |"""

    ITEM_NAME = "ITEM_NAME"
    SKU = "SKU"

    __str__ = str.__str__


Field6OrStr: TypeAlias = Annotated[Field6 | str, open_enum_validator(Field6)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field42(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_NAME | Product name | string |
    | SKU | Specifies the item identified. This value is defined by the seller. | string |
    <br><b style='color:green;'>Market availability: US only</b>"""

    ITEM_NAME = "ITEM_NAME"
    SKU = "SKU"

    __str__ = str.__str__


Field42OrStr: TypeAlias = Annotated[Field42 | str, open_enum_validator(Field42)]

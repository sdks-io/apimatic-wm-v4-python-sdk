from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Field51(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ITEM_PRIORITY | Recommended priority of the item by Walmart. | integer |
    | PRICE | Item price | integer |
    <br><b style='color:green;'>Market availability: US only</b>"""

    ITEM_PRIORITY = "ITEM_PRIORITY"
    PRICE = "PRICE"

    __str__ = str.__str__


Field51OrStr: TypeAlias = Annotated[Field51 | str, open_enum_validator(Field51)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemAvailabilityStatus4(str, Enum):
    """Item availability status of the recommended item. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | EXISTING_IN_WALMART | Indicates that item is existing in Walmart. | string |
    | NEW_TO_WALMART | Indicates that item is new to Walmart. | string |"""

    EXISTING_IN_WALMART = "EXISTING_IN_WALMART"
    NEW_TO_WALMART = "NEW_TO_WALMART"

    __str__ = str.__str__


ItemAvailabilityStatus4OrStr: TypeAlias = Annotated[
    ItemAvailabilityStatus4 | str, open_enum_validator(ItemAvailabilityStatus4)
]

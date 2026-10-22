from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemAvailabilityStatus(str, Enum):
    """Item availability status of the recommended item.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | EXISTING_IN_WALMART | Indicates that item is existing in Walmart. | string |
    | NEW_TO_WALMART | Indicates that item is new to Walmart. | string |"""

    EXISTING_IN_WALMART = "EXISTING_IN_WALMART"
    NEW_TO_WALMART = "NEW_TO_WALMART"

    __str__ = str.__str__


ItemAvailabilityStatusOrStr: TypeAlias = Annotated[
    ItemAvailabilityStatus | str, open_enum_validator(ItemAvailabilityStatus)
]

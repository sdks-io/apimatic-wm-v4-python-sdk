from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemStatus3(str, Enum):
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | ELIGIBLE | To get items which are eligible for the program | string |
    | ENROLLED | To get items which are currently enrolled into the program | string |
    | COMPLETE | To get items which have attained target reviews through the program | string |"""

    ELIGIBLE = "ELIGIBLE"
    ENROLLED = "ENROLLED"
    COMPLETE = "COMPLETE"

    __str__ = str.__str__


ItemStatus3OrStr: TypeAlias = Annotated[ItemStatus3 | str, open_enum_validator(ItemStatus3)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FieldModel(str, Enum):
    """Attribute on which sorting needs to be performed.

    **Supported Values**: clicks, gmv, orders **Default**: gmv"""

    CLICKS = "clicks"
    GMV = "gmv"
    ORDERS = "orders"

    __str__ = str.__str__


FieldModelOrStr: TypeAlias = Annotated[FieldModel | str, open_enum_validator(FieldModel)]

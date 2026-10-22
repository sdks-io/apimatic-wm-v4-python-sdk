from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter2(str, Enum):
    """To apply a range filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | PRICE | To filter based on the price. | string |"""

    PRICE = "PRICE"

    __str__ = str.__str__


Parameter2OrStr: TypeAlias = Annotated[Parameter2 | str, open_enum_validator(Parameter2)]

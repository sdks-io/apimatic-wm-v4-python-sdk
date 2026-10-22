from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Parameter21(str, Enum):
    """To apply a range filter based on the predefined parameter. <br><b style='color:green;'>Market availability: US |
    CA | MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | PRICE | To filter based on the price. | string |"""

    PRICE = "PRICE"

    __str__ = str.__str__


Parameter21OrStr: TypeAlias = Annotated[Parameter21 | str, open_enum_validator(Parameter21)]

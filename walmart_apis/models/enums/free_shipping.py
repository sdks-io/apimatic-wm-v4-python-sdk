from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FreeShipping(str, Enum):
    """Indicates if the shipping is free for a recommended item which is a buy box winner. <br><b
    style='color:green;'>Market availability: US | CA | MX</span></b>"""

    YES = "YES"
    NO = "NO"

    __str__ = str.__str__


FreeShippingOrStr: TypeAlias = Annotated[FreeShipping | str, open_enum_validator(FreeShipping)]

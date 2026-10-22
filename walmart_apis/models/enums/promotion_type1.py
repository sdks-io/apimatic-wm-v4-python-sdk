from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PromotionType1(str, Enum):
    """| Market | Translation |
    | --- | ----------- |
    | US | ["Clearance", "Reduced"]|

    <br><b style='color:green;'>Market availability: US</b>"""

    CLEARANCE = "Clearance"
    REDUCED = "Reduced"

    __str__ = str.__str__


PromotionType1OrStr: TypeAlias = Annotated[PromotionType1 | str, open_enum_validator(PromotionType1)]

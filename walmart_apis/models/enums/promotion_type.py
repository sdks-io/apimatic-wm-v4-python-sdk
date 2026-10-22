from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PromotionType(str, Enum):
    """| Market | Translation |
    | --- | ----------- |
    | CA | ["Clearance", "Reduced"]|
    | MX | ["Rebaja", "Liquidación"]|

    <br><b style='color:green;'>Market availability: US | CA | MX </b>"""

    CLEARANCE = "Clearance"
    REDUCED = "Reduced"
    REBAJA = "Rebaja"
    LIQUIDACI_N = "Liquidación"

    __str__ = str.__str__


PromotionTypeOrStr: TypeAlias = Annotated[PromotionType | str, open_enum_validator(PromotionType)]

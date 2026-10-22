from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdjustmentType(str, Enum):
    """Specifies how price adjustment is applied. UNIT for a fixed amount or PERCENTAGE for a percentage-based
    change.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    UNIT = "UNIT"
    PERCENTAGE = "PERCENTAGE"

    __str__ = str.__str__


AdjustmentTypeOrStr: TypeAlias = Annotated[AdjustmentType | str, open_enum_validator(AdjustmentType)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AdjustmentType2(str, Enum):
    """Specifies how price adjustment is applied. UNIT for a fixed amount or PERCENTAGE for a percentage-based
    change.<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    UNIT = "UNIT"
    PERCENTAGE = "PERCENTAGE"

    __str__ = str.__str__


AdjustmentType2OrStr: TypeAlias = Annotated[AdjustmentType2 | str, open_enum_validator(AdjustmentType2)]

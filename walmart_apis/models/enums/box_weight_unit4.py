from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxWeightUnit4(str, Enum):
    """Box Weight Unit [LB, KG]. <br/><b>Applicable to SWW and WPS.</span></b>"""

    LB = "LB"
    KG = "KG"

    __str__ = str.__str__


BoxWeightUnit4OrStr: TypeAlias = Annotated[BoxWeightUnit4 | str, open_enum_validator(BoxWeightUnit4)]

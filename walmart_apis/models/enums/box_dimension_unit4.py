from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BoxDimensionUnit4(str, Enum):
    """Box Dimension Unit [CM, IN]. Mandatory for CUSTOM_PACKAGE type, otherwise not required. <br/><b>Applicable to SWW
    and WPS.</span></b>"""

    CM = "CM"
    IN = "IN"

    __str__ = str.__str__


BoxDimensionUnit4OrStr: TypeAlias = Annotated[BoxDimensionUnit4 | str, open_enum_validator(BoxDimensionUnit4)]

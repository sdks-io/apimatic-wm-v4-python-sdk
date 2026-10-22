from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RebateType3(str, Enum):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    AMOUNT = "AMOUNT"
    PRODUCT = "PRODUCT"

    __str__ = str.__str__


RebateType3OrStr: TypeAlias = Annotated[RebateType3 | str, open_enum_validator(RebateType3)]

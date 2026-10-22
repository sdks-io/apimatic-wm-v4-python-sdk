from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SalesInsights2(str, Enum):
    """Tags that indicate why an item is in demand, helping sellers quickly assess customer interest and competitive
    trends. <br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    BEST_SELLER = "BEST_SELLER"
    TRENDING = "TRENDING"
    FIRST_MOVER = "FIRST_MOVER"
    HIGHLY_SEARCHED = "HIGHLY_SEARCHED"

    __str__ = str.__str__


SalesInsights2OrStr: TypeAlias = Annotated[SalesInsights2 | str, open_enum_validator(SalesInsights2)]

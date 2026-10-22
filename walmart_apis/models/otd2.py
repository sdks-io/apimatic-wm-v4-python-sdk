from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Otd2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    defected_order: Optional[int] = Field(default=UNSET, alias="defectedOrder")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_order: Optional[int] = Field(default=UNSET, alias="totalOrder")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    rate: Optional[int] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Otd2Dict(TypedDict):
    defected_order: NotRequired[int]
    total_order: NotRequired[int]
    rate: NotRequired[int]

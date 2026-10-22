from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter21 import Parameter21OrStr


class RangeFilter4(SdkBaseModel):
    """Filter based on a range with RangeFilter. You must also pass a parameter along with any of the beginning or the
    ending points or both. No parameter should be repeated. <br><b style='color:green;'>Market availability: US | CA |
    MX</span></b>"""

    parameter: Optional[Parameter21OrStr] = UNSET
    """To apply a range filter based on the predefined parameter. <br><b style='color:green;'>Market availability: US |
    CA | MX</span></b>

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | PRICE | To filter based on the price. | string |"""

    from_: Optional[str] = Field(default=UNSET, alias="from")
    """Filter range start <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    to: Optional[str] = UNSET
    """Filter range end <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""


class RangeFilter4Dict(TypedDict):
    parameter: NotRequired[Parameter21OrStr]
    from_: NotRequired[str]
    to: NotRequired[str]

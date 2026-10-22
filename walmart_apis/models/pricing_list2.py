from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pricing1 import Pricing1, Pricing1Dict


class PricingList2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    replace_all: Optional[bool] = Field(default=UNSET, alias="replaceAll")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    pricing: list[Pricing1]
    """<br><b style='color:green;'>Market availability: Global</b>"""


class PricingList2Dict(TypedDict):
    replace_all: NotRequired[bool]
    pricing: list[Pricing1Dict]

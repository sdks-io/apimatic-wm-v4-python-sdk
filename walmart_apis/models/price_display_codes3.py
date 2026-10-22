from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceDisplayCodes3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_clearance: Optional[bool] = Field(default=UNSET, alias="isClearance")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    hide_price_for_soi: Optional[Any] = Field(default=UNSET, alias="hidePriceForSOI")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    submap_type: Optional[Any] = Field(default=UNSET, alias="submapType")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_rollback: Optional[bool] = Field(default=UNSET, alias="isRollback")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_reduced_price: Optional[bool] = Field(default=UNSET, alias="isReducedPrice")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_eligible_for_associate_discount: Optional[Any] = Field(default=UNSET, alias="isEligibleForAssociateDiscount")
    """<br><b style='color:green;'>Market availability: Global</b>"""

    is_strikethrough: Optional[bool] = Field(default=UNSET, alias="isStrikethrough")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class PriceDisplayCodes3Dict(TypedDict):
    is_clearance: NotRequired[bool]
    hide_price_for_soi: NotRequired[Any]
    submap_type: NotRequired[Any]
    is_rollback: NotRequired[bool]
    is_reduced_price: NotRequired[bool]
    is_eligible_for_associate_discount: NotRequired[Any]
    is_strikethrough: NotRequired[bool]

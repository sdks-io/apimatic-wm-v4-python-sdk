from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Gmv(SdkBaseModel):
    """chargeAmount.<br><b style='color:green;'>Market availability: MX | CA |CL</b>, Refund amount details for the
    return order line.<br><b style='color:green;'>Market availability: MX | CA | CL</b>, refundAmount.<br><b
    style='color:green;'>Market availability: MX</b>, taxName.<br><b style='color:green;'>Market availability: MX</b>,
    unitPrice.<br><b style='color:green;'>Market availability: MX</b>"""

    amount: Optional[str] = UNSET
    currency: Optional[str] = UNSET


class GmvDict(TypedDict):
    amount: NotRequired[str]
    currency: NotRequired[str]

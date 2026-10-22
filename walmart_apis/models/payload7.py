from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Payload7(SdkBaseModel):
    """Payload in the response for rejecting recommendations."""

    message: Optional[str] = UNSET
    """Message confirming the rejection of the recommendations.
     Message discription for US will be like 'The selected items will be removed shortly from the recommendations.' and
        for CA and MX : 'Recommendation Removed successfully. No of recommendation removed:5' <br><b
        style='color:green;'>Market availability: US | CA | MX</span></b>"""


class Payload7Dict(TypedDict):
    message: NotRequired[str]

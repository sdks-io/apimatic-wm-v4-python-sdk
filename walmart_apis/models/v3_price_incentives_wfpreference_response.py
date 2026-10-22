from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3PriceIncentivesWfpreferenceResponse(SdkBaseModel):
    auto_enroll_enabled: Optional[bool] = Field(default=UNSET, alias="autoEnrollEnabled")
    """Status of autoEnrollEnabled true or false.<br><b style='color:green;'>Market availability: US</b>"""

    is_disabled: Optional[bool] = Field(default=UNSET, alias="isDisabled")
    """Status of isDisabled true or false.<br><b style='color:green;'>Market availability: US</b>"""


class V3PriceIncentivesWfpreferenceResponseDict(TypedDict):
    auto_enroll_enabled: NotRequired[bool]
    is_disabled: NotRequired[bool]

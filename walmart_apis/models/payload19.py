from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Payload19(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    unpublished_count: Optional[str] = Field(default=UNSET, alias="unpublishedCount")
    """Specifies the total count of unpublished items.<br><b style='color:green;'>Market availability: US | CA |
    MX</b>"""

    unpublished_value: Optional[str] = Field(default=UNSET, alias="unpublishedValue")
    """Specifies the total value of unpublished items.<br><b style='color:green;'>Market availability: US | CA |
    MX</b>"""

    unpublished_reason_code: Optional[str] = Field(default=UNSET, alias="unpublishedReasonCode")
    """The reason why item is unpublished.<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Payload19Dict(TypedDict):
    unpublished_count: NotRequired[str]
    unpublished_value: NotRequired[str]
    unpublished_reason_code: NotRequired[str]

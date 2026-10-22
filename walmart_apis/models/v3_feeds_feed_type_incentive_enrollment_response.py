from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class V3FeedsFeedTypeIncentiveEnrollmentResponse(SdkBaseModel):
    feed_id: Optional[str] = Field(default=UNSET, alias="feedId")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    message: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""

    additional_attributes: OptionalNullable[Any] = Field(default=UNSET, alias="additionalAttributes")
    """<br><b style='color:green;'>Market availability: US only</b>"""

    errors: OptionalNullable[Any] = UNSET
    """<br><b style='color:green;'>Market availability: US only</b>"""


class V3FeedsFeedTypeIncentiveEnrollmentResponseDict(TypedDict):
    feed_id: NotRequired[str]
    message: NotRequired[str]
    additional_attributes: NotRequired[Any | None]
    errors: NotRequired[Any | None]

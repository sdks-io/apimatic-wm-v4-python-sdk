from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Payload2(SdkBaseModel):
    unpublished_count: Optional[str] = Field(default=UNSET, alias="unpublishedCount")
    """total count for unpublished Item"""

    unpublished_value: Optional[str] = Field(default=UNSET, alias="unpublishedValue")
    """total value for unpublished Item"""

    unpublished_reason_code: Optional[str] = Field(default=UNSET, alias="unpublishedReasonCode")
    """the reason why item is unpublished"""


class Payload2Dict(TypedDict):
    unpublished_count: NotRequired[str]
    unpublished_value: NotRequired[str]
    unpublished_reason_code: NotRequired[str]

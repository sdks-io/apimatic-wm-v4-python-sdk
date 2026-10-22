from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Data9(SdkBaseModel):
    """Response payload for the operation."""

    manifest_id: Optional[str] = Field(default=UNSET, alias="manifestId")
    """Manifest ID returned by the create scan form API. Use this value to download the scan form or for future
    reference."""

    status: Optional[str] = UNSET
    """Status of the scan form request. Example: SUCCESS."""


class Data9Dict(TypedDict):
    manifest_id: NotRequired[str]
    status: NotRequired[str]

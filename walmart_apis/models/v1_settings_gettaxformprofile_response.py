from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload10 import Payload10, Payload10Dict


class V1SettingsGettaxformprofileResponse(SdkBaseModel):
    """Envelope containing the partner identifier and available tax forms."""

    payload: Optional[Payload10] = UNSET
    status: Optional[str] = UNSET
    """Request outcome, for example OK."""


class V1SettingsGettaxformprofileResponseDict(TypedDict):
    payload: NotRequired[Payload10Dict]
    status: NotRequired[str]

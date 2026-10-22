from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .failure2 import Failure2, Failure2Dict
from .success2 import Success2, Success2Dict


class Payload32(SdkBaseModel):
    """Response payload."""

    success: Optional[Success2] = UNSET
    """Items succeeded.<br><b style='color:green;'>Market availability: US only</b>"""

    failure: Optional[Failure2] = UNSET
    """Items failed.<br><b style='color:green;'>Market availability: US only</b>"""


class Payload32Dict(TypedDict):
    success: NotRequired[Success2Dict]
    failure: NotRequired[Failure2Dict]

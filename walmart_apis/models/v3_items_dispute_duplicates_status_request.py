from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .issues1 import Issues1, Issues1Dict


class V3ItemsDisputeDuplicatesStatusRequest(SdkBaseModel):
    issues: list[Issues1]
    """Items status included in the response list.

    <strong style="color: green;">**Market availability: US only**</strong>"""


class V3ItemsDisputeDuplicatesStatusRequestDict(TypedDict):
    issues: list[Issues1Dict]

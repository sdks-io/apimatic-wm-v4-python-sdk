from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorIdentifiers(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    entry: Optional[list[str]] = UNSET


class ErrorIdentifiersDict(TypedDict):
    entry: NotRequired[list[str]]

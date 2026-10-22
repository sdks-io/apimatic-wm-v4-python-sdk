from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorIdentifiers1(SdkBaseModel):
    """error Identifiers.

    <b style="color: green;">Market availability: MX | CL | US</b>"""

    entry: Optional[list[Any]] = UNSET


class ErrorIdentifiers1Dict(TypedDict):
    entry: NotRequired[list[Any]]

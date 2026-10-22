from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorIdentifiers2(SdkBaseModel):
    """error Identifiers.

    <b style="color: green;">Market availability: CL only</b>"""

    entry: Optional[list[Any]] = UNSET


class ErrorIdentifiers2Dict(TypedDict):
    entry: NotRequired[list[Any]]

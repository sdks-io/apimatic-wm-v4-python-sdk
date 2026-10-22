from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorIdentifiers11(SdkBaseModel):
    """error Identifiers.

    <b style="color: green;">Market availability: US | CA | MX</b>"""

    entry: Optional[list[Any]] = UNSET


class ErrorIdentifiers11Dict(TypedDict):
    entry: NotRequired[list[Any]]

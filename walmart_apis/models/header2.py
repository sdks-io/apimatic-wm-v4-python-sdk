from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Header2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    header_attributes: Optional[Any] = Field(default=UNSET, alias="headerAttributes")


class Header2Dict(TypedDict):
    header_attributes: NotRequired[Any]

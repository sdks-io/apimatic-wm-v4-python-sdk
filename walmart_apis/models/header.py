from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Header(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    header_attributes: OptionalNullable[str] = Field(default=UNSET, alias="headerAttributes")


class HeaderDict(TypedDict):
    header_attributes: NotRequired[str | None]

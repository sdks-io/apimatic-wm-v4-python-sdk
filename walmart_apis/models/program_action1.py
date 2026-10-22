from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict
from .programs1 import Programs1, Programs1Dict


class ProgramAction1(SdkBaseModel):
    """items>"""

    item_identifiers: Optional[ItemIdentifiers] = Field(default=UNSET, alias="ItemIdentifiers")
    """<br><b style='color:green;'>Market availability: US</b>"""

    programs: Optional[Programs1] = Field(default=UNSET, alias="Programs")


class ProgramAction1Dict(TypedDict):
    item_identifiers: NotRequired[ItemIdentifiersDict]
    programs: NotRequired[Programs1Dict]

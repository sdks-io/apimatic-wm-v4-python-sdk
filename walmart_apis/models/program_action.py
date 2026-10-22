from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict
from .programs import Programs, ProgramsDict


class ProgramAction(SdkBaseModel):
    """This includes all the SKU IDs and the type of shipping configuration to migrate."""

    item_identifiers: Optional[ItemIdentifiers] = Field(default=UNSET, alias="ItemIdentifiers")
    """<br><b style='color:green;'>Market availability: US</b>"""

    programs: Optional[Programs] = Field(default=UNSET, alias="Programs")


class ProgramActionDict(TypedDict):
    item_identifiers: NotRequired[ItemIdentifiersDict]
    programs: NotRequired[ProgramsDict]

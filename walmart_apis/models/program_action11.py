from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict
from .programs21 import Programs21, Programs21Dict


class ProgramAction11(SdkBaseModel):
    """This includes all the SKU IDs and the type of shipping configuration to migrate."""

    programs: Optional[Programs21] = Field(default=UNSET, alias="Programs")
    """The type of shipping configuration to migrate. <br><b style='color:green;'>Market availability: US</span></b>"""

    item_identifiers: Optional[ItemIdentifiers] = Field(default=UNSET, alias="ItemIdentifiers")
    """Item Identifier which needs to be migrated. <br><b style='color:green;'>Market availability: US</span></b>"""


class ProgramAction11Dict(TypedDict):
    programs: NotRequired[Programs21Dict]
    item_identifiers: NotRequired[ItemIdentifiersDict]

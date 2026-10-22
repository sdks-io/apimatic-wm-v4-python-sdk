from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error4 import Error4, Error4Dict


class UpdateInventoriesResponseNodeDto(SdkBaseModel):
    ship_node: Optional[str] = Field(default=UNSET, alias="shipNode")
    """ShipNode Id of the ship node for which the inventory is requested"""

    status: Optional[str] = UNSET
    """Node Update status. Example: 'Success'"""

    errors: Optional[list[Error4]] = UNSET
    """Node Update Error description."""


class UpdateInventoriesResponseNodeDtoDict(TypedDict):
    ship_node: NotRequired[str]
    status: NotRequired[str]
    errors: NotRequired[list[Error4Dict]]

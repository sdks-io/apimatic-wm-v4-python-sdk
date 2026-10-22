from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item_ingestion_status1 import ItemIngestionStatus1, ItemIngestionStatus1Dict


class ItemDetails6(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    item_ingestion_status: list[ItemIngestionStatus1] = Field(alias="itemIngestionStatus")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""


class ItemDetails6Dict(TypedDict):
    item_ingestion_status: list[ItemIngestionStatus1Dict]

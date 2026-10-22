from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item_details6 import ItemDetails6, ItemDetails6Dict


class V3PriceResponse(SdkBaseModel):
    feed_status: str = Field(alias="feedStatus")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    feed_submission_date: int = Field(alias="feedSubmissionDate")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    items_received: int = Field(alias="itemsReceived")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    items_succeeded: int = Field(alias="itemsSucceeded")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    items_failed: int = Field(alias="itemsFailed")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    items_processing: int = Field(alias="itemsProcessing")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    item_details: ItemDetails6 = Field(alias="itemDetails")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""


class V3PriceResponseDict(TypedDict):
    feed_status: str
    feed_submission_date: int
    items_received: int
    items_succeeded: int
    items_failed: int
    items_processing: int
    item_details: ItemDetails6Dict

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ItemIngestionStatus1(SdkBaseModel):
    mart_id: int = Field(alias="martId")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    sku: str
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    ingestion_status: str = Field(alias="ingestionStatus")
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""


class ItemIngestionStatus1Dict(TypedDict):
    mart_id: int
    sku: str
    ingestion_status: str

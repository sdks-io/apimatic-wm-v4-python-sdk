from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .strategy5 import Strategy5, Strategy5Dict


class Item11(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    strategy: Optional[Strategy5] = Field(default=UNSET, alias="Strategy")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Item11Dict(TypedDict):
    strategy: NotRequired[Strategy5Dict]

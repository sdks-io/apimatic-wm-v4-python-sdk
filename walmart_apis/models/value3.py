from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Value3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score_type: Optional[str] = Field(default=UNSET, alias="scoreType")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score_value: Optional[int] = Field(default=UNSET, alias="scoreValue")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    impact: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Value3Dict(TypedDict):
    score_type: NotRequired[str]
    score_value: NotRequired[int]
    impact: NotRequired[str]

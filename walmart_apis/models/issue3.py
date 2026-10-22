from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Issue3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    date: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    publish_flag: Optional[bool] = Field(default=UNSET, alias="publishFlag")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    transactable_flag: Optional[bool] = Field(default=UNSET, alias="transactableFlag")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Issue3Dict(TypedDict):
    date: NotRequired[str]
    publish_flag: NotRequired[bool]
    transactable_flag: NotRequired[bool]

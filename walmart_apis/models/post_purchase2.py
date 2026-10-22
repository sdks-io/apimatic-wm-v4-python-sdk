from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cancellations5 import Cancellations5, Cancellations5Dict
from .otd2 import Otd2, Otd2Dict


class PostPurchase2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    cancellations: Optional[Cancellations5] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    returns: Optional[Any] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_count: Optional[str] = Field(default=UNSET, alias="issueCount")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    otd: Optional[Otd2] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class PostPurchase2Dict(TypedDict):
    cancellations: NotRequired[Cancellations5Dict]
    returns: NotRequired[Any]
    issue_count: NotRequired[str]
    otd: NotRequired[Otd2Dict]

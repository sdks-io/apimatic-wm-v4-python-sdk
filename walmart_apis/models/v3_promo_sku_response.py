from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error5 import Error5, Error5Dict
from .header2 import Header2, Header2Dict
from .payload14 import Payload14, Payload14Dict


class V3PromoSkuResponse(SdkBaseModel):
    payload: Optional[Payload14] = UNSET
    header: Optional[Header2] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    status: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""

    errors: Optional[list[Error5]] = UNSET
    """<br><b style='color:green;'>Market availability: Global</b>"""


class V3PromoSkuResponseDict(TypedDict):
    payload: NotRequired[Payload14Dict]
    header: NotRequired[Header2Dict]
    status: NotRequired[str]
    errors: NotRequired[list[Error5Dict]]

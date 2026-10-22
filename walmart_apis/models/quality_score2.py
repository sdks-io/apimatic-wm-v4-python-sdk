from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .value3 import Value3, Value3Dict


class QualityScore2(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    score: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    values: Optional[list[Value3]] = UNSET


class QualityScore2Dict(TypedDict):
    score: NotRequired[float]
    values: NotRequired[list[Value3Dict]]

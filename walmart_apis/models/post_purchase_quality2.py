from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostPurchaseQuality2(SdkBaseModel):
    """Post Purchase Quality<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    defect_ratio: Optional[int] = Field(default=UNSET, alias="defectRatio")
    """Defect Ratio<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    item_defect_cnt: Optional[int] = Field(default=UNSET, alias="itemDefectCnt")
    """Item Defect Count<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class PostPurchaseQuality2Dict(TypedDict):
    defect_ratio: NotRequired[int]
    item_defect_cnt: NotRequired[int]

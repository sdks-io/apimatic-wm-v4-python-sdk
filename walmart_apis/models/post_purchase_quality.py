from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostPurchaseQuality(SdkBaseModel):
    """Post Purchase Quality"""

    defect_ratio: Optional[int] = Field(default=UNSET, alias="defectRatio")
    """Defect Ratio"""

    item_defect_cnt: Optional[int] = Field(default=UNSET, alias="itemDefectCnt")
    """Item Defect Count"""


class PostPurchaseQualityDict(TypedDict):
    defect_ratio: NotRequired[int]
    item_defect_cnt: NotRequired[int]

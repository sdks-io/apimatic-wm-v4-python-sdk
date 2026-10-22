from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Record6(SdkBaseModel):
    """Information of item recommendations based on the categorizationType."""

    name: Optional[str] = UNSET
    """Name of the brand or category as per the categorizationType. <br><b style='color:green;'>Market availability: US
    | CA | MX</span></b>"""

    number_of_item_recommendations: Optional[int] = Field(default=UNSET, alias="numberOfItemRecommendations")
    """This attribute is deprecated. <br><b style='color:green;'>Market availability: US only</span></b>"""


class Record6Dict(TypedDict):
    name: NotRequired[str]
    number_of_item_recommendations: NotRequired[int]

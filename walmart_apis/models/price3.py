from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    total_issue: Optional[int] = Field(default=UNSET, alias="totalIssue")
    """<br><b style='color:green;'>Market availability: US</b>"""

    price: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    issue_title: Optional[str] = Field(default=UNSET, alias="issueTitle")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    competitor_price: Optional[float] = Field(default=UNSET, alias="competitorPrice")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    walmart_shipping: Optional[float] = Field(default=UNSET, alias="walmartShipping")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    competitor_shipping: Optional[float] = Field(default=UNSET, alias="competitorShipping")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    competitor_url: Optional[str] = Field(default=UNSET, alias="competitorUrl")
    """<br><b style='color:green;'>Market availability: US</b>"""

    score: Optional[float] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    additional_des: Optional[str] = Field(default=UNSET, alias="additionalDes")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    asin: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""


class Price3Dict(TypedDict):
    total_issue: NotRequired[int]
    price: NotRequired[float]
    issue_title: NotRequired[str]
    competitor_price: NotRequired[float]
    walmart_shipping: NotRequired[float]
    competitor_shipping: NotRequired[float]
    competitor_url: NotRequired[str]
    score: NotRequired[float]
    additional_des: NotRequired[str]
    asin: NotRequired[str]

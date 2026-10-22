from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.locale2 import Locale2, Locale2Dict


class ItemFeedHeader(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    process_mode: Optional[str] = Field(default=UNSET, alias="processMode")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    subset: Optional[str] = UNSET
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    mart: Optional[str] = UNSET
    """mart for different markets is WALMART_US(for US), WALMART_CA(for CA), WALMART_MEXICO(for mx).<br><b
    style='color:green;'>Market availability: US | CA | MX</b>"""

    selling_channel: Optional[str] = Field(default=UNSET, alias="sellingChannel")
    """<br><b style='color:green;'>Market availability: US | CA | MX</b>"""

    version: Optional[str] = UNSET
    """version for different markets is 1.1(for US), 1.01(for CA), 1.05(for MX).<br><b style='color:green;'>Market
    availability: US | CA | MX</b>"""

    locale: Optional[Locale2] = UNSET
    """Locale for different markets is: 'en' (for US), 'es' (for MX), ['en','fr'] (for CA).<br><b
    style='color:green;'>Market availability: US | CA | MX</b>"""

    sub_category: Optional[str] = Field(default=UNSET, alias="subCategory")
    """<br><b style='color:green;'>Market availability: MX</b>"""


class ItemFeedHeaderDict(TypedDict):
    process_mode: NotRequired[str]
    subset: NotRequired[str]
    mart: NotRequired[str]
    selling_channel: NotRequired[str]
    version: NotRequired[str]
    locale: NotRequired[Locale2Dict]
    sub_category: NotRequired[str]

from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_info_list import CarrierInfoList, CarrierInfoListDict


class Label(SdkBaseModel):
    label_image_url: Optional[str] = Field(default=UNSET, alias="labelImageURL")
    """Url to get the return label.<br><b style='color:green;'>Market availability: US</b>"""

    carrier_info_list: Optional[list[CarrierInfoList]] = Field(default=UNSET, alias="carrierInfoList")
    """Carrier information for the return.<br><b style='color:green;'>Market availability: US</b>"""


class LabelDict(TypedDict):
    label_image_url: NotRequired[str]
    carrier_info_list: NotRequired[list[CarrierInfoListDict]]

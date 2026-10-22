from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.categorization_type3 import CategorizationType3OrStr
from .meta11 import Meta11, Meta11Dict
from .record6 import Record6, Record6Dict


class Payload6(SdkBaseModel):
    """Payload in the response having the categorization details about the item recommendations."""

    categorization_type: Optional[CategorizationType3OrStr] = Field(default=UNSET, alias="categorizationType")
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To get list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To get list of categories which are associated with the assortment recommendations | string |

    <br><b style='color:green;'>Market availability: US | CA | MX</span></b>"""

    meta: Optional[Meta11] = UNSET
    """Meta information for the response."""

    records: Optional[list[Record6]] = UNSET
    """Information of item recommendations based on the categorizationType."""


class Payload6Dict(TypedDict):
    categorization_type: NotRequired[CategorizationType3OrStr]
    meta: NotRequired[Meta11Dict]
    records: NotRequired[list[Record6Dict]]

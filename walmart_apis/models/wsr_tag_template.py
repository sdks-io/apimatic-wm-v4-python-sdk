from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.page_type import PageTypeOrStr


class WsrTagTemplate(SdkBaseModel):
    """A tag template containing URL pattern with placeholders for affiliate tracking."""

    page_type: PageTypeOrStr = Field(alias="pageType")
    """The type of page this template is for (For example, ``ITEM``, ``BRANDSHOP``).

    <span style="color:green">**Market availability: Global**</span>"""

    template: str
    """The URL template with placeholders. Placeholders include ``{insertCampaignId}``, ``{insertAdGroupId}``,
    ``{insertCreativeId}``, ``{insertItemId}``, and ``{insertBrandshopId}`` which should be replaced with actual values
    when constructing the final referral URL.

    <span style="color:green">**Market availability: Global**</span>"""


class WsrTagTemplateDict(TypedDict):
    page_type: PageTypeOrStr
    template: str

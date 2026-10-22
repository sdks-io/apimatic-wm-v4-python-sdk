from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wsr_tag_template import WsrTagTemplate, WsrTagTemplateDict


class WsrTagTemplatesResponse(SdkBaseModel):
    """Response containing tag templates for different page types."""

    data: Optional[list[WsrTagTemplate]] = UNSET
    """List of tag templates for different page types.

    <span style="color:green">**Market availability: Global**</span>"""


class WsrTagTemplatesResponseDict(TypedDict):
    data: NotRequired[list[WsrTagTemplateDict]]

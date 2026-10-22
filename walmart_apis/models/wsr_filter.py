from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.field1 import Field1OrStr


class WsrFilter(SdkBaseModel):
    """Filter configuration to narrow down report results.

    **Validation**: Both field and values are required when a filter is provided."""

    field: Field1OrStr
    """Attribute on which filter needs to be applied.

    **Supported fields**:
    - ``campaignId``: Filter by campaign identifier(s)
    - ``adGroupId``: Filter by ad group identifier(s)
    - ``creativeId``: Filter by creative identifier(s)"""

    values: list[str]
    """List of attribute values to filter on. Multiple values act as an OR condition."""


class WsrFilterDict(TypedDict):
    field: Field1OrStr
    values: list[str]

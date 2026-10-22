from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter2 import Parameter2OrStr


class RangeFilterCriteria(SdkBaseModel):
    """Filter based on a range with RangeFilter. You must also pass a parameter along with any of the beginning or the
    ending points or both. No parameter should be repeated."""

    parameter: Optional[Parameter2OrStr] = UNSET
    """To apply a range filter based on the predefined parameter.

    | Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | PRICE | To filter based on the price. | string |"""

    from_: Optional[str] = Field(default=UNSET, alias="from")
    """Filter range start"""

    to: Optional[str] = UNSET
    """Filter range end"""


class RangeFilterCriteriaDict(TypedDict):
    parameter: NotRequired[Parameter2OrStr]
    from_: NotRequired[str]
    to: NotRequired[str]

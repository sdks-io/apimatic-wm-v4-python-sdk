from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter1 import Parameter1OrStr


class MultiValueFilter(SdkBaseModel):
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""

    parameter: Parameter1OrStr
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND | To filter based on list of brands which are associated with the assortment recommendations | string |
    | CATEGORY | To filter based on list of categories which are associated with the assortment recommendations | string
        |
    | PRODUCT_TYPE | To filter based on list of product types which are associated with the assortment recommendations |
        string |"""

    values: Optional[list[str]] = UNSET
    """A list of values corresponds to the parameter in the filter. The values in the list should not be null or blank.
    Maximum size of the list should be 7."""


class MultiValueFilterDict(TypedDict):
    parameter: Parameter1OrStr
    values: NotRequired[list[str]]

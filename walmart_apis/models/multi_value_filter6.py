from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter15 import Parameter15OrStr


class MultiValueFilter6(SdkBaseModel):
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""

    parameter: Parameter15OrStr
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND <br><b style='color:green;'>Market availability: US, CA, MX</span></b> | To filter based on list of brands
        which are associated with the assortment recommendations | string |
    | CATEGORY <br><b style='color:green;'>Market availability: US, CA, MX</span></b> | To filter based on list of
        categories which are associated with the assortment recommendations | string |
    | PRODUCT_TYPE <br><b style='color:green;'>Market availability: US only</span></b> | To filter based on list of
        product types which are associated with the assortment recommendations | string |"""

    values: Optional[list[str]] = UNSET
    """A list of values corresponds to the parameter in the filter. The values in the list should not be null or blank.
    Maximum size of the list should be 7."""


class MultiValueFilter6Dict(TypedDict):
    parameter: Parameter15OrStr
    values: NotRequired[list[str]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.parameter18 import Parameter18OrStr


class MultiValueFilter7(SdkBaseModel):
    """Filters based on multiple values associated with a specific parameter. No parameter should be repeated."""

    parameter: Parameter18OrStr
    """| Attribute | Description | Data Type |
    | --- | ----------- | ------- |
    | BRAND <br><b style='color:green;'>Market availability: US | CA | MX</span></b>| To filter based on list of brands
        which are associated with the assortment recommendations. This is allowed when the categorization type is
        CATEGORY | string |
    | CATEGORY <br><b style='color:green;'>Market availability: US | CA | MX</span></b> | To filter based on list of
        categories which are associated with the assortment recommendations. This is allowed when the categorization
        type is BRAND | string |"""

    values: Optional[list[str]] = UNSET
    """A list of values corresponds to the parameter in the filter. The values in the list should not be null or blank.
    Maximum 7 values are allowed in the list."""


class MultiValueFilter7Dict(TypedDict):
    parameter: Parameter18OrStr
    values: NotRequired[list[str]]

from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.row_filter_type import RowFilterTypeOrStr


class RangeFilter(SdkBaseModel):
    from_: Optional[str] = Field(default=UNSET, alias="from")
    """Start value for the filter range.

    <strong style="color: green;">Market availability: Global</strong>"""

    to: Optional[str] = UNSET
    """End value for the filter range.

    <strong style="color: green;">Market availability: Global</strong>"""

    row_filter_type: RowFilterTypeOrStr = Field(alias="rowFilterType")
    """The type of filter to apply.

    <strong style="color: green;">Market availability: Global</strong>"""

    column_name: str = Field(alias="columnName")
    """Specifies the column name to which the filter should be applied. Only certain columns in the report support this
    filter. Refer to the guide section for more details.

    <strong style="color: green;">Market availability: Global</strong>"""


class RangeFilterDict(TypedDict):
    from_: NotRequired[str]
    to: NotRequired[str]
    row_filter_type: RowFilterTypeOrStr
    column_name: str

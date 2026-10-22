from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type4 import Type4OrStr


class MultiValueFilter1(SdkBaseModel):
    values: Optional[list[str]] = UNSET
    """MultiValue filter values which has to be included in report.

    <strong style="color: green;">Market availability: Global</strong>"""

    column_name: str = Field(alias="columnName")
    """Specifies the column name to which the filter should be applied. Only certain columns in the report support this
    filter. Refer to the guide section for more details.

    <strong style="color: green;">Market availability: Global</strong>"""

    type_: Type4OrStr = Field(alias="type")
    """The type of filter to apply.

    <strong style="color: green;">Market availability: Global</strong>"""


class MultiValueFilter1Dict(TypedDict):
    values: NotRequired[list[str]]
    column_name: str
    type_: Type4OrStr

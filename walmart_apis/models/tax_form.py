from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TaxForm(SdkBaseModel):
    form_type: Optional[str] = Field(default=UNSET, alias="formType")
    """Tax form type, for example 1099-K."""

    form_id: Optional[str] = Field(default=UNSET, alias="formId")
    """Identifier of the generated tax form document."""


class TaxFormDict(TypedDict):
    form_type: NotRequired[str]
    form_id: NotRequired[str]

from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProgramActionFeedHeader1(SdkBaseModel):
    """ProgramAction feed header details"""

    version: Optional[str] = UNSET
    """This is static spec version."""

    locale: Optional[str] = UNSET
    """The associated language locale."""

    business_unit: Optional[str] = Field(default=UNSET, alias="businessUnit")
    """This is is static Walmart BU."""


class ProgramActionFeedHeader1Dict(TypedDict):
    version: NotRequired[str]
    locale: NotRequired[str]
    business_unit: NotRequired[str]

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdditionalAttribute(SdkBaseModel):
    name: str
    value: str


class AdditionalAttributeDict(TypedDict):
    name: str
    value: str

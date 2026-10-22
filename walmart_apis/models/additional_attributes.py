from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdditionalAttributes(SdkBaseModel):
    name: str
    value: str


class AdditionalAttributesDict(TypedDict):
    name: str
    value: str

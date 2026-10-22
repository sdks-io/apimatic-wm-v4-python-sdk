from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .additional_attribute import AdditionalAttribute, AdditionalAttributeDict


class AdditionalAttributes1(SdkBaseModel):
    additional_attribute: list[AdditionalAttribute] = Field(alias="additionalAttribute")


class AdditionalAttributes1Dict(TypedDict):
    additional_attribute: list[AdditionalAttributeDict]

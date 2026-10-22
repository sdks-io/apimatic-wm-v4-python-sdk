from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type11 import Type11OrStr


class DocumentType1(SdkBaseModel):
    """Object describing a single uploaded document."""

    file_name: str = Field(alias="fileName")
    """Original file name for the uploaded document."""

    type_: Type11OrStr = Field(alias="type")
    """Document category; one of PROOF_OF_DAMAGED_ITEM, INVOICE, OTHER, PPOD."""


class DocumentType1Dict(TypedDict):
    file_name: str
    type_: Type11OrStr

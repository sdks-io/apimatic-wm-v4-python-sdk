from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr


class DocumentType(SdkBaseModel):
    """Object describing a single uploaded document."""

    file_name: str = Field(alias="fileName")
    """Original file name as uploaded."""

    type_: Type1OrStr = Field(alias="type")
    """Document category."""


class DocumentTypeDict(TypedDict):
    file_name: str
    type_: Type1OrStr

from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.document_type2 import DocumentType2OrStr


class Document(SdkBaseModel):
    id: Optional[str] = UNSET
    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    file_type: Optional[str] = Field(default=UNSET, alias="fileType")
    document_type: Optional[DocumentType2OrStr] = Field(default=UNSET, alias="documentType")


class DocumentDict(TypedDict):
    id: NotRequired[str]
    file_name: NotRequired[str]
    file_type: NotRequired[str]
    document_type: NotRequired[DocumentType2OrStr]

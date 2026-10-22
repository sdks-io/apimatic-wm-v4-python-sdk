from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .document import Document, DocumentDict


class History(SdkBaseModel):
    author: Optional[str] = UNSET
    timestamp: Optional[RFC3339DateTime] = UNSET
    status: Optional[str] = UNSET
    notes: Optional[str] = UNSET
    documents: Optional[list[Document]] = UNSET


class HistoryDict(TypedDict):
    author: NotRequired[str]
    timestamp: NotRequired[RFC3339DateTime]
    status: NotRequired[str]
    notes: NotRequired[str]
    documents: NotRequired[list[DocumentDict]]

from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShippingDocuments(SdkBaseModel):
    """Shipping Documents"""

    document_format: Optional[str] = Field(default=UNSET, alias="documentFormat")
    document_type: Optional[str] = Field(default=UNSET, alias="documentType")
    base64_encoded_document: Optional[str] = Field(default=UNSET, alias="base64EncodedDocument")


class ShippingDocumentsDict(TypedDict):
    document_format: NotRequired[str]
    document_type: NotRequired[str]
    base64_encoded_document: NotRequired[str]

from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V3ClaimsShipmentProtectionClaimDocumentsRequest(SdkBaseModel):
    document_ids: list[str] = Field(alias="documentIds")
    """Array of document IDs to download"""


class V3ClaimsShipmentProtectionClaimDocumentsRequestDict(TypedDict):
    document_ids: list[str]

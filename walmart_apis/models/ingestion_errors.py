from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ingestion_error import IngestionError, IngestionErrorDict


class IngestionErrors(SdkBaseModel):
    """List of errors for an item."""

    ingestion_error: Optional[list[IngestionError]] = Field(default=UNSET, alias="ingestionError")


class IngestionErrorsDict(TypedDict):
    ingestion_error: NotRequired[list[IngestionErrorDict]]

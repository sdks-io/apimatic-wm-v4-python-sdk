from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_categories_payload import GetCategoriesPayload, GetCategoriesPayloadDict


class GetCategoriesResponse(SdkBaseModel):
    payload: Optional[list[GetCategoriesPayload]] = UNSET


class GetCategoriesResponseDict(TypedDict):
    payload: NotRequired[list[GetCategoriesPayloadDict]]

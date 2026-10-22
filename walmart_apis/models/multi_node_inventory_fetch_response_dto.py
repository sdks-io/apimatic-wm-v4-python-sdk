from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .elements import Elements, ElementsDict
from .meta import Meta, MetaDict


class MultiNodeInventoryFetchResponseDto(SdkBaseModel):
    meta: Optional[Meta] = UNSET
    elements: Optional[Elements] = UNSET


class MultiNodeInventoryFetchResponseDtoDict(TypedDict):
    meta: NotRequired[MetaDict]
    elements: NotRequired[ElementsDict]

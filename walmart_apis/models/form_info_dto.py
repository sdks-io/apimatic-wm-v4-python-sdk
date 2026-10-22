from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_dto import ItemDto, ItemDtoDict


class FormInfoDto(SdkBaseModel):
    combined: Optional[str] = UNSET
    """Indicates whether multiple statements are combined into a single form."""

    rollup: Optional[str] = UNSET
    """Represents an aggregated view or rolled-up status of the form."""

    name: Optional[str] = UNSET
    """The display name of the tax form (for example, 1099-K)."""

    f_char: Optional[str] = Field(default=UNSET, alias="fChar")
    """Internal flag character used for processing."""

    items: Optional[list[ItemDto]] = UNSET
    """List of item-level details associated with the tax form."""


class FormInfoDtoDict(TypedDict):
    combined: NotRequired[str]
    rollup: NotRequired[str]
    name: NotRequired[str]
    f_char: NotRequired[str]
    items: NotRequired[list[ItemDtoDict]]

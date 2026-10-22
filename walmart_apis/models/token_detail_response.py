from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scopes import Scopes, ScopesDict


class TokenDetailResponse(SdkBaseModel):
    scopes: Scopes
    """The API categories with their corresponding access levels"""

    expire_at: str = "1560973098000"
    """The timestamp when the token expires"""

    issued_at: str = "1560973098000"
    """The timestamp when the token is issued"""

    is_valid: bool = True
    """Whether the token is valid; boolean value of true or false"""

    is_channel_match: bool = True
    """Whether the keys Seller used are correctly associated"""


class TokenDetailResponseDict(TypedDict):
    scopes: ScopesDict
    expire_at: str
    issued_at: str
    is_valid: bool
    is_channel_match: bool

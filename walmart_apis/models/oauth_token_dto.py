from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OauthTokenDto(SdkBaseModel):
    access_token: str = Field(alias="accessToken")
    """Access token to be used for accessing business APIs"""

    token_type: Optional[str] = Field(default=UNSET, alias="tokenType")
    """Type of token according to user. (e.g., 'BEARER')"""

    expires_in: Optional[int] = Field(default=UNSET, alias="expiresIn")
    """Expiry time of access token in seconds"""

    refresh_token: Optional[str] = UNSET
    """Token which should be used to refresh access token.<br /> This field is present in response when **grant_type:
    authorization_code**"""


class OauthTokenDtoDict(TypedDict):
    access_token: str
    token_type: NotRequired[str]
    expires_in: NotRequired[int]
    refresh_token: NotRequired[str]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class OauthTokenModel(SdkBaseModel):
    access_token: str = "eyJraWQiOiI1MWY3MjM0Ny0wYWY5LTRhZ...."
    """Access token to be used for accessing business APIs"""

    token_type: str = "Bearer"
    """Type of token according to user. (e.g., 'BEARER')"""

    expires_in: int = 900
    """Expiry time of access token in seconds"""

    refresh_token: str = "APXcIoTpKMH9OQN……."
    """Token which should be used to refresh access token.<br /> This field is present in response when **grant_type:
    authorization_code**"""


class OauthTokenModelDict(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: NotRequired[str]

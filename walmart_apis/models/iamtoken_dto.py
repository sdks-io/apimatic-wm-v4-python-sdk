from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.grant_type import GrantType, GrantTypeOrStr


class IamtokenDto(SdkBaseModel):
    grant_type: GrantTypeOrStr = GrantType.CLIENT_CREDENTIALS
    """Type of grant requested. <br /> **Available grant types:** authorization_code, refresh_token and
    client_credentials"""

    code: str = "65CA5DA313A549D49D15D3119D9AD85D"
    """Authorization code obtained by your client app when the seller authorizes your app to access the seller resource.
    <br /> This field is required when **grant_type: authorization_code**"""

    redirect_uri: str = "https://example-client-app.com"
    """This should be same as one of your client app URIs provided while registering the app. <br /> This field is
    required when **grant_type: authorization_code**"""

    refresh_token: str = "APXcIoTpKMH9OQN....."
    """Refresh token received as response of Authentication API with authorization_code grant type, to be used to
    refresh the access token. <br /> This field is required when **grant_type: refresh_token**"""


class IamtokenDtoDict(TypedDict):
    grant_type: GrantTypeOrStr
    code: NotRequired[str]
    redirect_uri: NotRequired[str]
    refresh_token: NotRequired[str]

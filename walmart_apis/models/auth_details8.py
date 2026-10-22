from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthDetails8(SdkBaseModel):
    """Authentication details for accessing the destination URL, if the URL is protected.<br><b
    style='color:green;'>Market availability: Global</b>"""

    auth_method: Optional[str] = Field(default=UNSET, alias="authMethod")
    """Authentication method for the destination URL. Allowed values: BASIC_AUTH, OAUTH, HMAC."""

    user_name: Optional[str] = Field(default=UNSET, alias="userName")
    """Username used to access the destination URL (required for BASIC_AUTH)."""

    password: Optional[str] = UNSET
    """Password used to access the destination URL (required for BASIC_AUTH)."""

    auth_header_name: Optional[str] = Field(default=UNSET, alias="authHeaderName")
    """Header name used to pass the authorization value to the destination URL (for example, Authorization)."""

    auth_url: Optional[str] = Field(default=UNSET, alias="authUrl")
    """OAuth server or token URL used when the authentication method is OAUTH."""

    client_secret: Optional[str] = Field(default=UNSET, alias="clientSecret")
    """Client secret used with the OAuth server (OAUTH) or as key material for HMAC."""

    client_id: Optional[str] = Field(default=UNSET, alias="clientId")
    """Client ID used with the OAuth server when the authentication method is OAUTH."""


class AuthDetails8Dict(TypedDict):
    auth_method: NotRequired[str]
    user_name: NotRequired[str]
    password: NotRequired[str]
    auth_header_name: NotRequired[str]
    auth_url: NotRequired[str]
    client_secret: NotRequired[str]
    client_id: NotRequired[str]

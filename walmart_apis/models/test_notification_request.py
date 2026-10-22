from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_details import AuthDetails, AuthDetailsDict


class TestNotificationRequest(SdkBaseModel):
    event_type: str = Field(alias="eventType")
    """Event type to test. Use the same identifier you would use to subscribe."""

    event_version: str = Field(alias="eventVersion")
    """Version of the event type to test."""

    resource_name: str = Field(alias="resourceName")
    """Resource (functional category) that the event type is mapped to."""

    event_url: str = Field(alias="eventUrl")
    """Destination URL where notifications are delivered."""

    auth_details: Optional[AuthDetails] = Field(default=UNSET, alias="authDetails")
    """Authentication details for accessing the destination URL, if the URL is protected."""

    headers: Optional[dict[str, str]] = UNSET
    """Additional HTTP headers to include when delivering notifications to the destination URL. Use for custom
    authentication headers, tracking identifiers, or any other headers your endpoint requires.<br><b
    style='color:green;'>Market availability: Global</b>"""


class TestNotificationRequestDict(TypedDict):
    event_type: str
    event_version: str
    resource_name: str
    event_url: str
    auth_details: NotRequired[AuthDetailsDict]
    headers: NotRequired[dict[str, str]]

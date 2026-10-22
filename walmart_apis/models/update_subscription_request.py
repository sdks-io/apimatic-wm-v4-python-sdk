from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_details import AuthDetails, AuthDetailsDict


class UpdateSubscriptionRequest(SdkBaseModel):
    event_type: Optional[str] = Field(default=UNSET, alias="eventType")
    """Event type that is subscribed for notifications."""

    event_version: Optional[str] = Field(default=UNSET, alias="eventVersion")
    """Version of the specific event type."""

    resource_name: Optional[str] = Field(default=UNSET, alias="resourceName")
    """Resource (functional category) that the event type is mapped to."""

    event_url: Optional[str] = Field(default=UNSET, alias="eventUrl")
    """Destination URL where notifications are delivered."""

    auth_details: Optional[AuthDetails] = Field(default=UNSET, alias="authDetails")
    """Authentication details for accessing the destination URL, if the URL is protected."""

    headers: Optional[dict[str, str]] = UNSET
    """Additional HTTP headers to include when delivering notifications to the destination URL. Use for custom
    authentication headers, tracking identifiers, or any other headers your endpoint requires.<br><b
    style='color:green;'>Market availability: Global</b>"""

    status: Optional[str] = UNSET
    """Status of the subscription. Allowed values are ACTIVE or INACTIVE."""


class UpdateSubscriptionRequestDict(TypedDict):
    event_type: NotRequired[str]
    event_version: NotRequired[str]
    resource_name: NotRequired[str]
    event_url: NotRequired[str]
    auth_details: NotRequired[AuthDetailsDict]
    headers: NotRequired[dict[str, str]]
    status: NotRequired[str]

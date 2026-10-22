from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_details import AuthDetails, AuthDetailsDict


class CreateSubscriptionRequestRecord(SdkBaseModel):
    event_type: str = Field(alias="eventType")
    """Event type to subscribe to. For allowed values, refer to the Event Payload section or use the GET Event Types
    API."""

    event_version: str = Field(alias="eventVersion")
    """Version of the event type. For supported versions per eventType, refer to the Event Payload section or use the
    GET Event Types API."""

    resource_name: str = Field(alias="resourceName")
    """Resource (functional category) that the event type is mapped to. For allowed values per eventType, refer to the
    Event Payload section or use the GET Event Types API."""

    event_url: str = Field(alias="eventUrl")
    """Destination URL where notifications are delivered."""

    auth_details: Optional[AuthDetails] = Field(default=UNSET, alias="authDetails")
    """Authentication details for accessing the destination URL, if the URL is protected."""

    headers: Optional[dict[str, str]] = UNSET
    """Additional HTTP headers to include when delivering notifications to the destination URL. Use for custom
    authentication headers, tracking identifiers, or any other headers your endpoint requires.<br><b
    style='color:green;'>Market availability: Global</b>"""

    status: str
    """Status of the subscription. Allowed values: ACTIVE, INACTIVE. To create a subscription, use status = ACTIVE.
    Notifications are sent only when the subscription is ACTIVE."""


class CreateSubscriptionRequestRecordDict(TypedDict):
    event_type: str
    event_version: str
    resource_name: str
    event_url: str
    auth_details: NotRequired[AuthDetailsDict]
    headers: NotRequired[dict[str, str]]
    status: str

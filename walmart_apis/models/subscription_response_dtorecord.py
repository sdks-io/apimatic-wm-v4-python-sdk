from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_details import AuthDetails, AuthDetailsDict


class SubscriptionResponseDtorecord(SdkBaseModel):
    event_type: Optional[str] = Field(default=UNSET, alias="eventType")
    """Event type for which the subscription was created."""

    subscription_id: Optional[str] = Field(default=UNSET, alias="subscriptionId")
    """Unique identifier for the subscription. Use this ID to retrieve, update, or delete the subscription."""

    partner_id: Optional[str] = Field(default=UNSET, alias="partnerId")
    """Partner ID of the seller who created the subscription."""

    event_version: Optional[str] = Field(default=UNSET, alias="eventVersion")
    """Version of the event type for which the subscription was created."""

    resource_name: Optional[str] = Field(default=UNSET, alias="resourceName")
    """Resource (functional category) that the event type is mapped to."""

    status: Optional[str] = UNSET
    """Subscription status. Allowed values: ACTIVE, INACTIVE."""

    event_url: Optional[str] = Field(default=UNSET, alias="eventUrl")
    """Destination URL where notifications are delivered."""

    auth_details: Optional[AuthDetails] = Field(default=UNSET, alias="authDetails")
    """Authentication details for accessing the destination URL, if the URL is protected."""

    headers: Optional[dict[str, str]] = UNSET
    """Additional HTTP headers to include when delivering notifications to the destination URL. Use for custom
    authentication headers, tracking identifiers, or any other headers your endpoint requires.<br><b
    style='color:green;'>Market availability: Global</b>"""


class SubscriptionResponseDtorecordDict(TypedDict):
    event_type: NotRequired[str]
    subscription_id: NotRequired[str]
    partner_id: NotRequired[str]
    event_version: NotRequired[str]
    resource_name: NotRequired[str]
    status: NotRequired[str]
    event_url: NotRequired[str]
    auth_details: NotRequired[AuthDetailsDict]
    headers: NotRequired[dict[str, str]]

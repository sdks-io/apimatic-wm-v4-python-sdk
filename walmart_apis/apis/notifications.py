from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market2 import WmMarket2OrStr
from ..models.reject_recommendations_response_payload import RejectRecommendationsResponsePayload
from ..models.v3_webhooks_event_types_response import V3WebhooksEventTypesResponse
from ..models.v3_webhooks_subscriptions_request import (
    V3WebhooksSubscriptionsRequest,
    V3WebhooksSubscriptionsRequestDict,
)
from ..models.v3_webhooks_subscriptions_request1 import (
    V3WebhooksSubscriptionsRequest1,
    V3WebhooksSubscriptionsRequest1Dict,
)
from ..models.v3_webhooks_subscriptions_response import V3WebhooksSubscriptionsResponse
from ..models.v3_webhooks_subscriptions_response1 import V3WebhooksSubscriptionsResponse1
from ..models.v3_webhooks_subscriptions_response2 import V3WebhooksSubscriptionsResponse2
from ..models.v3_webhooks_subscriptions_response3 import V3WebhooksSubscriptionsResponse3
from ..models.v3_webhooks_test_request import V3WebhooksTestRequest, V3WebhooksTestRequestDict
from ..server.server import Server


class Notifications:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NotificationsWithRawResponse(client, server, auth)

    def create_subscription(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse1:
        """Create one or more webhook subscriptions for event notifications by selecting an event type, event version,
        resource name, and providing a destination event URL.

        Use the Get Event Types API to retrieve available event types, versions, and resource names. Configure the
        eventUrl to receive notifications.

        URL authentication options
        - If authMethod is BASIC_AUTH, Walmart passes an authentication header to the eventUrl using authHeaderName as
            the header key and the Base64-encoded userName:password as the value.
        - If authMethod is HMAC, Walmart passes an authentication header to the eventUrl using authHeaderName as the
            header key and HMACSHA256 of the complete response as the value, with clientSecret as the key.
        - If authMethod is OAUTH, Walmart makes a POST call to authUrl to generate a token with request body
            "grant_type=client_credentials" and headers:
        (1) Authorization header using authHeaderName as the key and Base64-encoded clientId:clientSecret as the value,
        (2) Accept: "application/json; charset=UTF-8", (3) Content-Type: "application/x-www-form-urlencoded;
        charset=ISO-8859-1", and (4) any custom headers provided in headers. The authUrl must return HTTP 200 with
        access_token and expires_in fields. When sending notifications to eventUrl, Walmart includes the access_token in
        headers using authHeaderName as the key and value "Bearer <access_token>", along with any custom headers
        provided in headers.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for creating one or more subscriptions.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.create_subscription(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def delete_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse2:
        """Delete an existing webhook subscription by ID. After deletion, the subscription cannot be retrieved.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to delete.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_subscription(
                subscription_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_all_subscriptions(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        subscription_id: str | None = None,
        event_type: str | None = None,
        resource_name: str | None = None,
        status: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse:
        """Retrieve details of all webhook subscriptions created using the Create Subscription API. Use query parameters
        to filter by subscription ID, event type, resource, or status.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            subscription_id: Filter results to a specific subscription by its unique identifier.<br><b
                style='color:green;'>Market availability: Global</b>
            event_type: Filter results to a specific event type. Refer to the Event Payload section for the list of
                available event types.<br><b style='color:green;'>Market availability: Global</b>
            resource_name: Filter results to a specific resource (functional category). Refer to the Event Payload
                section for the list of available resource names.<br><b style='color:green;'>Market availability:
                Global</b>
            status: Filter results by subscription status. Allowed values: ACTIVE, INACTIVE.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_all_subscriptions(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                subscription_id=subscription_id,
                event_type=event_type,
                resource_name=resource_name,
                status=status,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_event_types(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksEventTypesResponse:
        """Retrieve the list of event types and resource names available for subscription. Notifications are triggered
        only for event types that you subscribe to using the Create Subscription API.

        Event types are workflow events fired when statuses or conditions change (for example, an offer moving from
        published to unpublished, an order auto-cancellation, or a buy box change).

        Resource names are functional API categories (for example, ITEM, PRICE, ORDER, INVENTORY). Permissions to
        subscribe to an event type are governed by the resource's delegated access permissions.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation. Returns the list of event types and resource names available for subscription.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_event_types(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def test_notification(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksTestRequest | V3WebhooksTestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """Send a test notification to a destination URL using a sample payload.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.test_notification(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse3:
        """Update the details of a subscription. You can update the event version, destination URL, headers, and
        authentication details. You can also enable or disable the subscription by changing the status to ACTIVE or
        INACTIVE.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to update.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for updating a subscription.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation. Returns the updated subscription(s).

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_subscription(
                subscription_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> NotificationsWithRawResponse:
        return self._with_raw_response


class AsyncNotifications:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNotificationsWithRawResponse(client, server, auth)

    async def create_subscription(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse1:
        """Create one or more webhook subscriptions for event notifications by selecting an event type, event version,
        resource name, and providing a destination event URL.

        Use the Get Event Types API to retrieve available event types, versions, and resource names. Configure the
        eventUrl to receive notifications.

        URL authentication options
        - If authMethod is BASIC_AUTH, Walmart passes an authentication header to the eventUrl using authHeaderName as
            the header key and the Base64-encoded userName:password as the value.
        - If authMethod is HMAC, Walmart passes an authentication header to the eventUrl using authHeaderName as the
            header key and HMACSHA256 of the complete response as the value, with clientSecret as the key.
        - If authMethod is OAUTH, Walmart makes a POST call to authUrl to generate a token with request body
            "grant_type=client_credentials" and headers:
        (1) Authorization header using authHeaderName as the key and Base64-encoded clientId:clientSecret as the value,
        (2) Accept: "application/json; charset=UTF-8", (3) Content-Type: "application/x-www-form-urlencoded;
        charset=ISO-8859-1", and (4) any custom headers provided in headers. The authUrl must return HTTP 200 with
        access_token and expires_in fields. When sending notifications to eventUrl, Walmart includes the access_token in
        headers using authHeaderName as the key and value "Bearer <access_token>", along with any custom headers
        provided in headers.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for creating one or more subscriptions.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_subscription(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def delete_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse2:
        """Delete an existing webhook subscription by ID. After deletion, the subscription cannot be retrieved.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to delete.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_subscription(
                subscription_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_all_subscriptions(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        subscription_id: str | None = None,
        event_type: str | None = None,
        resource_name: str | None = None,
        status: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse:
        """Retrieve details of all webhook subscriptions created using the Create Subscription API. Use query parameters
        to filter by subscription ID, event type, resource, or status.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            subscription_id: Filter results to a specific subscription by its unique identifier.<br><b
                style='color:green;'>Market availability: Global</b>
            event_type: Filter results to a specific event type. Refer to the Event Payload section for the list of
                available event types.<br><b style='color:green;'>Market availability: Global</b>
            resource_name: Filter results to a specific resource (functional category). Refer to the Event Payload
                section for the list of available resource names.<br><b style='color:green;'>Market availability:
                Global</b>
            status: Filter results by subscription status. Allowed values: ACTIVE, INACTIVE.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_all_subscriptions(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                subscription_id=subscription_id,
                event_type=event_type,
                resource_name=resource_name,
                status=status,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_event_types(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksEventTypesResponse:
        """Retrieve the list of event types and resource names available for subscription. Notifications are triggered
        only for event types that you subscribe to using the Create Subscription API.

        Event types are workflow events fired when statuses or conditions change (for example, an offer moving from
        published to unpublished, an order auto-cancellation, or a buy box change).

        Resource names are functional API categories (for example, ITEM, PRICE, ORDER, INVENTORY). Permissions to
        subscribe to an event type are governed by the resource's delegated access permissions.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation. Returns the list of event types and resource names available for subscription.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_event_types(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def test_notification(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksTestRequest | V3WebhooksTestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """Send a test notification to a destination URL using a sample payload.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.test_notification(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WebhooksSubscriptionsResponse3:
        """Update the details of a subscription. You can update the event version, destination URL, headers, and
        authentication details. You can also enable or disable the subscription by changing the status to ACTIVE or
        INACTIVE.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to update.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for updating a subscription.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation. Returns the updated subscription(s).

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_subscription(
                subscription_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNotificationsWithRawResponse:
        return self._with_raw_response


class NotificationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_subscription(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse1, RawError]:
        """Create one or more webhook subscriptions for event notifications by selecting an event type, event version,
        resource name, and providing a destination event URL.

        Use the Get Event Types API to retrieve available event types, versions, and resource names. Configure the
        eventUrl to receive notifications.

        URL authentication options
        - If authMethod is BASIC_AUTH, Walmart passes an authentication header to the eventUrl using authHeaderName as
            the header key and the Base64-encoded userName:password as the value.
        - If authMethod is HMAC, Walmart passes an authentication header to the eventUrl using authHeaderName as the
            header key and HMACSHA256 of the complete response as the value, with clientSecret as the key.
        - If authMethod is OAUTH, Walmart makes a POST call to authUrl to generate a token with request body
            "grant_type=client_credentials" and headers:
        (1) Authorization header using authHeaderName as the key and Base64-encoded clientId:clientSecret as the value,
        (2) Accept: "application/json; charset=UTF-8", (3) Content-Type: "application/x-www-form-urlencoded;
        charset=ISO-8859-1", and (4) any custom headers provided in headers. The authUrl must return HTTP 200 with
        access_token and expires_in fields. When sending notifications to eventUrl, Walmart includes the access_token in
        headers using authHeaderName as the key and value "Bearer <access_token>", along with any custom headers
        provided in headers.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for creating one or more subscriptions.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/webhooks/subscriptions"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3WebhooksSubscriptionsResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse2, RawError]:
        """Delete an existing webhook subscription by ID. After deletion, the subscription cannot be retrieved.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to delete.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/webhooks/subscriptions/{subscriptionId}"),
            path_params=[param[str]("subscriptionId", subscription_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3WebhooksSubscriptionsResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_all_subscriptions(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        subscription_id: str | None = None,
        event_type: str | None = None,
        resource_name: str | None = None,
        status: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse, RawError]:
        """Retrieve details of all webhook subscriptions created using the Create Subscription API. Use query parameters
        to filter by subscription ID, event type, resource, or status.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            subscription_id: Filter results to a specific subscription by its unique identifier.<br><b
                style='color:green;'>Market availability: Global</b>
            event_type: Filter results to a specific event type. Refer to the Event Payload section for the list of
                available event types.<br><b style='color:green;'>Market availability: Global</b>
            resource_name: Filter results to a specific resource (functional category). Refer to the Event Payload
                section for the list of available resource names.<br><b style='color:green;'>Market availability:
                Global</b>
            status: Filter results by subscription status. Allowed values: ACTIVE, INACTIVE.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/webhooks/subscriptions"),
            query_params=[
                param[str | None]("subscriptionId", subscription_id),
                param[str | None]("eventType", event_type),
                param[str | None]("resourceName", resource_name),
                param[str | None]("status", status),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3WebhooksSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_event_types(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksEventTypesResponse, RawError]:
        """Retrieve the list of event types and resource names available for subscription. Notifications are triggered
        only for event types that you subscribe to using the Create Subscription API.

        Event types are workflow events fired when statuses or conditions change (for example, an offer moving from
        published to unpublished, an order auto-cancellation, or a buy box change).

        Resource names are functional API categories (for example, ITEM, PRICE, ORDER, INVENTORY). Permissions to
        subscribe to an event type are governed by the resource's delegated access permissions.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/webhooks/eventTypes"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3WebhooksEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def test_notification(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksTestRequest | V3WebhooksTestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, RawError]:
        """Send a test notification to a destination URL using a sample payload.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/webhooks/test"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksTestRequest | V3WebhooksTestRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse3, RawError]:
        """Update the details of a subscription. You can update the event version, destination URL, headers, and
        authentication details. You can also enable or disable the subscription by changing the status to ACTIVE or
        INACTIVE.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to update.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for updating a subscription.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v3/webhooks/subscriptions/{subscriptionId}"),
            path_params=[param[str]("subscriptionId", subscription_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3WebhooksSubscriptionsResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncNotificationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_subscription(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse1, RawError]:
        """Create one or more webhook subscriptions for event notifications by selecting an event type, event version,
        resource name, and providing a destination event URL.

        Use the Get Event Types API to retrieve available event types, versions, and resource names. Configure the
        eventUrl to receive notifications.

        URL authentication options
        - If authMethod is BASIC_AUTH, Walmart passes an authentication header to the eventUrl using authHeaderName as
            the header key and the Base64-encoded userName:password as the value.
        - If authMethod is HMAC, Walmart passes an authentication header to the eventUrl using authHeaderName as the
            header key and HMACSHA256 of the complete response as the value, with clientSecret as the key.
        - If authMethod is OAUTH, Walmart makes a POST call to authUrl to generate a token with request body
            "grant_type=client_credentials" and headers:
        (1) Authorization header using authHeaderName as the key and Base64-encoded clientId:clientSecret as the value,
        (2) Accept: "application/json; charset=UTF-8", (3) Content-Type: "application/x-www-form-urlencoded;
        charset=ISO-8859-1", and (4) any custom headers provided in headers. The authUrl must return HTTP 200 with
        access_token and expires_in fields. When sending notifications to eventUrl, Walmart includes the access_token in
        headers using authHeaderName as the key and value "Bearer <access_token>", along with any custom headers
        provided in headers.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for creating one or more subscriptions.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/webhooks/subscriptions"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3WebhooksSubscriptionsResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse2, RawError]:
        """Delete an existing webhook subscription by ID. After deletion, the subscription cannot be retrieved.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to delete.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/webhooks/subscriptions/{subscriptionId}"),
            path_params=[param[str]("subscriptionId", subscription_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3WebhooksSubscriptionsResponse2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_all_subscriptions(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        subscription_id: str | None = None,
        event_type: str | None = None,
        resource_name: str | None = None,
        status: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse, RawError]:
        """Retrieve details of all webhook subscriptions created using the Create Subscription API. Use query parameters
        to filter by subscription ID, event type, resource, or status.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            subscription_id: Filter results to a specific subscription by its unique identifier.<br><b
                style='color:green;'>Market availability: Global</b>
            event_type: Filter results to a specific event type. Refer to the Event Payload section for the list of
                available event types.<br><b style='color:green;'>Market availability: Global</b>
            resource_name: Filter results to a specific resource (functional category). Refer to the Event Payload
                section for the list of available resource names.<br><b style='color:green;'>Market availability:
                Global</b>
            status: Filter results by subscription status. Allowed values: ACTIVE, INACTIVE.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/webhooks/subscriptions"),
            query_params=[
                param[str | None]("subscriptionId", subscription_id),
                param[str | None]("eventType", event_type),
                param[str | None]("resourceName", resource_name),
                param[str | None]("status", status),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3WebhooksSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_event_types(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksEventTypesResponse, RawError]:
        """Retrieve the list of event types and resource names available for subscription. Notifications are triggered
        only for event types that you subscribe to using the Create Subscription API.

        Event types are workflow events fired when statuses or conditions change (for example, an offer moving from
        published to unpublished, an order auto-cancellation, or a buy box change).

        Resource names are functional API categories (for example, ITEM, PRICE, ORDER, INVENTORY). Permissions to
        subscribe to an event type are governed by the resource's delegated access permissions.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/webhooks/eventTypes"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3WebhooksEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def test_notification(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksTestRequest | V3WebhooksTestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, RawError]:
        """Send a test notification to a destination URL using a sample payload.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/webhooks/test"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksTestRequest | V3WebhooksTestRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_subscription(
        self,
        subscription_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket2OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WebhooksSubscriptionsResponse3, RawError]:
        """Update the details of a subscription. You can update the event version, destination URL, headers, and
        authentication details. You can also enable or disable the subscription by changing the status to ACTIVE or
        INACTIVE.

        <b style='color:green;'>Market availability: Global</b>

        Args:
            subscription_id: Unique identifier of the subscription to update.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Name of the Walmart service being called.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API.<br><b style='color:green;'>Market availability:
                Global</span></b>
            body: Request body parameters for updating a subscription.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v3/webhooks/subscriptions/{subscriptionId}"),
            path_params=[param[str]("subscriptionId", subscription_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket2OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3WebhooksSubscriptionsResponse3],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

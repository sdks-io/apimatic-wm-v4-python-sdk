from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_id1 import FeedId1
from ..models.v3_feeds_request1 import V3FeedsRequest1, V3FeedsRequest1Dict
from ..models.v3_settings_shipping_simplifiedshippingsettings_account_request import (
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_account_request1 import (
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1,
    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_account_response import (
    V3SettingsShippingSimplifiedshippingsettingsAccountResponse,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_account_response1 import (
    V3SettingsShippingSimplifiedshippingsettingsAccountResponse1,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_request import (
    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest,
    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_response import (
    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse,
)
from ..models.v3_settings_shipping_simplifiedshippingsettings_response import (
    V3SettingsShippingSimplifiedshippingsettingsResponse,
)
from ..server.server import Server


class SimplifiedShippingSettings:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = SimplifiedShippingSettingsWithRawResponse(client, server)

    def bulk_migrate_offers_for_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest1 | V3FeedsRequest1Dict,
        *,
        feed_type: str = "PROGRAM_ACTIONS",
        request_type: str = "SHIPPING_CONFIG",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """This API is used to bulk migrate offers from manual templates to Simplified Shipping Settings and vice-versa.
        Make sure to create account level settings before proceeding with item migration to Simplified Shipping
        Settings. <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            feed_type: The type of feed, which specifies the nature of the update. <br><b style='color:green;'>Market
                availability: US</span></b>
            request_type: Specifies the type of request being made. <br><b style='color:green;'>Market availability:
                US</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.bulk_migrate_offers_for_simplified_shipping_settings(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                feed_type=feed_type,
                request_type=request_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def create_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]:
        """This API is used to update the account-level configuration. The carrier configurations created using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API..
        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.create_simplified_shipping_settings(
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

    def get_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsResponse]:
        """This API helps seller to fetch the Simplified Shipping Settings for a seller account and FC-level
        configurations. <br><b style='color:green;'>Market availability: Global</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_simplified_shipping_settings(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_fc_level_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
            | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]:
        """This API can be used for overriding the configurations at one or more Fulfillment Centers. <br><b
        style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_fc_level_simplified_shipping_settings(
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

    def update_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]:
        """This API is used to update the account-level configuration. The carrier configurations updated using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API.

        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_simplified_shipping_settings(
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
    def with_raw_response(self) -> SimplifiedShippingSettingsWithRawResponse:
        return self._with_raw_response


class AsyncSimplifiedShippingSettings:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncSimplifiedShippingSettingsWithRawResponse(client, server)

    async def bulk_migrate_offers_for_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest1 | V3FeedsRequest1Dict,
        *,
        feed_type: str = "PROGRAM_ACTIONS",
        request_type: str = "SHIPPING_CONFIG",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """This API is used to bulk migrate offers from manual templates to Simplified Shipping Settings and vice-versa.
        Make sure to create account level settings before proceeding with item migration to Simplified Shipping
        Settings. <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            feed_type: The type of feed, which specifies the nature of the update. <br><b style='color:green;'>Market
                availability: US</span></b>
            request_type: Specifies the type of request being made. <br><b style='color:green;'>Market availability:
                US</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_migrate_offers_for_simplified_shipping_settings(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                feed_type=feed_type,
                request_type=request_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def create_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]:
        """This API is used to update the account-level configuration. The carrier configurations created using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API..
        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_simplified_shipping_settings(
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

    async def get_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsResponse]:
        """This API helps seller to fetch the Simplified Shipping Settings for a seller account and FC-level
        configurations. <br><b style='color:green;'>Market availability: Global</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_simplified_shipping_settings(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_fc_level_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
            | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]:
        """This API can be used for overriding the configurations at one or more Fulfillment Centers. <br><b
        style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_fc_level_simplified_shipping_settings(
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

    async def update_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]:
        """This API is used to update the account-level configuration. The carrier configurations updated using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API.

        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_simplified_shipping_settings(
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
    def with_raw_response(self) -> AsyncSimplifiedShippingSettingsWithRawResponse:
        return self._with_raw_response


class SimplifiedShippingSettingsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def bulk_migrate_offers_for_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest1 | V3FeedsRequest1Dict,
        *,
        feed_type: str = "PROGRAM_ACTIONS",
        request_type: str = "SHIPPING_CONFIG",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RawError]:
        """This API is used to bulk migrate offers from manual templates to Simplified Shipping Settings and vice-versa.
        Make sure to create account level settings before proceeding with item migration to Simplified Shipping
        Settings. <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            feed_type: The type of feed, which specifies the nature of the update. <br><b style='color:green;'>Market
                availability: US</span></b>
            request_type: Specifies the type of request being made. <br><b style='color:green;'>Market availability:
                US</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[str]("feedType", feed_type), param[str]("requestType", request_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsRequest1 | V3FeedsRequest1Dict](body),
            decoder=json_decoder[FeedId1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1], RawError]:
        """This API is used to update the account-level configuration. The carrier configurations created using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API..
        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/account"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
                    | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
                )
            ](body),
            decoder=json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsResponse], RawError]:
        """This API helps seller to fetch the Simplified Shipping Settings for a seller account and FC-level
        configurations. <br><b style='color:green;'>Market availability: Global</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_fc_level_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
            | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse], RawError]:
        """This API can be used for overriding the configurations at one or more Fulfillment Centers. <br><b
        style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/fulfillmentcenter"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
                    | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
                )
            ](body),
            decoder=json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse], RawError]:
        """This API is used to update the account-level configuration. The carrier configurations updated using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API.

        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/account"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsAccountRequest
                    | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
                )
            ](body),
            decoder=json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSimplifiedShippingSettingsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def bulk_migrate_offers_for_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest1 | V3FeedsRequest1Dict,
        *,
        feed_type: str = "PROGRAM_ACTIONS",
        request_type: str = "SHIPPING_CONFIG",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RawError]:
        """This API is used to bulk migrate offers from manual templates to Simplified Shipping Settings and vice-versa.
        Make sure to create account level settings before proceeding with item migration to Simplified Shipping
        Settings. <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            feed_type: The type of feed, which specifies the nature of the update. <br><b style='color:green;'>Market
                availability: US</span></b>
            request_type: Specifies the type of request being made. <br><b style='color:green;'>Market availability:
                US</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[str]("feedType", feed_type), param[str]("requestType", request_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsRequest1 | V3FeedsRequest1Dict](body),
            decoder=async_json_decoder[FeedId1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1], RawError]:
        """This API is used to update the account-level configuration. The carrier configurations created using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API..
        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/account"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsAccountRequest1
                    | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict
                )
            ](body),
            decoder=async_json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsResponse], RawError]:
        """This API helps seller to fetch the Simplified Shipping Settings for a seller account and FC-level
        configurations. <br><b style='color:green;'>Market availability: Global</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_fc_level_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
            | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse], RawError]:
        """This API can be used for overriding the configurations at one or more Fulfillment Centers. <br><b
        style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/fulfillmentcenter"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest
                    | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict
                )
            ](body),
            decoder=async_json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_simplified_shipping_settings(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3SettingsShippingSimplifiedshippingsettingsAccountRequest
            | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse], RawError]:
        """This API is used to update the account-level configuration. The carrier configurations updated using this API
        will be applied across all Fulfillment Centers (FCs) unless they are overridden using the FC Configuration API.

        <br><b style='color:green;'>Market availability: US</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</span></b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <br><b
                style='color:green;'>Market availability: Global</span></b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.. <br><b style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/settings/shipping/simplifiedshippingsettings/account"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3SettingsShippingSimplifiedshippingsettingsAccountRequest
                    | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict
                )
            ](body),
            decoder=async_json_decoder[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

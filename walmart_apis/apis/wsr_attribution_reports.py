from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_tag_templates_error import GetTagTemplatesErrorBody, get_tag_templates_error_mapper
from ..errors.get_wsr_item_report_error import GetWsrItemReportErrorBody, get_wsr_item_report_error_mapper
from ..errors.get_wsr_performance_report_error import (
    GetWsrPerformanceReportErrorBody,
    get_wsr_performance_report_error_mapper,
)
from ..models.enums.template_type import TemplateType, TemplateTypeOrStr
from ..models.enums.wm_global_version import WmGlobalVersion, WmGlobalVersionOrStr
from ..models.enums.wm_market import WmMarket, WmMarketOrStr
from ..models.wsr_item_report_response import WsrItemReportResponse
from ..models.wsr_performance_report_response import WsrPerformanceReportResponse
from ..models.wsr_report_request import WsrReportRequest, WsrReportRequestDict
from ..models.wsr_tag_templates_response import WsrTagTemplatesResponse
from ..server.server import Server


class WsrAttributionReports:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WsrAttributionReportsWithRawResponse(client, server, auth)

    def get_tag_templates(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        template_type: TemplateTypeOrStr = TemplateType.NON_MACRO,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrTagTemplatesResponse:
        """Fetch referral link tag templates for different page types (ITEM, BRANDSHOP). Tag templates contain URL
        patterns with placeholders that can be used to construct final referral URLs/tags for affiliate tracking.

        <span style="color:green">**Market availability: US**</span>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            template_type: The type of tag template to fetch. Currently supports NON_MACRO. <span
                style="color:green">**Market availability: Global**</span>
            wm_global_version: The version of the global API used.
            wm_market: The target market of the API call.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tag templates retrieved successfully

        Raises:
            ApiError: Invalid request parameters - Invalid template type Internal server error - Unable to fetch tag
                templates ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.get_tag_templates(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                template_type=template_type,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_wsr_item_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrItemReportResponse:
        """Retrieve detailed item-level performance reports for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns performance data at the individual item/product level, including product details such as
        item name, category, and product type along with performance metrics. This is useful for understanding which
        products are driving the most revenue through affiliate channels.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Item report request with filters and parameters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Item report retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters Internal server error - Unable to generate item report
                ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.get_wsr_item_report(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                body,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_wsr_performance_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrPerformanceReportResponse:
        """Retrieve performance analytics and metrics for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns aggregated performance data including clicks, orders, GMV, and commission metrics within a
        specified date range. Data can be aggregated at different levels based on the ``performanceBy`` parameter.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Performance report request with date range and optional filters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Performance report retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters Internal server error - Unable to generate performance
                report ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.get_wsr_performance_report(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                body,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> WsrAttributionReportsWithRawResponse:
        return self._with_raw_response


class AsyncWsrAttributionReports:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWsrAttributionReportsWithRawResponse(client, server, auth)

    async def get_tag_templates(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        template_type: TemplateTypeOrStr = TemplateType.NON_MACRO,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrTagTemplatesResponse:
        """Fetch referral link tag templates for different page types (ITEM, BRANDSHOP). Tag templates contain URL
        patterns with placeholders that can be used to construct final referral URLs/tags for affiliate tracking.

        <span style="color:green">**Market availability: US**</span>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            template_type: The type of tag template to fetch. Currently supports NON_MACRO. <span
                style="color:green">**Market availability: Global**</span>
            wm_global_version: The version of the global API used.
            wm_market: The target market of the API call.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tag templates retrieved successfully

        Raises:
            ApiError: Invalid request parameters - Invalid template type Internal server error - Unable to fetch tag
                templates ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.get_tag_templates(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                template_type=template_type,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_wsr_item_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrItemReportResponse:
        """Retrieve detailed item-level performance reports for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns performance data at the individual item/product level, including product details such as
        item name, category, and product type along with performance metrics. This is useful for understanding which
        products are driving the most revenue through affiliate channels.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Item report request with filters and parameters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Item report retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters Internal server error - Unable to generate item report
                ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.get_wsr_item_report(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                body,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_wsr_performance_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WsrPerformanceReportResponse:
        """Retrieve performance analytics and metrics for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns aggregated performance data including clicks, orders, GMV, and commission metrics within a
        specified date range. Data can be aggregated at different levels based on the ``performanceBy`` parameter.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Performance report request with date range and optional filters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Performance report retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters Internal server error - Unable to generate performance
                report ``error`` is ``WsrErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.get_wsr_performance_report(
                wm_sec_access_token,
                wm_svc_name,
                wm_qos_correlation_id,
                body,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWsrAttributionReportsWithRawResponse:
        return self._with_raw_response


class WsrAttributionReportsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_tag_templates(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        template_type: TemplateTypeOrStr = TemplateType.NON_MACRO,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrTagTemplatesResponse, GetTagTemplatesErrorBody]:
        """Fetch referral link tag templates for different page types (ITEM, BRANDSHOP). Tag templates contain URL
        patterns with placeholders that can be used to construct final referral URLs/tags for affiliate tracking.

        <span style="color:green">**Market availability: US**</span>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            template_type: The type of tag template to fetch. Currently supports NON_MACRO. <span
                style="color:green">**Market availability: Global**</span>
            wm_global_version: The version of the global API used.
            wm_market: The target market of the API call.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/wsr/attribution/tag-templates/{templateType}"),
            path_params=[param[TemplateTypeOrStr]("templateType", template_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WsrTagTemplatesResponse],
            error_mapper=get_tag_templates_error_mapper,
            request_options=request_options,
        )

    def get_wsr_item_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrItemReportResponse, GetWsrItemReportErrorBody]:
        """Retrieve detailed item-level performance reports for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns performance data at the individual item/product level, including product details such as
        item name, category, and product type along with performance metrics. This is useful for understanding which
        products are driving the most revenue through affiliate channels.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Item report request with filters and parameters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/wsr/attribution/item-report"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[WsrReportRequest | WsrReportRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WsrItemReportResponse],
            error_mapper=get_wsr_item_report_error_mapper,
            request_options=request_options,
        )

    def get_wsr_performance_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrPerformanceReportResponse, GetWsrPerformanceReportErrorBody]:
        """Retrieve performance analytics and metrics for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns aggregated performance data including clicks, orders, GMV, and commission metrics within a
        specified date range. Data can be aggregated at different levels based on the ``performanceBy`` parameter.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Performance report request with date range and optional filters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/wsr/attribution/performance-report"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[WsrReportRequest | WsrReportRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WsrPerformanceReportResponse],
            error_mapper=get_wsr_performance_report_error_mapper,
            request_options=request_options,
        )


class AsyncWsrAttributionReportsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_tag_templates(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        template_type: TemplateTypeOrStr = TemplateType.NON_MACRO,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrTagTemplatesResponse, GetTagTemplatesErrorBody]:
        """Fetch referral link tag templates for different page types (ITEM, BRANDSHOP). Tag templates contain URL
        patterns with placeholders that can be used to construct final referral URLs/tags for affiliate tracking.

        <span style="color:green">**Market availability: US**</span>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            template_type: The type of tag template to fetch. Currently supports NON_MACRO. <span
                style="color:green">**Market availability: Global**</span>
            wm_global_version: The version of the global API used.
            wm_market: The target market of the API call.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/wsr/attribution/tag-templates/{templateType}"),
            path_params=[param[TemplateTypeOrStr]("templateType", template_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WsrTagTemplatesResponse],
            error_mapper=get_tag_templates_error_mapper,
            request_options=request_options,
        )

    async def get_wsr_item_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrItemReportResponse, GetWsrItemReportErrorBody]:
        """Retrieve detailed item-level performance reports for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns performance data at the individual item/product level, including product details such as
        item name, category, and product type along with performance metrics. This is useful for understanding which
        products are driving the most revenue through affiliate channels.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Item report request with filters and parameters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/wsr/attribution/item-report"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[WsrReportRequest | WsrReportRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WsrItemReportResponse],
            error_mapper=get_wsr_item_report_error_mapper,
            request_options=request_options,
        )

    async def get_wsr_performance_report(
        self,
        wm_sec_access_token: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        body: WsrReportRequest | WsrReportRequestDict,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WsrPerformanceReportResponse, GetWsrPerformanceReportErrorBody]:
        """Retrieve performance analytics and metrics for affiliate campaigns.

        <span style="color:green">**Market availability: US only**</span>

        This endpoint returns aggregated performance data including clicks, orders, GMV, and commission metrics within a
        specified date range. Data can be aggregated at different levels based on the ``performanceBy`` parameter.

        ### Aggregation Levels and Field Availability The ``performanceBy`` parameter determines which identifier fields
        are populated in the response:

        | performanceBy | campaignId | adGroupId | creativeId |
        |---------------|------------|-----------|------------|
        | CAMPAIGN | ✓ | null | null |
        | ADGROUP | ✓ | ✓ | null |
        | CREATIVE | ✓ | ✓ | ✓ |

        ### Supported filters
        - ``startDate``: Report start date (required)
        - ``endDate``: Report end date (required)
        - ``campaignId``: Filter by specific campaign IDs
        - ``adGroupId``: Filter by specific ad group IDs
        - ``creativeId``: Filter by specific creative IDs

        ### Date Validation Rules
        - End date must be strictly after start date
        - Maximum date range: less than 1 year
        - Dates must be in ISO format (YYYY-MM-DD)

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            body: Performance report request with date range and optional filters
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/wsr/attribution/performance-report"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[WsrReportRequest | WsrReportRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WsrPerformanceReportResponse],
            error_mapper=get_wsr_performance_report_error_mapper,
            request_options=request_options,
        )

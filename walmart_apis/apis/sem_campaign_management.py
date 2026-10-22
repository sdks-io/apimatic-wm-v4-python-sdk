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
from ..errors.create_campaign_error import CreateCampaignErrorBody, create_campaign_error_mapper
from ..errors.delete_campaign_error import DeleteCampaignErrorBody, delete_campaign_error_mapper
from ..errors.get_campaign_details_error import GetCampaignDetailsErrorBody, get_campaign_details_error_mapper
from ..errors.search_campaign_recommendations_error import (
    SearchCampaignRecommendationsErrorBody,
    search_campaign_recommendations_error_mapper,
)
from ..errors.stop_campaign_error import StopCampaignErrorBody, stop_campaign_error_mapper
from ..errors.update_campaign_error import UpdateCampaignErrorBody, update_campaign_error_mapper
from ..models.campaign_recommendations_search_request import (
    CampaignRecommendationsSearchRequest,
    CampaignRecommendationsSearchRequestDict,
)
from ..models.campaign_recommendations_search_response import CampaignRecommendationsSearchResponse
from ..models.enums.accept import Accept, AcceptOrStr
from ..models.enums.wm_global_version import WmGlobalVersion, WmGlobalVersionOrStr
from ..models.enums.wm_market import WmMarket, WmMarketOrStr
from ..models.sem_campaign import SemCampaign
from ..models.sem_campaign_create_request import SemCampaignCreateRequest, SemCampaignCreateRequestDict
from ..models.sem_campaign_response import SemCampaignResponse
from ..models.sem_campaign_update_request import SemCampaignUpdateRequest, SemCampaignUpdateRequestDict
from ..server.server import Server


class SemCampaignManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SemCampaignManagementWithRawResponse(client, server, auth)

    def create_campaign(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignCreateRequest | SemCampaignCreateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to create a new campaign by providing the required details in the request. Upon
        successful creation, a unique campaign ID will be assigned to the newly created campaign for identification and
        management purposes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.create_campaign(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def delete_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to permanently remove an existing campaign from the system. Once deleted, the campaign
        and its unique ID will no longer be retrievable. The campaign's unique ID must be included in the request.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be deleted.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.delete_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_campaign_details(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaign:
        """This API allows you to retrieve detailed information about a specific campaign. Provide the campaign's unique
        ID in the request to fetch its attributes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose details are to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.get_campaign_details(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def search_campaign_recommendations(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CampaignRecommendationsSearchResponse:
        """Search for campaign-level recommendations to improve SEM campaign performance. Returns a paginated list of
        active campaigns for the authenticated seller, each enriched with actionable recommendations — including budget
        adjustments and bidding strategy optimizations — along with projected performance impact metrics (clicks,
        impressions, ad spend).<br><b style='color:green;'>Market availability: US only</b>

        ### Why this API matters SEM campaigns require continuous optimization to stay competitive. Budget constraints
        and suboptimal bidding strategies are the two most common reasons campaigns underperform. Without data-driven
        guidance, sellers either overspend without results or miss revenue opportunities by underspending.

        This API bridges that gap by surfacing **machine-generated recommendations** for each active campaign, complete
        with projected impact on clicks, impressions, and ad spend. Partners can integrate these recommendations into
        their dashboards and automation pipelines to:
        - **Increase ROAS**: Apply budget and bidding strategy recommendations to maximize return on ad spend
        - **Reduce wasted spend**: Identify campaigns where budget is being underutilized or misallocated
        - **Automate campaign tuning**: Build automated workflows that periodically fetch recommendations and apply them
            programmatically, reducing manual effort and reaction time
        - **Enable data-driven decisions**: Each recommendation includes three impact scenarios (recommended,
            conservative, aggressive) so sellers can choose the option that fits their risk tolerance

        ### Key use cases
        1. **Campaign Health Dashboard**: Display campaigns with pending recommendations, color-coded by type
            (``BUDGET`` vs ``BIDDING_STRATEGY``), with projected impact metrics
        2. **Automated Budget Optimizer**: Periodically poll this API and auto-apply budget recommendations that meet a
            minimum projected ROAS threshold
        3. **Bidding Strategy Advisor**: Surface bidding strategy change suggestions to sellers with before/after
            performance projections
        4. **Bulk Campaign Management**: Retrieve all recommendations across campaigns in a single paginated call,
            enabling batch review and bulk application of changes

        ### How it works The API returns only active campaigns that are eligible for recommendations. You can filter
        results using ``campaignIds`` or ``recommendationType`` (``BUDGET`` or ``BIDDING_STRATEGY``).

        ### Default behavior
        - When no request body is provided, the API defaults to ``offset=0``, ``limit=10``.
        - By default, the API returns recommendations for both ``BUDGET`` and ``BIDDING_STRATEGY``.
        - Results are not sorted by default; use the sort object to order by adspend.
        - Returns only **active campaigns** that have at least one pending recommendation
        - Results are not sorted by default; use the ``sort`` object to order by ``adspend``

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Description |
        |---------------------------|-------------------------------|----------------------------------------------------------|
        | ``campaignIds`` | Numeric string campaign IDs | Filter by specific campaign identifiers |
        | ``recommendationType`` | ``BUDGET``, ``BIDDING_STRATEGY`` | Filter by recommendation type |

        ### Sorting Results can be sorted using the ``sort`` object:

        | Sort Field | Supported Orders | Description |
        |------------|------------------|------------------------------------------|
        | ``adspend`` | ``ASC``, ``DESC`` | Sort campaigns by ad spend |

        ### Recommendation types
        | Type | Description |
        |--------------------|--------------------------------------------------------------------------|
        | ``BUDGET`` | Recommended total or daily budget adjustment to improve campaign reach |
        | ``BIDDING_STRATEGY`` | Recommended change to bidding strategy for better performance |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata (``pageNo``, ``pageSize``, ``totalCount``, ``totalPages``,
            ``hasNextPage``, ``hasPreviousPage``)
        - ``data``: Array of campaign-level suggestions. Each campaign includes current settings (bidding strategy,
            target ROAS, daily budget) and an array of ``campaignRecommendations`` with projected performance impact at
            three levels: recommended, minimum, and maximum.

        ### Performance impact projections Each recommendation includes a ``recommendedValueImpact`` object with up to
        three scenarios:
        - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
        - **minRecommendation**: A conservative lower-bound option (may be ``null`` if not applicable)
        - **maxRecommendation**: An aggressive upper-bound option

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination, sorting, and filters. Defaults to ``offset=0``, ``limit=10``
                with no filters and no sorting if body is absent.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Campaign recommendations retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters or malformed request body. Unauthorized - Missing,
                invalid, or expired bearer token. Forbidden - Seller does not have access to SEM advertising features.
                Unprocessable Entity - Request is malformed (For example, request body passed as string instead of JSON
                object). Rate limit exceeded - You have exceeded your API calls threshold. Internal server error -
                Unexpected server error. Service Unavailable - Service is temporarily unavailable. ``error`` is
                ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            self._with_raw_response.search_campaign_recommendations(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                accept=accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    def stop_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to stop an active campaign. Stopping a campaign does not delete it but prevents further
        actions. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be stopped.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.stop_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to modify an existing campaign's details and manage its associated items. You must
        provide the campaign's unique ID along with the necessary changes in the request. The specified updates will be
        applied while preserving the campaign's unique identifier.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be updated.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.update_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SemCampaignManagementWithRawResponse:
        return self._with_raw_response


class AsyncSemCampaignManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSemCampaignManagementWithRawResponse(client, server, auth)

    async def create_campaign(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignCreateRequest | SemCampaignCreateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to create a new campaign by providing the required details in the request. Upon
        successful creation, a unique campaign ID will be assigned to the newly created campaign for identification and
        management purposes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_campaign(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def delete_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to permanently remove an existing campaign from the system. Once deleted, the campaign
        and its unique ID will no longer be retrievable. The campaign's unique ID must be included in the request.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be deleted.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_campaign_details(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaign:
        """This API allows you to retrieve detailed information about a specific campaign. Provide the campaign's unique
        ID in the request to fetch its attributes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose details are to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_campaign_details(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def search_campaign_recommendations(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CampaignRecommendationsSearchResponse:
        """Search for campaign-level recommendations to improve SEM campaign performance. Returns a paginated list of
        active campaigns for the authenticated seller, each enriched with actionable recommendations — including budget
        adjustments and bidding strategy optimizations — along with projected performance impact metrics (clicks,
        impressions, ad spend).<br><b style='color:green;'>Market availability: US only</b>

        ### Why this API matters SEM campaigns require continuous optimization to stay competitive. Budget constraints
        and suboptimal bidding strategies are the two most common reasons campaigns underperform. Without data-driven
        guidance, sellers either overspend without results or miss revenue opportunities by underspending.

        This API bridges that gap by surfacing **machine-generated recommendations** for each active campaign, complete
        with projected impact on clicks, impressions, and ad spend. Partners can integrate these recommendations into
        their dashboards and automation pipelines to:
        - **Increase ROAS**: Apply budget and bidding strategy recommendations to maximize return on ad spend
        - **Reduce wasted spend**: Identify campaigns where budget is being underutilized or misallocated
        - **Automate campaign tuning**: Build automated workflows that periodically fetch recommendations and apply them
            programmatically, reducing manual effort and reaction time
        - **Enable data-driven decisions**: Each recommendation includes three impact scenarios (recommended,
            conservative, aggressive) so sellers can choose the option that fits their risk tolerance

        ### Key use cases
        1. **Campaign Health Dashboard**: Display campaigns with pending recommendations, color-coded by type
            (``BUDGET`` vs ``BIDDING_STRATEGY``), with projected impact metrics
        2. **Automated Budget Optimizer**: Periodically poll this API and auto-apply budget recommendations that meet a
            minimum projected ROAS threshold
        3. **Bidding Strategy Advisor**: Surface bidding strategy change suggestions to sellers with before/after
            performance projections
        4. **Bulk Campaign Management**: Retrieve all recommendations across campaigns in a single paginated call,
            enabling batch review and bulk application of changes

        ### How it works The API returns only active campaigns that are eligible for recommendations. You can filter
        results using ``campaignIds`` or ``recommendationType`` (``BUDGET`` or ``BIDDING_STRATEGY``).

        ### Default behavior
        - When no request body is provided, the API defaults to ``offset=0``, ``limit=10``.
        - By default, the API returns recommendations for both ``BUDGET`` and ``BIDDING_STRATEGY``.
        - Results are not sorted by default; use the sort object to order by adspend.
        - Returns only **active campaigns** that have at least one pending recommendation
        - Results are not sorted by default; use the ``sort`` object to order by ``adspend``

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Description |
        |---------------------------|-------------------------------|----------------------------------------------------------|
        | ``campaignIds`` | Numeric string campaign IDs | Filter by specific campaign identifiers |
        | ``recommendationType`` | ``BUDGET``, ``BIDDING_STRATEGY`` | Filter by recommendation type |

        ### Sorting Results can be sorted using the ``sort`` object:

        | Sort Field | Supported Orders | Description |
        |------------|------------------|------------------------------------------|
        | ``adspend`` | ``ASC``, ``DESC`` | Sort campaigns by ad spend |

        ### Recommendation types
        | Type | Description |
        |--------------------|--------------------------------------------------------------------------|
        | ``BUDGET`` | Recommended total or daily budget adjustment to improve campaign reach |
        | ``BIDDING_STRATEGY`` | Recommended change to bidding strategy for better performance |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata (``pageNo``, ``pageSize``, ``totalCount``, ``totalPages``,
            ``hasNextPage``, ``hasPreviousPage``)
        - ``data``: Array of campaign-level suggestions. Each campaign includes current settings (bidding strategy,
            target ROAS, daily budget) and an array of ``campaignRecommendations`` with projected performance impact at
            three levels: recommended, minimum, and maximum.

        ### Performance impact projections Each recommendation includes a ``recommendedValueImpact`` object with up to
        three scenarios:
        - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
        - **minRecommendation**: A conservative lower-bound option (may be ``null`` if not applicable)
        - **maxRecommendation**: An aggressive upper-bound option

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination, sorting, and filters. Defaults to ``offset=0``, ``limit=10``
                with no filters and no sorting if body is absent.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Campaign recommendations retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters or malformed request body. Unauthorized - Missing,
                invalid, or expired bearer token. Forbidden - Seller does not have access to SEM advertising features.
                Unprocessable Entity - Request is malformed (For example, request body passed as string instead of JSON
                object). Rate limit exceeded - You have exceeded your API calls threshold. Internal server error -
                Unexpected server error. Service Unavailable - Service is temporarily unavailable. ``error`` is
                ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            await self._with_raw_response.search_campaign_recommendations(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                accept=accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    async def stop_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to stop an active campaign. Stopping a campaign does not delete it but prevents further
        actions. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be stopped.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.stop_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignResponse:
        """This API allows you to modify an existing campaign's details and manage its associated items. You must
        provide the campaign's unique ID along with the necessary changes in the request. The specified updates will be
        applied while preserving the campaign's unique identifier.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be updated.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_campaign(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSemCampaignManagementWithRawResponse:
        return self._with_raw_response


class SemCampaignManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_campaign(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignCreateRequest | SemCampaignCreateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, CreateCampaignErrorBody]:
        """This API allows you to create a new campaign by providing the required details in the request. Upon
        successful creation, a unique campaign ID will be assigned to the newly created campaign for identification and
        management purposes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemCampaignCreateRequest | SemCampaignCreateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaignResponse],
            error_mapper=create_campaign_error_mapper,
            request_options=request_options,
        )

    def delete_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, DeleteCampaignErrorBody]:
        """This API allows you to permanently remove an existing campaign from the system. Once deleted, the campaign
        and its unique ID will no longer be retrievable. The campaign's unique ID must be included in the request.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be deleted.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaignResponse],
            error_mapper=delete_campaign_error_mapper,
            request_options=request_options,
        )

    def get_campaign_details(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaign, GetCampaignDetailsErrorBody]:
        """This API allows you to retrieve detailed information about a specific campaign. Provide the campaign's unique
        ID in the request to fetch its attributes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose details are to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaign],
            error_mapper=get_campaign_details_error_mapper,
            request_options=request_options,
        )

    def search_campaign_recommendations(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CampaignRecommendationsSearchResponse, SearchCampaignRecommendationsErrorBody]:
        """Search for campaign-level recommendations to improve SEM campaign performance. Returns a paginated list of
        active campaigns for the authenticated seller, each enriched with actionable recommendations — including budget
        adjustments and bidding strategy optimizations — along with projected performance impact metrics (clicks,
        impressions, ad spend).<br><b style='color:green;'>Market availability: US only</b>

        ### Why this API matters SEM campaigns require continuous optimization to stay competitive. Budget constraints
        and suboptimal bidding strategies are the two most common reasons campaigns underperform. Without data-driven
        guidance, sellers either overspend without results or miss revenue opportunities by underspending.

        This API bridges that gap by surfacing **machine-generated recommendations** for each active campaign, complete
        with projected impact on clicks, impressions, and ad spend. Partners can integrate these recommendations into
        their dashboards and automation pipelines to:
        - **Increase ROAS**: Apply budget and bidding strategy recommendations to maximize return on ad spend
        - **Reduce wasted spend**: Identify campaigns where budget is being underutilized or misallocated
        - **Automate campaign tuning**: Build automated workflows that periodically fetch recommendations and apply them
            programmatically, reducing manual effort and reaction time
        - **Enable data-driven decisions**: Each recommendation includes three impact scenarios (recommended,
            conservative, aggressive) so sellers can choose the option that fits their risk tolerance

        ### Key use cases
        1. **Campaign Health Dashboard**: Display campaigns with pending recommendations, color-coded by type
            (``BUDGET`` vs ``BIDDING_STRATEGY``), with projected impact metrics
        2. **Automated Budget Optimizer**: Periodically poll this API and auto-apply budget recommendations that meet a
            minimum projected ROAS threshold
        3. **Bidding Strategy Advisor**: Surface bidding strategy change suggestions to sellers with before/after
            performance projections
        4. **Bulk Campaign Management**: Retrieve all recommendations across campaigns in a single paginated call,
            enabling batch review and bulk application of changes

        ### How it works The API returns only active campaigns that are eligible for recommendations. You can filter
        results using ``campaignIds`` or ``recommendationType`` (``BUDGET`` or ``BIDDING_STRATEGY``).

        ### Default behavior
        - When no request body is provided, the API defaults to ``offset=0``, ``limit=10``.
        - By default, the API returns recommendations for both ``BUDGET`` and ``BIDDING_STRATEGY``.
        - Results are not sorted by default; use the sort object to order by adspend.
        - Returns only **active campaigns** that have at least one pending recommendation
        - Results are not sorted by default; use the ``sort`` object to order by ``adspend``

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Description |
        |---------------------------|-------------------------------|----------------------------------------------------------|
        | ``campaignIds`` | Numeric string campaign IDs | Filter by specific campaign identifiers |
        | ``recommendationType`` | ``BUDGET``, ``BIDDING_STRATEGY`` | Filter by recommendation type |

        ### Sorting Results can be sorted using the ``sort`` object:

        | Sort Field | Supported Orders | Description |
        |------------|------------------|------------------------------------------|
        | ``adspend`` | ``ASC``, ``DESC`` | Sort campaigns by ad spend |

        ### Recommendation types
        | Type | Description |
        |--------------------|--------------------------------------------------------------------------|
        | ``BUDGET`` | Recommended total or daily budget adjustment to improve campaign reach |
        | ``BIDDING_STRATEGY`` | Recommended change to bidding strategy for better performance |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata (``pageNo``, ``pageSize``, ``totalCount``, ``totalPages``,
            ``hasNextPage``, ``hasPreviousPage``)
        - ``data``: Array of campaign-level suggestions. Each campaign includes current settings (bidding strategy,
            target ROAS, daily budget) and an array of ``campaignRecommendations`` with projected performance impact at
            three levels: recommended, minimum, and maximum.

        ### Performance impact projections Each recommendation includes a ``recommendedValueImpact`` object with up to
        three scenarios:
        - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
        - **minRecommendation**: A conservative lower-bound option (may be ``null`` if not applicable)
        - **maxRecommendation**: An aggressive upper-bound option

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination, sorting, and filters. Defaults to ``offset=0``, ``limit=10``
                with no filters and no sorting if body is absent.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/recommendations/search"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[AcceptOrStr]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[CampaignRecommendationsSearchResponse],
            error_mapper=search_campaign_recommendations_error_mapper,
            request_options=request_options,
        )

    def stop_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, StopCampaignErrorBody]:
        """This API allows you to stop an active campaign. Stopping a campaign does not delete it but prevents further
        actions. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be stopped.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}/stop"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaignResponse],
            error_mapper=stop_campaign_error_mapper,
            request_options=request_options,
        )

    def update_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, UpdateCampaignErrorBody]:
        """This API allows you to modify an existing campaign's details and manage its associated items. You must
        provide the campaign's unique ID along with the necessary changes in the request. The specified updates will be
        applied while preserving the campaign's unique identifier.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be updated.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemCampaignUpdateRequest | SemCampaignUpdateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaignResponse],
            error_mapper=update_campaign_error_mapper,
            request_options=request_options,
        )


class AsyncSemCampaignManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_campaign(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignCreateRequest | SemCampaignCreateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, CreateCampaignErrorBody]:
        """This API allows you to create a new campaign by providing the required details in the request. Upon
        successful creation, a unique campaign ID will be assigned to the newly created campaign for identification and
        management purposes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemCampaignCreateRequest | SemCampaignCreateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaignResponse],
            error_mapper=create_campaign_error_mapper,
            request_options=request_options,
        )

    async def delete_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, DeleteCampaignErrorBody]:
        """This API allows you to permanently remove an existing campaign from the system. Once deleted, the campaign
        and its unique ID will no longer be retrievable. The campaign's unique ID must be included in the request.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be deleted.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaignResponse],
            error_mapper=delete_campaign_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_details(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaign, GetCampaignDetailsErrorBody]:
        """This API allows you to retrieve detailed information about a specific campaign. Provide the campaign's unique
        ID in the request to fetch its attributes.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose details are to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaign],
            error_mapper=get_campaign_details_error_mapper,
            request_options=request_options,
        )

    async def search_campaign_recommendations(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CampaignRecommendationsSearchResponse, SearchCampaignRecommendationsErrorBody]:
        """Search for campaign-level recommendations to improve SEM campaign performance. Returns a paginated list of
        active campaigns for the authenticated seller, each enriched with actionable recommendations — including budget
        adjustments and bidding strategy optimizations — along with projected performance impact metrics (clicks,
        impressions, ad spend).<br><b style='color:green;'>Market availability: US only</b>

        ### Why this API matters SEM campaigns require continuous optimization to stay competitive. Budget constraints
        and suboptimal bidding strategies are the two most common reasons campaigns underperform. Without data-driven
        guidance, sellers either overspend without results or miss revenue opportunities by underspending.

        This API bridges that gap by surfacing **machine-generated recommendations** for each active campaign, complete
        with projected impact on clicks, impressions, and ad spend. Partners can integrate these recommendations into
        their dashboards and automation pipelines to:
        - **Increase ROAS**: Apply budget and bidding strategy recommendations to maximize return on ad spend
        - **Reduce wasted spend**: Identify campaigns where budget is being underutilized or misallocated
        - **Automate campaign tuning**: Build automated workflows that periodically fetch recommendations and apply them
            programmatically, reducing manual effort and reaction time
        - **Enable data-driven decisions**: Each recommendation includes three impact scenarios (recommended,
            conservative, aggressive) so sellers can choose the option that fits their risk tolerance

        ### Key use cases
        1. **Campaign Health Dashboard**: Display campaigns with pending recommendations, color-coded by type
            (``BUDGET`` vs ``BIDDING_STRATEGY``), with projected impact metrics
        2. **Automated Budget Optimizer**: Periodically poll this API and auto-apply budget recommendations that meet a
            minimum projected ROAS threshold
        3. **Bidding Strategy Advisor**: Surface bidding strategy change suggestions to sellers with before/after
            performance projections
        4. **Bulk Campaign Management**: Retrieve all recommendations across campaigns in a single paginated call,
            enabling batch review and bulk application of changes

        ### How it works The API returns only active campaigns that are eligible for recommendations. You can filter
        results using ``campaignIds`` or ``recommendationType`` (``BUDGET`` or ``BIDDING_STRATEGY``).

        ### Default behavior
        - When no request body is provided, the API defaults to ``offset=0``, ``limit=10``.
        - By default, the API returns recommendations for both ``BUDGET`` and ``BIDDING_STRATEGY``.
        - Results are not sorted by default; use the sort object to order by adspend.
        - Returns only **active campaigns** that have at least one pending recommendation
        - Results are not sorted by default; use the ``sort`` object to order by ``adspend``

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Description |
        |---------------------------|-------------------------------|----------------------------------------------------------|
        | ``campaignIds`` | Numeric string campaign IDs | Filter by specific campaign identifiers |
        | ``recommendationType`` | ``BUDGET``, ``BIDDING_STRATEGY`` | Filter by recommendation type |

        ### Sorting Results can be sorted using the ``sort`` object:

        | Sort Field | Supported Orders | Description |
        |------------|------------------|------------------------------------------|
        | ``adspend`` | ``ASC``, ``DESC`` | Sort campaigns by ad spend |

        ### Recommendation types
        | Type | Description |
        |--------------------|--------------------------------------------------------------------------|
        | ``BUDGET`` | Recommended total or daily budget adjustment to improve campaign reach |
        | ``BIDDING_STRATEGY`` | Recommended change to bidding strategy for better performance |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata (``pageNo``, ``pageSize``, ``totalCount``, ``totalPages``,
            ``hasNextPage``, ``hasPreviousPage``)
        - ``data``: Array of campaign-level suggestions. Each campaign includes current settings (bidding strategy,
            target ROAS, daily budget) and an array of ``campaignRecommendations`` with projected performance impact at
            three levels: recommended, minimum, and maximum.

        ### Performance impact projections Each recommendation includes a ``recommendedValueImpact`` object with up to
        three scenarios:
        - **recommended**: The optimal suggested value (marked ``isRecommended: true``)
        - **minRecommendation**: A conservative lower-bound option (may be ``null`` if not applicable)
        - **maxRecommendation**: An aggressive upper-bound option

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination, sorting, and filters. Defaults to ``offset=0``, ``limit=10``
                with no filters and no sorting if body is absent.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/recommendations/search"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[AcceptOrStr]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[CampaignRecommendationsSearchResponse],
            error_mapper=search_campaign_recommendations_error_mapper,
            request_options=request_options,
        )

    async def stop_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, StopCampaignErrorBody]:
        """This API allows you to stop an active campaign. Stopping a campaign does not delete it but prevents further
        actions. The campaign's unique ID must be included in the request.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be stopped.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}/stop"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaignResponse],
            error_mapper=stop_campaign_error_mapper,
            request_options=request_options,
        )

    async def update_campaign(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignResponse, UpdateCampaignErrorBody]:
        """This API allows you to modify an existing campaign's details and manage its associated items. You must
        provide the campaign's unique ID along with the necessary changes in the request. The specified updates will be
        applied while preserving the campaign's unique identifier.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            campaign_id: Campaign ID of the campaign to be updated.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            body: Request Payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemCampaignUpdateRequest | SemCampaignUpdateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaignResponse],
            error_mapper=update_campaign_error_mapper,
            request_options=request_options,
        )

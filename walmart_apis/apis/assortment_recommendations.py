from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_assortment_recommendation_trends_error import (
    GetAssortmentRecommendationTrendsErrorBody,
    get_assortment_recommendation_trends_error_mapper,
)
from ..errors.get_assortment_recommendation_variants_error import (
    GetAssortmentRecommendationVariantsErrorBody,
    get_assortment_recommendation_variants_error_mapper,
)
from ..errors.get_assortment_recommendations_error import (
    GetAssortmentRecommendationsErrorBody,
    get_assortment_recommendations_error_mapper,
)
from ..errors.get_categorization_details_of_assortment_recommendations_error import (
    GetCategorizationDetailsOfAssortmentRecommendationsErrorBody,
    get_categorization_details_of_assortment_recommendations_error_mapper,
)
from ..errors.reject_assortment_recommendations_error import (
    RejectAssortmentRecommendationsErrorBody,
    reject_assortment_recommendations_error_mapper,
)
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.v3_growth_assortment_recommendations_categorization_counts_request import (
    V3GrowthAssortmentRecommendationsCategorizationCountsRequest,
    V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict,
)
from ..models.v3_growth_assortment_recommendations_categorization_counts_response import (
    V3GrowthAssortmentRecommendationsCategorizationCountsResponse,
)
from ..models.v3_growth_assortment_recommendations_rejections_request import (
    V3GrowthAssortmentRecommendationsRejectionsRequest,
    V3GrowthAssortmentRecommendationsRejectionsRequestDict,
)
from ..models.v3_growth_assortment_recommendations_rejections_response import (
    V3GrowthAssortmentRecommendationsRejectionsResponse,
)
from ..models.v3_growth_assortment_recommendations_request import (
    V3GrowthAssortmentRecommendationsRequest,
    V3GrowthAssortmentRecommendationsRequestDict,
)
from ..models.v3_growth_assortment_recommendations_response import V3GrowthAssortmentRecommendationsResponse
from ..models.v3_growth_assortment_recommendations_trends_response import (
    V3GrowthAssortmentRecommendationsTrendsResponse,
)
from ..models.v3_growth_assortment_recommendations_variants_response import (
    V3GrowthAssortmentRecommendationsVariantsResponse,
)
from ..server.server import Server


class AssortmentRecommendations:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = AssortmentRecommendationsWithRawResponse(client, server)

    def get_assortment_recommendation_trends(
        self,
        recommendation_unique_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        trend_types: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsTrendsResponse:
        """You can fetch the monthly and weekly trends for both demand and price, for the assortment recommendations
        that are recommended for you. <br><b style='color:green;'>Market availability: US only</span></b>

        Args:
            recommendation_unique_id: Unique ID that is returned in the response of the get recommendations API or in
                the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            trend_types: Comma separated list of trends.<br><b style='color:green;'>Market availability: US
                only</span></b> | Attribute | Description | Data Type | | --- | ----------- | ------- | | PRICE_TRENDS |
                Indicates the price trends for the recommended item in the marketplace currency for rolling
                52-weeks/12-months. The data may not be available for all weeks/months. | string | | DEMAND_TRENDS |
                Indicates the demand trends for the recommended item for 52-weeks/12-months. | string |
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_assortment_recommendation_trends(
                recommendation_unique_id,
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                trend_types=trend_types,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_assortment_recommendation_variants(
        self,
        primary_variant_item_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsVariantsResponse:
        """You can fetch variant items corresponding to a recommended primary variant item. <br><b
        style='color:green;'>Market availability: US only</span></b>

        Args:
            primary_variant_item_id: Primary variant item ID that is returned in the response of get recommendations API
                or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            next_cursor: Used for pagination when more than 200 records are retrieved. The nextCursor value of the
                response includes a marker which needs to be passed in next call which retrieves the next page of
                results. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_assortment_recommendation_variants(
                primary_variant_item_id,
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                next_cursor=next_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsResponse:
        """You can fetch the list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can get the list of ITEM recommendations. You can apply filters to fetch selective item recommendations.
            <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_assortment_recommendations(
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_categorization_details_of_assortment_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3GrowthAssortmentRecommendationsCategorizationCountsRequest
            | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsCategorizationCountsResponse:
        """You can get the list of brands or categories associated with the items recommendations that are recommended
        for you.

        Using BRAND as a categorizationType
        * You can get the list of brands sorted by the number of item recommendations associated with it. This is then
            sorted in lexicographic order of brand name.

        Using CATEGORY as a categorizationType
        * You can get the list of categories sorted by the number of item recommendations associated with it. This is
            then sorted in lexicographic order of category name.
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs <br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID <br><b style='color:green;'>Market availability: US | CA |
                MX</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called <br><b style='color:green;'>Market
                availability: US | CA | MX</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1<br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel <br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_categorization_details_of_assortment_recommendations(
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

    def reject_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: (
            V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsRejectionsResponse:
        """You can reject a list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can reject specific item recommendations using the filterCriteria or by providing the list of
            itemRecommendationUniqueIds.
        * You will need to provide valid rejection code(s) while submitting the reject request. You are required to send
            the custom rejection message if the rejection code is OTHER_REASON
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.reject_assortment_recommendations(
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AssortmentRecommendationsWithRawResponse:
        return self._with_raw_response


class AsyncAssortmentRecommendations:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncAssortmentRecommendationsWithRawResponse(client, server)

    async def get_assortment_recommendation_trends(
        self,
        recommendation_unique_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        trend_types: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsTrendsResponse:
        """You can fetch the monthly and weekly trends for both demand and price, for the assortment recommendations
        that are recommended for you. <br><b style='color:green;'>Market availability: US only</span></b>

        Args:
            recommendation_unique_id: Unique ID that is returned in the response of the get recommendations API or in
                the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            trend_types: Comma separated list of trends.<br><b style='color:green;'>Market availability: US
                only</span></b> | Attribute | Description | Data Type | | --- | ----------- | ------- | | PRICE_TRENDS |
                Indicates the price trends for the recommended item in the marketplace currency for rolling
                52-weeks/12-months. The data may not be available for all weeks/months. | string | | DEMAND_TRENDS |
                Indicates the demand trends for the recommended item for 52-weeks/12-months. | string |
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_assortment_recommendation_trends(
                recommendation_unique_id,
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                trend_types=trend_types,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_assortment_recommendation_variants(
        self,
        primary_variant_item_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsVariantsResponse:
        """You can fetch variant items corresponding to a recommended primary variant item. <br><b
        style='color:green;'>Market availability: US only</span></b>

        Args:
            primary_variant_item_id: Primary variant item ID that is returned in the response of get recommendations API
                or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            next_cursor: Used for pagination when more than 200 records are retrieved. The nextCursor value of the
                response includes a marker which needs to be passed in next call which retrieves the next page of
                results. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_assortment_recommendation_variants(
                primary_variant_item_id,
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                next_cursor=next_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsResponse:
        """You can fetch the list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can get the list of ITEM recommendations. You can apply filters to fetch selective item recommendations.
            <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_assortment_recommendations(
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_categorization_details_of_assortment_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3GrowthAssortmentRecommendationsCategorizationCountsRequest
            | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsCategorizationCountsResponse:
        """You can get the list of brands or categories associated with the items recommendations that are recommended
        for you.

        Using BRAND as a categorizationType
        * You can get the list of brands sorted by the number of item recommendations associated with it. This is then
            sorted in lexicographic order of brand name.

        Using CATEGORY as a categorizationType
        * You can get the list of categories sorted by the number of item recommendations associated with it. This is
            then sorted in lexicographic order of category name.
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs <br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID <br><b style='color:green;'>Market availability: US | CA |
                MX</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called <br><b style='color:green;'>Market
                availability: US | CA | MX</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1<br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel <br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_categorization_details_of_assortment_recommendations(
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

    async def reject_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: (
            V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthAssortmentRecommendationsRejectionsResponse:
        """You can reject a list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can reject specific item recommendations using the filterCriteria or by providing the list of
            itemRecommendationUniqueIds.
        * You will need to provide valid rejection code(s) while submitting the reject request. You are required to send
            the custom rejection message if the rejection code is OTHER_REASON
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - Invalid Input Forbidden - Unsupported Market System Error ``error`` is
                ``ErrorResponse1 | V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.reject_assortment_recommendations(
                wm_global_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncAssortmentRecommendationsWithRawResponse:
        return self._with_raw_response


class AssortmentRecommendationsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_assortment_recommendation_trends(
        self,
        recommendation_unique_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        trend_types: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsTrendsResponse, GetAssortmentRecommendationTrendsErrorBody]:
        """You can fetch the monthly and weekly trends for both demand and price, for the assortment recommendations
        that are recommended for you. <br><b style='color:green;'>Market availability: US only</span></b>

        Args:
            recommendation_unique_id: Unique ID that is returned in the response of the get recommendations API or in
                the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            trend_types: Comma separated list of trends.<br><b style='color:green;'>Market availability: US
                only</span></b> | Attribute | Description | Data Type | | --- | ----------- | ------- | | PRICE_TRENDS |
                Indicates the price trends for the recommended item in the marketplace currency for rolling
                52-weeks/12-months. The data may not be available for all weeks/months. | string | | DEMAND_TRENDS |
                Indicates the demand trends for the recommended item for 52-weeks/12-months. | string |
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/growth/assortment/recommendations/trends"),
            query_params=[
                param[str]("recommendationUniqueId", recommendation_unique_id),
                param[str | None]("trendTypes", trend_types),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[V3GrowthAssortmentRecommendationsTrendsResponse],
            error_mapper=get_assortment_recommendation_trends_error_mapper,
            request_options=request_options,
        )

    def get_assortment_recommendation_variants(
        self,
        primary_variant_item_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsVariantsResponse, GetAssortmentRecommendationVariantsErrorBody]:
        """You can fetch variant items corresponding to a recommended primary variant item. <br><b
        style='color:green;'>Market availability: US only</span></b>

        Args:
            primary_variant_item_id: Primary variant item ID that is returned in the response of get recommendations API
                or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            next_cursor: Used for pagination when more than 200 records are retrieved. The nextCursor value of the
                response includes a marker which needs to be passed in next call which retrieves the next page of
                results. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/growth/assortment/recommendations/variants"),
            query_params=[
                param[str]("primaryVariantItemId", primary_variant_item_id),
                param[str | None]("nextCursor", next_cursor),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[V3GrowthAssortmentRecommendationsVariantsResponse],
            error_mapper=get_assortment_recommendation_variants_error_mapper,
            request_options=request_options,
        )

    def get_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsResponse, GetAssortmentRecommendationsErrorBody]:
        """You can fetch the list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can get the list of ITEM recommendations. You can apply filters to fetch selective item recommendations.
            <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/assortment/recommendations"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict](
                body
            ),
            decoder=json_decoder[V3GrowthAssortmentRecommendationsResponse],
            error_mapper=get_assortment_recommendations_error_mapper,
            request_options=request_options,
        )

    def get_categorization_details_of_assortment_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3GrowthAssortmentRecommendationsCategorizationCountsRequest
            | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V3GrowthAssortmentRecommendationsCategorizationCountsResponse,
        GetCategorizationDetailsOfAssortmentRecommendationsErrorBody,
    ]:
        """You can get the list of brands or categories associated with the items recommendations that are recommended
        for you.

        Using BRAND as a categorizationType
        * You can get the list of brands sorted by the number of item recommendations associated with it. This is then
            sorted in lexicographic order of brand name.

        Using CATEGORY as a categorizationType
        * You can get the list of categories sorted by the number of item recommendations associated with it. This is
            then sorted in lexicographic order of category name.
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs <br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID <br><b style='color:green;'>Market availability: US | CA |
                MX</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called <br><b style='color:green;'>Market
                availability: US | CA | MX</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1<br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel <br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/assortment/recommendations/categorization/counts"),
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
                    V3GrowthAssortmentRecommendationsCategorizationCountsRequest
                    | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
                )
            ](body),
            decoder=json_decoder[V3GrowthAssortmentRecommendationsCategorizationCountsResponse],
            error_mapper=get_categorization_details_of_assortment_recommendations_error_mapper,
            request_options=request_options,
        )

    def reject_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: (
            V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsRejectionsResponse, RejectAssortmentRecommendationsErrorBody]:
        """You can reject a list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can reject specific item recommendations using the filterCriteria or by providing the list of
            itemRecommendationUniqueIds.
        * You will need to provide valid rejection code(s) while submitting the reject request. You are required to send
            the custom rejection message if the rejection code is OTHER_REASON
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/growth/assortment/recommendations/rejections"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3GrowthAssortmentRecommendationsRejectionsRequest
                    | V3GrowthAssortmentRecommendationsRejectionsRequestDict
                )
            ](body),
            decoder=json_decoder[V3GrowthAssortmentRecommendationsRejectionsResponse],
            error_mapper=reject_assortment_recommendations_error_mapper,
            request_options=request_options,
        )


class AsyncAssortmentRecommendationsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_assortment_recommendation_trends(
        self,
        recommendation_unique_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        trend_types: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsTrendsResponse, GetAssortmentRecommendationTrendsErrorBody]:
        """You can fetch the monthly and weekly trends for both demand and price, for the assortment recommendations
        that are recommended for you. <br><b style='color:green;'>Market availability: US only</span></b>

        Args:
            recommendation_unique_id: Unique ID that is returned in the response of the get recommendations API or in
                the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            trend_types: Comma separated list of trends.<br><b style='color:green;'>Market availability: US
                only</span></b> | Attribute | Description | Data Type | | --- | ----------- | ------- | | PRICE_TRENDS |
                Indicates the price trends for the recommended item in the marketplace currency for rolling
                52-weeks/12-months. The data may not be available for all weeks/months. | string | | DEMAND_TRENDS |
                Indicates the demand trends for the recommended item for 52-weeks/12-months. | string |
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/growth/assortment/recommendations/trends"),
            query_params=[
                param[str]("recommendationUniqueId", recommendation_unique_id),
                param[str | None]("trendTypes", trend_types),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[V3GrowthAssortmentRecommendationsTrendsResponse],
            error_mapper=get_assortment_recommendation_trends_error_mapper,
            request_options=request_options,
        )

    async def get_assortment_recommendation_variants(
        self,
        primary_variant_item_id: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsVariantsResponse, GetAssortmentRecommendationVariantsErrorBody]:
        """You can fetch variant items corresponding to a recommended primary variant item. <br><b
        style='color:green;'>Market availability: US only</span></b>

        Args:
            primary_variant_item_id: Primary variant item ID that is returned in the response of get recommendations API
                or in the on-request bulk CSV file. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            next_cursor: Used for pagination when more than 200 records are retrieved. The nextCursor value of the
                response includes a marker which needs to be passed in next call which retrieves the next page of
                results. <br><b style='color:green;'>Market availability: US only</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/growth/assortment/recommendations/variants"),
            query_params=[
                param[str]("primaryVariantItemId", primary_variant_item_id),
                param[str | None]("nextCursor", next_cursor),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[V3GrowthAssortmentRecommendationsVariantsResponse],
            error_mapper=get_assortment_recommendation_variants_error_mapper,
            request_options=request_options,
        )

    async def get_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsResponse, GetAssortmentRecommendationsErrorBody]:
        """You can fetch the list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can get the list of ITEM recommendations. You can apply filters to fetch selective item recommendations.
            <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/assortment/recommendations"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict](
                body
            ),
            decoder=async_json_decoder[V3GrowthAssortmentRecommendationsResponse],
            error_mapper=get_assortment_recommendations_error_mapper,
            request_options=request_options,
        )

    async def get_categorization_details_of_assortment_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3GrowthAssortmentRecommendationsCategorizationCountsRequest
            | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V3GrowthAssortmentRecommendationsCategorizationCountsResponse,
        GetCategorizationDetailsOfAssortmentRecommendationsErrorBody,
    ]:
        """You can get the list of brands or categories associated with the items recommendations that are recommended
        for you.

        Using BRAND as a categorizationType
        * You can get the list of brands sorted by the number of item recommendations associated with it. This is then
            sorted in lexicographic order of brand name.

        Using CATEGORY as a categorizationType
        * You can get the list of categories sorted by the number of item recommendations associated with it. This is
            then sorted in lexicographic order of category name.
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs <br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID <br><b style='color:green;'>Market availability: US | CA |
                MX</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called <br><b style='color:green;'>Market
                availability: US | CA | MX</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1<br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel <br><b
                style='color:green;'>Market availability: US | CA | MX</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/assortment/recommendations/categorization/counts"),
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
                    V3GrowthAssortmentRecommendationsCategorizationCountsRequest
                    | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict
                )
            ](body),
            decoder=async_json_decoder[V3GrowthAssortmentRecommendationsCategorizationCountsResponse],
            error_mapper=get_categorization_details_of_assortment_recommendations_error_mapper,
            request_options=request_options,
        )

    async def reject_assortment_recommendations(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: (
            V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthAssortmentRecommendationsRejectionsResponse, RejectAssortmentRecommendationsErrorBody]:
        """You can reject a list of recommendations that are recommended for you.

        Using ITEM as a recommendationType,
        * You can reject specific item recommendations using the filterCriteria or by providing the list of
            itemRecommendationUniqueIds.
        * You will need to provide valid rejection code(s) while submitting the reject request. You are required to send
            the custom rejection message if the rejection code is OTHER_REASON
        <br><b style='color:green;'>Market availability: US | CA | MX</span></b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/growth/assortment/recommendations/rejections"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3GrowthAssortmentRecommendationsRejectionsRequest
                    | V3GrowthAssortmentRecommendationsRejectionsRequestDict
                )
            ](body),
            decoder=async_json_decoder[V3GrowthAssortmentRecommendationsRejectionsResponse],
            error_mapper=reject_assortment_recommendations_error_mapper,
            request_options=request_options,
        )

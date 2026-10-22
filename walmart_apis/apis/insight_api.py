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
from ..errors.get_categories_list_error import GetCategoriesListErrorBody, get_categories_list_error_mapper
from ..errors.get_listing_quality_score_error import (
    GetListingQualityScoreErrorBody,
    get_listing_quality_score_error_mapper,
)
from ..errors.get_pro_seller_badge_info_error import (
    GetProSellerBadgeInfoErrorBody,
    get_pro_seller_badge_info_error_mapper,
)
from ..errors.get_seller_incentives_info_error import (
    GetSellerIncentivesInfoErrorBody,
    get_seller_incentives_info_error_mapper,
)
from ..errors.get_unpublished_item_count_error import (
    GetUnpublishedItemCountErrorBody,
    get_unpublished_item_count_error_mapper,
)
from ..errors.get_unpublished_items_error import GetUnpublishedItemsErrorBody, get_unpublished_items_error_mapper
from ..errors.items_details_for_listing_error import (
    ItemsDetailsForListingErrorBody,
    items_details_for_listing_error_mapper,
)
from ..models.enums.type3 import Type3OrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.v3_insights_items_listing_quality_count_response import V3InsightsItemsListingQualityCountResponse
from ..models.v3_insights_items_listing_quality_items_request import (
    V3InsightsItemsListingQualityItemsRequest,
    V3InsightsItemsListingQualityItemsRequestDict,
)
from ..models.v3_insights_items_listing_quality_items_response import V3InsightsItemsListingQualityItemsResponse
from ..models.v3_insights_items_listing_quality_score_response import V3InsightsItemsListingQualityScoreResponse
from ..models.v3_insights_items_unpublished_counts_response import V3InsightsItemsUnpublishedCountsResponse
from ..models.v3_insights_items_unpublished_items_response import V3InsightsItemsUnpublishedItemsResponse
from ..models.v3_insights_prosellerbadge_response import V3InsightsProsellerbadgeResponse
from ..models.v3_insights_seller_incentives_response import V3InsightsSellerIncentivesResponse
from ..server.server import Server


class InsightApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InsightApiWithRawResponse(client, server, auth)

    def get_categories_list(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = True,
        wfs_flag: bool | None = None,
        has_issue: int | None = 0,
        type_: Type3OrStr | None = None,
        in_demand_indicator: bool | None = None,
        limit: int | None = None,
        offset: int | None = 0,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityCountResponse:
        """Get a list of all item categories that have items with listing quality issues or brands for a seller.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US only</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            has_issue: Specify whether or not to include items that have issues in the Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            type_: Specify whether to get item count by brand or category.If not specified, category is the default
                value.<br><b style='color:green;'>Market availability: US only</b>
            in_demand_indicator: Specify whether to get item count by customer favorite.<br><b
                style='color:green;'>Market availability: US only</b>
            limit: Specify the number of items to return. The default is 100, with a maximum value of 1000..<br><b
                style='color:green;'>Market availability: US only</b>
            offset: Specify the offset of item list to be returned.<br><b style='color:green;'>Market availability: US
                only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation<br><b style='color:green;'>Market availability: US only</b>

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsItemsListingQualityCount400Error1 | V3Token400Error1 |
                V3InsightsItemsListingQualityCount500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_categories_list(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                view_trending_items=view_trending_items,
                wfs_flag=wfs_flag,
                has_issue=has_issue,
                type_=type_,
                in_demand_indicator=in_demand_indicator,
                limit=limit,
                offset=offset,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_listing_quality_score(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = None,
        wfs_flag: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityScoreResponse:
        """Get the total Listing Quality Score for a seller's entire item catalog.<br><b style='color:green;'>Market
        availability: US | CA | MX</b>

        Args:
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsItemsListingQualityScore400Error1 | V3Token400Error1 |
                V3InsightsItemsListingQualityScore500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_listing_quality_score(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                view_trending_items=view_trending_items,
                wfs_flag=wfs_flag,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_pro_seller_badge_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsProsellerbadgeResponse:
        """The Pro Seller badge status will provide you with information regarding your current badge status as well as
        the progress you've made in meeting the criteria.<br><b style='color:green;'>Market availability: MX only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsProsellerbadge400Error1 | V3Token400Error1 | V3InsightsProsellerbadge500Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_pro_seller_badge_info(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_seller_incentives_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsSellerIncentivesResponse:
        """The Pro Seller Tier and Rewards Status API allows you to check your seller’s current tier status within the
        Pro Seller program, a three-tier incentive structure consisting of Rising, Advanced, and Pro Seller levels in US
        and a single-tier i.e Pro Seller in CA.<br><b style='color:green;'>Market availability: US | CA</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsSellerIncentives500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_seller_incentives_info(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_unpublished_item_count(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsUnpublishedCountsResponse:
        """This API allows you to get the count of unpublished items.<br><b style='color:green;'>Market availability: US
        | CA | MX</b>

        Args:
            from_date: Returns all unpublished items count with reason codes since the given date period<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsItemsUnpublishedCounts500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_unpublished_item_count(
                from_date,
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_unpublished_items(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        unpublished_reason_code: str | None = "all",
        limit: str | None = "20",
        offer_lifecycle_status: str | None = "all",
        market_trending: str | None = "true",
        items_with_inventory: str | None = "true",
        is_customer_favorite: bool | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsUnpublishedItemsResponse:
        """Get Unpublished Items<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            from_date: Returns all unpublished items since the given date<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            unpublished_reason_code: Unpublished reason code<br><b style='color:green;'>Market availability: US | CA |
                MX</b>
            limit: The number of items to be returned.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            offer_lifecycle_status: The lifecycle status of an item describes where the item listing is in the overall
                lifecycle. Examples of allowed values are ACTIVE , ARCHIVED, RETIRED.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            market_trending: Filter the item list to return only items that are trending on Walmart.com<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            items_with_inventory: Filter the item list to return only items that have inventory<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            is_customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer
                favorites are returned. When set to ``false``, only non-favorites are returned. If omitted, all items
                are returned.<br><b style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error Bad request ``error`` is
                ``V3Token400Error1 | V3InsightsItemsUnpublishedItems500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_unpublished_items(
                from_date,
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                unpublished_reason_code=unpublished_reason_code,
                limit=limit,
                offer_lifecycle_status=offer_lifecycle_status,
                market_trending=market_trending,
                items_with_inventory=items_with_inventory,
                is_customer_favorite=is_customer_favorite,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def items_details_for_listing(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict,
        *,
        limit: str | None = "200",
        next_cursor: str | None = None,
        offset: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityItemsResponse:
        """Get each item's listing quality details including: item quality score, offer score, content score and issues,
        and item performance.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            next_cursor: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: US
                only</b>
            offset: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: CA |
                MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsItemsListingQualityItems500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.items_details_for_listing(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                limit=limit,
                next_cursor=next_cursor,
                offset=offset,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> InsightApiWithRawResponse:
        return self._with_raw_response


class AsyncInsightApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInsightApiWithRawResponse(client, server, auth)

    async def get_categories_list(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = True,
        wfs_flag: bool | None = None,
        has_issue: int | None = 0,
        type_: Type3OrStr | None = None,
        in_demand_indicator: bool | None = None,
        limit: int | None = None,
        offset: int | None = 0,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityCountResponse:
        """Get a list of all item categories that have items with listing quality issues or brands for a seller.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US only</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            has_issue: Specify whether or not to include items that have issues in the Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            type_: Specify whether to get item count by brand or category.If not specified, category is the default
                value.<br><b style='color:green;'>Market availability: US only</b>
            in_demand_indicator: Specify whether to get item count by customer favorite.<br><b
                style='color:green;'>Market availability: US only</b>
            limit: Specify the number of items to return. The default is 100, with a maximum value of 1000..<br><b
                style='color:green;'>Market availability: US only</b>
            offset: Specify the offset of item list to be returned.<br><b style='color:green;'>Market availability: US
                only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation<br><b style='color:green;'>Market availability: US only</b>

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsItemsListingQualityCount400Error1 | V3Token400Error1 |
                V3InsightsItemsListingQualityCount500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_categories_list(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                view_trending_items=view_trending_items,
                wfs_flag=wfs_flag,
                has_issue=has_issue,
                type_=type_,
                in_demand_indicator=in_demand_indicator,
                limit=limit,
                offset=offset,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_listing_quality_score(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = None,
        wfs_flag: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityScoreResponse:
        """Get the total Listing Quality Score for a seller's entire item catalog.<br><b style='color:green;'>Market
        availability: US | CA | MX</b>

        Args:
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsItemsListingQualityScore400Error1 | V3Token400Error1 |
                V3InsightsItemsListingQualityScore500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_listing_quality_score(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                view_trending_items=view_trending_items,
                wfs_flag=wfs_flag,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_pro_seller_badge_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsProsellerbadgeResponse:
        """The Pro Seller badge status will provide you with information regarding your current badge status as well as
        the progress you've made in meeting the criteria.<br><b style='color:green;'>Market availability: MX only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3InsightsProsellerbadge400Error1 | V3Token400Error1 | V3InsightsProsellerbadge500Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_pro_seller_badge_info(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_seller_incentives_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsSellerIncentivesResponse:
        """The Pro Seller Tier and Rewards Status API allows you to check your seller’s current tier status within the
        Pro Seller program, a three-tier incentive structure consisting of Rising, Advanced, and Pro Seller levels in US
        and a single-tier i.e Pro Seller in CA.<br><b style='color:green;'>Market availability: US | CA</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsSellerIncentives500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_seller_incentives_info(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_unpublished_item_count(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsUnpublishedCountsResponse:
        """This API allows you to get the count of unpublished items.<br><b style='color:green;'>Market availability: US
        | CA | MX</b>

        Args:
            from_date: Returns all unpublished items count with reason codes since the given date period<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsItemsUnpublishedCounts500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_unpublished_item_count(
                from_date,
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_unpublished_items(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        unpublished_reason_code: str | None = "all",
        limit: str | None = "20",
        offer_lifecycle_status: str | None = "all",
        market_trending: str | None = "true",
        items_with_inventory: str | None = "true",
        is_customer_favorite: bool | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsUnpublishedItemsResponse:
        """Get Unpublished Items<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            from_date: Returns all unpublished items since the given date<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            unpublished_reason_code: Unpublished reason code<br><b style='color:green;'>Market availability: US | CA |
                MX</b>
            limit: The number of items to be returned.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            offer_lifecycle_status: The lifecycle status of an item describes where the item listing is in the overall
                lifecycle. Examples of allowed values are ACTIVE , ARCHIVED, RETIRED.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            market_trending: Filter the item list to return only items that are trending on Walmart.com<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            items_with_inventory: Filter the item list to return only items that have inventory<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            is_customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer
                favorites are returned. When set to ``false``, only non-favorites are returned. If omitted, all items
                are returned.<br><b style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error Bad request ``error`` is
                ``V3Token400Error1 | V3InsightsItemsUnpublishedItems500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_unpublished_items(
                from_date,
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                unpublished_reason_code=unpublished_reason_code,
                limit=limit,
                offer_lifecycle_status=offer_lifecycle_status,
                market_trending=market_trending,
                items_with_inventory=items_with_inventory,
                is_customer_favorite=is_customer_favorite,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def items_details_for_listing(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict,
        *,
        limit: str | None = "200",
        next_cursor: str | None = None,
        offset: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3InsightsItemsListingQualityItemsResponse:
        """Get each item's listing quality details including: item quality score, offer score, content score and issues,
        and item performance.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            next_cursor: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: US
                only</b>
            offset: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: CA |
                MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1
                | V3InsightsItemsListingQualityItems500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.items_details_for_listing(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                limit=limit,
                next_cursor=next_cursor,
                offset=offset,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncInsightApiWithRawResponse:
        return self._with_raw_response


class InsightApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_categories_list(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = True,
        wfs_flag: bool | None = None,
        has_issue: int | None = 0,
        type_: Type3OrStr | None = None,
        in_demand_indicator: bool | None = None,
        limit: int | None = None,
        offset: int | None = 0,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityCountResponse, GetCategoriesListErrorBody]:
        """Get a list of all item categories that have items with listing quality issues or brands for a seller.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US only</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            has_issue: Specify whether or not to include items that have issues in the Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            type_: Specify whether to get item count by brand or category.If not specified, category is the default
                value.<br><b style='color:green;'>Market availability: US only</b>
            in_demand_indicator: Specify whether to get item count by customer favorite.<br><b
                style='color:green;'>Market availability: US only</b>
            limit: Specify the number of items to return. The default is 100, with a maximum value of 1000..<br><b
                style='color:green;'>Market availability: US only</b>
            offset: Specify the offset of item list to be returned.<br><b style='color:green;'>Market availability: US
                only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/listingQuality/count"),
            query_params=[
                param[bool | None]("viewTrendingItems", view_trending_items),
                param[bool | None]("wfsFlag", wfs_flag),
                param[int | None]("hasIssue", has_issue),
                param[Type3OrStr | None]("type", type_),
                param[bool | None]("inDemandIndicator", in_demand_indicator),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsItemsListingQualityCountResponse],
            error_mapper=get_categories_list_error_mapper,
            request_options=request_options,
        )

    def get_listing_quality_score(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = None,
        wfs_flag: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityScoreResponse, GetListingQualityScoreErrorBody]:
        """Get the total Listing Quality Score for a seller's entire item catalog.<br><b style='color:green;'>Market
        availability: US | CA | MX</b>

        Args:
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/listingQuality/score"),
            query_params=[
                param[bool | None]("viewTrendingItems", view_trending_items), param[str | None]("wfsFlag", wfs_flag)
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsItemsListingQualityScoreResponse],
            error_mapper=get_listing_quality_score_error_mapper,
            request_options=request_options,
        )

    def get_pro_seller_badge_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsProsellerbadgeResponse, GetProSellerBadgeInfoErrorBody]:
        """The Pro Seller badge status will provide you with information regarding your current badge status as well as
        the progress you've made in meeting the criteria.<br><b style='color:green;'>Market availability: MX only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/prosellerbadge"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsProsellerbadgeResponse],
            error_mapper=get_pro_seller_badge_info_error_mapper,
            request_options=request_options,
        )

    def get_seller_incentives_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsSellerIncentivesResponse, GetSellerIncentivesInfoErrorBody]:
        """The Pro Seller Tier and Rewards Status API allows you to check your seller’s current tier status within the
        Pro Seller program, a three-tier incentive structure consisting of Rising, Advanced, and Pro Seller levels in US
        and a single-tier i.e Pro Seller in CA.<br><b style='color:green;'>Market availability: US | CA</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/sellerIncentives"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsSellerIncentivesResponse],
            error_mapper=get_seller_incentives_info_error_mapper,
            request_options=request_options,
        )

    def get_unpublished_item_count(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsUnpublishedCountsResponse, GetUnpublishedItemCountErrorBody]:
        """This API allows you to get the count of unpublished items.<br><b style='color:green;'>Market availability: US
        | CA | MX</b>

        Args:
            from_date: Returns all unpublished items count with reason codes since the given date period<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/unpublished/counts"),
            query_params=[param[str]("fromDate", from_date)],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsItemsUnpublishedCountsResponse],
            error_mapper=get_unpublished_item_count_error_mapper,
            request_options=request_options,
        )

    def get_unpublished_items(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        unpublished_reason_code: str | None = "all",
        limit: str | None = "20",
        offer_lifecycle_status: str | None = "all",
        market_trending: str | None = "true",
        items_with_inventory: str | None = "true",
        is_customer_favorite: bool | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsUnpublishedItemsResponse, GetUnpublishedItemsErrorBody]:
        """Get Unpublished Items<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            from_date: Returns all unpublished items since the given date<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            unpublished_reason_code: Unpublished reason code<br><b style='color:green;'>Market availability: US | CA |
                MX</b>
            limit: The number of items to be returned.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            offer_lifecycle_status: The lifecycle status of an item describes where the item listing is in the overall
                lifecycle. Examples of allowed values are ACTIVE , ARCHIVED, RETIRED.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            market_trending: Filter the item list to return only items that are trending on Walmart.com<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            items_with_inventory: Filter the item list to return only items that have inventory<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            is_customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer
                favorites are returned. When set to ``false``, only non-favorites are returned. If omitted, all items
                are returned.<br><b style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/unpublished/items"),
            query_params=[
                param[str]("fromDate", from_date),
                param[str | None]("unpublishedReasonCode", unpublished_reason_code),
                param[str | None]("limit", limit),
                param[str | None]("offerLifecycleStatus", offer_lifecycle_status),
                param[str | None]("marketTrending", market_trending),
                param[str | None]("itemsWithInventory", items_with_inventory),
                param[bool | None]("isCustomerFavorite", is_customer_favorite),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsItemsUnpublishedItemsResponse],
            error_mapper=get_unpublished_items_error_mapper,
            request_options=request_options,
        )

    def items_details_for_listing(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict,
        *,
        limit: str | None = "200",
        next_cursor: str | None = None,
        offset: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityItemsResponse, ItemsDetailsForListingErrorBody]:
        """Get each item's listing quality details including: item quality score, offer score, content score and issues,
        and item performance.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            next_cursor: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: US
                only</b>
            offset: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: CA |
                MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/insights/items/listingQuality/items"),
            query_params=[
                param[str | None]("limit", limit),
                param[str | None]("nextCursor", next_cursor),
                param[str | None]("offset", offset),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3InsightsItemsListingQualityItemsResponse],
            error_mapper=items_details_for_listing_error_mapper,
            request_options=request_options,
        )


class AsyncInsightApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_categories_list(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = True,
        wfs_flag: bool | None = None,
        has_issue: int | None = 0,
        type_: Type3OrStr | None = None,
        in_demand_indicator: bool | None = None,
        limit: int | None = None,
        offset: int | None = 0,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityCountResponse, GetCategoriesListErrorBody]:
        """Get a list of all item categories that have items with listing quality issues or brands for a seller.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US only</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            has_issue: Specify whether or not to include items that have issues in the Listing Quality Score.<br><b
                style='color:green;'>Market availability: US only</b>
            type_: Specify whether to get item count by brand or category.If not specified, category is the default
                value.<br><b style='color:green;'>Market availability: US only</b>
            in_demand_indicator: Specify whether to get item count by customer favorite.<br><b
                style='color:green;'>Market availability: US only</b>
            limit: Specify the number of items to return. The default is 100, with a maximum value of 1000..<br><b
                style='color:green;'>Market availability: US only</b>
            offset: Specify the offset of item list to be returned.<br><b style='color:green;'>Market availability: US
                only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/listingQuality/count"),
            query_params=[
                param[bool | None]("viewTrendingItems", view_trending_items),
                param[bool | None]("wfsFlag", wfs_flag),
                param[int | None]("hasIssue", has_issue),
                param[Type3OrStr | None]("type", type_),
                param[bool | None]("inDemandIndicator", in_demand_indicator),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsItemsListingQualityCountResponse],
            error_mapper=get_categories_list_error_mapper,
            request_options=request_options,
        )

    async def get_listing_quality_score(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        view_trending_items: bool | None = None,
        wfs_flag: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityScoreResponse, GetListingQualityScoreErrorBody]:
        """Get the total Listing Quality Score for a seller's entire item catalog.<br><b style='color:green;'>Market
        availability: US | CA | MX</b>

        Args:
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            view_trending_items: Specify whether or not to include seller's items that are trending in the Listing
                Quality Score.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wfs_flag: Specify whether or not to include WFS-eligible items in the overall Listing Quality Score.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/listingQuality/score"),
            query_params=[
                param[bool | None]("viewTrendingItems", view_trending_items), param[str | None]("wfsFlag", wfs_flag)
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsItemsListingQualityScoreResponse],
            error_mapper=get_listing_quality_score_error_mapper,
            request_options=request_options,
        )

    async def get_pro_seller_badge_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsProsellerbadgeResponse, GetProSellerBadgeInfoErrorBody]:
        """The Pro Seller badge status will provide you with information regarding your current badge status as well as
        the progress you've made in meeting the criteria.<br><b style='color:green;'>Market availability: MX only</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/prosellerbadge"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsProsellerbadgeResponse],
            error_mapper=get_pro_seller_badge_info_error_mapper,
            request_options=request_options,
        )

    async def get_seller_incentives_info(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsSellerIncentivesResponse, GetSellerIncentivesInfoErrorBody]:
        """The Pro Seller Tier and Rewards Status API allows you to check your seller’s current tier status within the
        Pro Seller program, a three-tier incentive structure consisting of Rising, Advanced, and Pro Seller levels in US
        and a single-tier i.e Pro Seller in CA.<br><b style='color:green;'>Market availability: US | CA</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/sellerIncentives"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsSellerIncentivesResponse],
            error_mapper=get_seller_incentives_info_error_mapper,
            request_options=request_options,
        )

    async def get_unpublished_item_count(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsUnpublishedCountsResponse, GetUnpublishedItemCountErrorBody]:
        """This API allows you to get the count of unpublished items.<br><b style='color:green;'>Market availability: US
        | CA | MX</b>

        Args:
            from_date: Returns all unpublished items count with reason codes since the given date period<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/unpublished/counts"),
            query_params=[param[str]("fromDate", from_date)],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsItemsUnpublishedCountsResponse],
            error_mapper=get_unpublished_item_count_error_mapper,
            request_options=request_options,
        )

    async def get_unpublished_items(
        self,
        from_date: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        *,
        unpublished_reason_code: str | None = "all",
        limit: str | None = "20",
        offer_lifecycle_status: str | None = "all",
        market_trending: str | None = "true",
        items_with_inventory: str | None = "true",
        is_customer_favorite: bool | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsUnpublishedItemsResponse, GetUnpublishedItemsErrorBody]:
        """Get Unpublished Items<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            from_date: Returns all unpublished items since the given date<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            unpublished_reason_code: Unpublished reason code<br><b style='color:green;'>Market availability: US | CA |
                MX</b>
            limit: The number of items to be returned.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            offer_lifecycle_status: The lifecycle status of an item describes where the item listing is in the overall
                lifecycle. Examples of allowed values are ACTIVE , ARCHIVED, RETIRED.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            market_trending: Filter the item list to return only items that are trending on Walmart.com<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            items_with_inventory: Filter the item list to return only items that have inventory<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            is_customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer
                favorites are returned. When set to ``false``, only non-favorites are returned. If omitted, all items
                are returned.<br><b style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/insights/items/unpublished/items"),
            query_params=[
                param[str]("fromDate", from_date),
                param[str | None]("unpublishedReasonCode", unpublished_reason_code),
                param[str | None]("limit", limit),
                param[str | None]("offerLifecycleStatus", offer_lifecycle_status),
                param[str | None]("marketTrending", market_trending),
                param[str | None]("itemsWithInventory", items_with_inventory),
                param[bool | None]("isCustomerFavorite", is_customer_favorite),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsItemsUnpublishedItemsResponse],
            error_mapper=get_unpublished_items_error_mapper,
            request_options=request_options,
        )

    async def items_details_for_listing(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict,
        *,
        limit: str | None = "200",
        next_cursor: str | None = None,
        offset: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3InsightsItemsListingQualityItemsResponse, ItemsDetailsForListingErrorBody]:
        """Get each item's listing quality details including: item quality score, offer score, content score and issues,
        and item performance.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_global_version: GLOBAL VERSION DEFAULT AS 3.1.<br><b style='color:green;'>Market availability:
                Global</span></b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name<br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.<br><b
                style='color:green;'>Market availability: US | CA | MX</b>
            next_cursor: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: US
                only</b>
            offset: Specify pagination for long list of items.<br><b style='color:green;'>Market availability: CA |
                MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/insights/items/listingQuality/items"),
            query_params=[
                param[str | None]("limit", limit),
                param[str | None]("nextCursor", next_cursor),
                param[str | None]("offset", offset),
            ],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3InsightsItemsListingQualityItemsResponse],
            error_mapper=items_details_for_listing_error_mapper,
            request_options=request_options,
        )

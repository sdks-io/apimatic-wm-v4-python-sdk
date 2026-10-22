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
from ..errors.create_strategy_error import CreateStrategyErrorBody, create_strategy_error_mapper
from ..errors.delete_strategy_error import DeleteStrategyErrorBody, delete_strategy_error_mapper
from ..errors.get_all_incentives_error import GetAllIncentivesErrorBody, get_all_incentives_error_mapper
from ..errors.get_repricer_feed_error import GetRepricerFeedErrorBody, get_repricer_feed_error_mapper
from ..errors.get_strategies_error import GetStrategiesErrorBody, get_strategies_error_mapper
from ..errors.price_and_promotion_bulk_uploads_error import (
    PriceAndPromotionBulkUploadsErrorBody,
    price_and_promotion_bulk_uploads_error_mapper,
)
from ..errors.reduced_referral_fee_incentives_enrollment_error import (
    ReducedReferralFeeIncentivesEnrollmentErrorBody,
    reduced_referral_fee_incentives_enrollment_error_mapper,
)
from ..errors.update_price_error import UpdatePriceErrorBody, update_price_error_mapper
from ..errors.update_strategy_error import UpdateStrategyErrorBody, update_strategy_error_mapper
from ..errors.update_walmart_funded_incentives_enrollment_status_error import (
    UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody,
    update_walmart_funded_incentives_enrollment_status_error_mapper,
)
from ..errors.walmart_funded_incentives_enrollment_error import (
    WalmartFundedIncentivesEnrollmentErrorBody,
    walmart_funded_incentives_enrollment_error_mapper,
)
from ..models.enums.feed_type2 import FeedType2OrStr
from ..models.enums.feed_type11 import FeedType11OrStr
from ..models.enums.feed_type21 import FeedType21OrStr
from ..models.enums.incentive_status import IncentiveStatus, IncentiveStatusOrStr
from ..models.enums.incentive_type import IncentiveTypeOrStr
from ..models.enums.order import Order, OrderOrStr
from ..models.enums.sort_by1 import SortBy1, SortBy1OrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_id import FeedId
from ..models.feed_id1 import FeedId1
from ..models.reject_recommendations_response_payload import RejectRecommendationsResponsePayload
from ..models.v3_feeds_feed_type_incentive_enrollment_request import (
    V3FeedsFeedTypeIncentiveEnrollmentRequest,
    V3FeedsFeedTypeIncentiveEnrollmentRequestDict,
)
from ..models.v3_feeds_feed_type_incentive_enrollment_response import V3FeedsFeedTypeIncentiveEnrollmentResponse
from ..models.v3_feeds_feed_type_price_and_promotion_request import (
    V3FeedsFeedTypePriceAndPromotionRequest,
    V3FeedsFeedTypePriceAndPromotionRequestDict,
)
from ..models.v3_feeds_feed_type_walmart_funded_incentives_enrollment_request import (
    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest,
    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict,
)
from ..models.v3_price_incentives_response import V3PriceIncentivesResponse
from ..models.v3_price_incentives_wfpreference_response import V3PriceIncentivesWfpreferenceResponse
from ..models.v3_price_request import V3PriceRequest, V3PriceRequestDict
from ..models.v3_price_response import V3PriceResponse
from ..models.v3_repricer_feeds_request import V3RepricerFeedsRequest, V3RepricerFeedsRequestDict
from ..models.v3_repricer_strategies_response import V3RepricerStrategiesResponse
from ..models.v3_repricer_strategy_request import V3RepricerStrategyRequest, V3RepricerStrategyRequestDict
from ..models.v3_repricer_strategy_request1 import V3RepricerStrategyRequest1, V3RepricerStrategyRequest1Dict
from ..models.v3_repricer_strategy_response import V3RepricerStrategyResponse
from ..models.v3_repricer_strategy_response2 import V3RepricerStrategyResponse2
from ..server.server import Server


class Prices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PricesWithRawResponse(client, server, auth)

    def create_strategy(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategyResponse2:
        """Creates a new strategy for the seller.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_strategy(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def delete_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """Deletes the strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.delete_strategy(
                strategy_collection_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_all_incentives(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE,
        limit: int | None = 25,
        offset: int | None = 0,
        sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE,
        sort_order: OrderOrStr | None = Order.DESC,
        incentive_type: IncentiveTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceIncentivesResponse:
        """Get Incentives API endpoint gives you the list of all price incentives for items in your catalog.

        The details include Item Id, Product Name, Product Url, SKU Id, Target Price, current Price, Incentive Type,
        Incentive Status, Base referral fee, Reduced Referral Fee, Enrollment Type, Inventory count, Enrollment Date
        (epoch Timestamp), Start date (epoch Timestamp), Expiration date (epoch Timestamp), and Incentive Id.

        Target Price, Expiration date, Start date, Incentive Id, and Reduced Ref fee and Enrollment Type for WF items
        would not be shown (null values).

        Enrollment Type and Date for Eligible Reduced Referral Fee incentives will not show up.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            incentive_status: Specify the incentive status to retrieve items with ELIGIBLE or ENROLLED incentives.
                Allowed values include ENROLLED and ELIGIBLE.<br><b style='color:green;'>Market availability: US</b>
            limit: Specify number of items to return. Max limit value is 200 and min is 1.<br><b
                style='color:green;'>Market availability: US</b>
            offset: Specify the offset of item list to be returned. Min offset value is 0.<br><b
                style='color:green;'>Market availability: US</b>
            sort_by: Specify the sort criteria for items. Examples of the allowed values are ITEM_ID, PRODUCT_NAME,
                CURRENT_PRICE, EXPIRATION_DATE, ENROLLMENT_DATE.<br><b style='color:green;'>Market availability: US</b>
            sort_order: Specify the sort order for given sort criteria. Examples of the allowed values are ASC or
                DESC.<br><b style='color:green;'>Market availability: US</b>
            incentive_type: Specify the incentive type to filter the incentive items. Allowed values include
                REDUCED_REFERRAL, WALMART_FUNDED.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3PriceIncentives400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_all_incentives(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                incentive_status=incentive_status,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                incentive_type=incentive_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_repricer_feed(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Add/Remove one or more items from a strategy.<br><b style='color:green;'>Market availability: US | CA |
        MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            <br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_repricer_feed(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_strategies(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        offset: str | None = "0",
        limit: str | None = "10",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategiesResponse:
        """Get the list of strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            offset: The response object starts at 0, representing the first entity that can be retrieved.<br><b
                style='color:green;'>Market availability: CA | MX</b>
            limit: The number of entities to return, with a maximum limit of 25.<br><b style='color:green;'>Market
                availability: CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_strategies(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def price_and_promotion_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """Updates prices and promotions in bulk for multiple items. You can modify the prices of multiple items in bulk
        using a price feed. This is useful for implementing pricing strategies across your catalog, such as seasonal
        discounts, competitive pricing adjustments, or clearance sales.

        Each price feed can contain up to 10,000 items. To ensure optimal performance (feed processing time), we
        recommend limiting feeds to 1,000 items and keeping the payload under 10 MB.

        Use this API instead of the single price update API when updating prices for multiple items. For newly created
        items, ensure that the Walmart Part ID (WPID) has been assigned and that at least 24 hours have passed since
        item creation before submitting a bulk price update feed. The bulk price update Service Level Agreement (SLA) is
        15 minutes.

        The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:

        <ul><li>You may include the same Stock Keeping Unit (SKU) multiple times in a single feed. However, if a SKU is
        repeated in a feed, only one price will be applied.</li><li>The price sequence guarantee ensures that the latest
        price update, based on its creation timestamp, is the one that changes the item's price, overwriting the
        previous version.</li><li>Price updates received with an earlier timestamp are ignored. We recommend using UTC
        timestamps for the value of <code>feedDate</code> in all feed-based bulk updates.</li></ul>

        After submitting the price feed, wait at least 5 minutes before checking whether the bulk price update was
        successful. If a price update fails, for example, due to duplicate SKU entries, an error response will be
        returned.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/global-marketplace/docs/update-pricing-for-multiple-items-bulk">Pricing API
        Guide</a>.

        <strong style="color: green;">Market availability: Global</strong>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.price_and_promotion_bulk_uploads(
                feed_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def reduced_referral_fee_incentives_enrollment(
        self,
        feed_type: FeedType11OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsFeedTypeIncentiveEnrollmentResponse:
        """You can use this API endpoint to enroll any eligible reduced referral fee incentive and unenroll any active
        reduced referral fee incentives.<br><b style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists referralFeeIncentiveEnrollment through which sku opt-in using Y and opt-out
                using N.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.reduced_referral_fee_incentives_enrollment(
                feed_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_price(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceResponse:
        """Updates the price of an item listed on Walmart Marketplace. Use this API to change the price of a single
        item. If you want to update pricing for multiple items, we recommend using the <a
        href="https://developer.walmart.com/global-marketplace/reference/priceandpromotionbulkuploads">Update pricing
        for multiple items in bulk</a> API.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/us-marketplace/docs/update-pricing-for-a-single-item">Pricing API
        Guide</a>.<br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_price(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategyResponse:
        """Updates the existing strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_strategy(
                strategy_collection_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_walmart_funded_incentives_enrollment_status(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        auto_enroll_enabled: bool = True,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceIncentivesWfpreferenceResponse:
        """If you wish to permanently disable Walmart-funded incentives for all items of your catalog, you can use this
        API to set the Walmart-funded incentives program as OFF.

        The default value of this variable is ON.

        Any changes to preferences will lock in (disable) the preference option for a period of 4 hours as indicated by
        isDisabled response field of the API.<br><b style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            auto_enroll_enabled: Specify the boolean for enabling auto enrollment. Examples of the allowed values are
                true or false.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_walmart_funded_incentives_enrollment_status(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                auto_enroll_enabled=auto_enroll_enabled,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def walmart_funded_incentives_enrollment(
        self,
        feed_type: FeedType2OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
            | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """While all Walmart-funded incentives are auto-enrolled by default, you can use this API endpoint to 'Opt-out'
        specific Walmart-funded items whose price you don't wish to lower.

        You can also 'Opt-in' items which were previously Opted-out by you at any time using this API.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists walmartFundedIncentivesEnrollment through which Opt-in / Opt-out has to be
                updated
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.walmart_funded_incentives_enrollment(
                feed_type,
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
    def with_raw_response(self) -> PricesWithRawResponse:
        return self._with_raw_response


class AsyncPrices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPricesWithRawResponse(client, server, auth)

    async def create_strategy(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategyResponse2:
        """Creates a new strategy for the seller.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_strategy(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def delete_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """Deletes the strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_strategy(
                strategy_collection_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_all_incentives(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE,
        limit: int | None = 25,
        offset: int | None = 0,
        sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE,
        sort_order: OrderOrStr | None = Order.DESC,
        incentive_type: IncentiveTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceIncentivesResponse:
        """Get Incentives API endpoint gives you the list of all price incentives for items in your catalog.

        The details include Item Id, Product Name, Product Url, SKU Id, Target Price, current Price, Incentive Type,
        Incentive Status, Base referral fee, Reduced Referral Fee, Enrollment Type, Inventory count, Enrollment Date
        (epoch Timestamp), Start date (epoch Timestamp), Expiration date (epoch Timestamp), and Incentive Id.

        Target Price, Expiration date, Start date, Incentive Id, and Reduced Ref fee and Enrollment Type for WF items
        would not be shown (null values).

        Enrollment Type and Date for Eligible Reduced Referral Fee incentives will not show up.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            incentive_status: Specify the incentive status to retrieve items with ELIGIBLE or ENROLLED incentives.
                Allowed values include ENROLLED and ELIGIBLE.<br><b style='color:green;'>Market availability: US</b>
            limit: Specify number of items to return. Max limit value is 200 and min is 1.<br><b
                style='color:green;'>Market availability: US</b>
            offset: Specify the offset of item list to be returned. Min offset value is 0.<br><b
                style='color:green;'>Market availability: US</b>
            sort_by: Specify the sort criteria for items. Examples of the allowed values are ITEM_ID, PRODUCT_NAME,
                CURRENT_PRICE, EXPIRATION_DATE, ENROLLMENT_DATE.<br><b style='color:green;'>Market availability: US</b>
            sort_order: Specify the sort order for given sort criteria. Examples of the allowed values are ASC or
                DESC.<br><b style='color:green;'>Market availability: US</b>
            incentive_type: Specify the incentive type to filter the incentive items. Allowed values include
                REDUCED_REFERRAL, WALMART_FUNDED.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3PriceIncentives400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_all_incentives(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                incentive_status=incentive_status,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                incentive_type=incentive_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_repricer_feed(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Add/Remove one or more items from a strategy.<br><b style='color:green;'>Market availability: US | CA |
        MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            <br><b style='color:green;'>Market availability: US | CA | MX</b>

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_repricer_feed(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_strategies(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        offset: str | None = "0",
        limit: str | None = "10",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategiesResponse:
        """Get the list of strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            offset: The response object starts at 0, representing the first entity that can be retrieved.<br><b
                style='color:green;'>Market availability: CA | MX</b>
            limit: The number of entities to return, with a maximum limit of 25.<br><b style='color:green;'>Market
                availability: CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_strategies(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def price_and_promotion_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """Updates prices and promotions in bulk for multiple items. You can modify the prices of multiple items in bulk
        using a price feed. This is useful for implementing pricing strategies across your catalog, such as seasonal
        discounts, competitive pricing adjustments, or clearance sales.

        Each price feed can contain up to 10,000 items. To ensure optimal performance (feed processing time), we
        recommend limiting feeds to 1,000 items and keeping the payload under 10 MB.

        Use this API instead of the single price update API when updating prices for multiple items. For newly created
        items, ensure that the Walmart Part ID (WPID) has been assigned and that at least 24 hours have passed since
        item creation before submitting a bulk price update feed. The bulk price update Service Level Agreement (SLA) is
        15 minutes.

        The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:

        <ul><li>You may include the same Stock Keeping Unit (SKU) multiple times in a single feed. However, if a SKU is
        repeated in a feed, only one price will be applied.</li><li>The price sequence guarantee ensures that the latest
        price update, based on its creation timestamp, is the one that changes the item's price, overwriting the
        previous version.</li><li>Price updates received with an earlier timestamp are ignored. We recommend using UTC
        timestamps for the value of <code>feedDate</code> in all feed-based bulk updates.</li></ul>

        After submitting the price feed, wait at least 5 minutes before checking whether the bulk price update was
        successful. If a price update fails, for example, due to duplicate SKU entries, an error response will be
        returned.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/global-marketplace/docs/update-pricing-for-multiple-items-bulk">Pricing API
        Guide</a>.

        <strong style="color: green;">Market availability: Global</strong>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.price_and_promotion_bulk_uploads(
                feed_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def reduced_referral_fee_incentives_enrollment(
        self,
        feed_type: FeedType11OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsFeedTypeIncentiveEnrollmentResponse:
        """You can use this API endpoint to enroll any eligible reduced referral fee incentive and unenroll any active
        reduced referral fee incentives.<br><b style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists referralFeeIncentiveEnrollment through which sku opt-in using Y and opt-out
                using N.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.reduced_referral_fee_incentives_enrollment(
                feed_type,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_price(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceResponse:
        """Updates the price of an item listed on Walmart Marketplace. Use this API to change the price of a single
        item. If you want to update pricing for multiple items, we recommend using the <a
        href="https://developer.walmart.com/global-marketplace/reference/priceandpromotionbulkuploads">Update pricing
        for multiple items in bulk</a> API.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/us-marketplace/docs/update-pricing-for-a-single-item">Pricing API
        Guide</a>.<br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_price(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3RepricerStrategyResponse:
        """Updates the existing strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Forbidden - Unsupported Market Internal Server Error ``error`` is
                ``V3RepricerStrategy400Error1 | V3Token400Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_strategy(
                strategy_collection_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_walmart_funded_incentives_enrollment_status(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        auto_enroll_enabled: bool = True,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceIncentivesWfpreferenceResponse:
        """If you wish to permanently disable Walmart-funded incentives for all items of your catalog, you can use this
        API to set the Walmart-funded incentives program as OFF.

        The default value of this variable is ON.

        Any changes to preferences will lock in (disable) the preference option for a period of 4 hours as indicated by
        isDisabled response field of the API.<br><b style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            auto_enroll_enabled: Specify the boolean for enabling auto enrollment. Examples of the allowed values are
                true or false.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_walmart_funded_incentives_enrollment_status(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                auto_enroll_enabled=auto_enroll_enabled,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def walmart_funded_incentives_enrollment(
        self,
        feed_type: FeedType2OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
            | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """While all Walmart-funded incentives are auto-enrolled by default, you can use this API endpoint to 'Opt-out'
        specific Walmart-funded items whose price you don't wish to lower.

        You can also 'Opt-in' items which were previously Opted-out by you at any time using this API.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists walmartFundedIncentivesEnrollment through which Opt-in / Opt-out has to be
                updated
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token400Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.walmart_funded_incentives_enrollment(
                feed_type,
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
    def with_raw_response(self) -> AsyncPricesWithRawResponse:
        return self._with_raw_response


class PricesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_strategy(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategyResponse2, CreateStrategyErrorBody]:
        """Creates a new strategy for the seller.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/repricer/strategy"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3RepricerStrategyResponse2],
            error_mapper=create_strategy_error_mapper,
            request_options=request_options,
        )

    def delete_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, DeleteStrategyErrorBody]:
        """Deletes the strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/repricer/strategy/{strategyCollectionId}"),
            path_params=[param[str]("strategyCollectionId", strategy_collection_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=delete_strategy_error_mapper,
            request_options=request_options,
        )

    def get_all_incentives(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE,
        limit: int | None = 25,
        offset: int | None = 0,
        sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE,
        sort_order: OrderOrStr | None = Order.DESC,
        incentive_type: IncentiveTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceIncentivesResponse, GetAllIncentivesErrorBody]:
        """Get Incentives API endpoint gives you the list of all price incentives for items in your catalog.

        The details include Item Id, Product Name, Product Url, SKU Id, Target Price, current Price, Incentive Type,
        Incentive Status, Base referral fee, Reduced Referral Fee, Enrollment Type, Inventory count, Enrollment Date
        (epoch Timestamp), Start date (epoch Timestamp), Expiration date (epoch Timestamp), and Incentive Id.

        Target Price, Expiration date, Start date, Incentive Id, and Reduced Ref fee and Enrollment Type for WF items
        would not be shown (null values).

        Enrollment Type and Date for Eligible Reduced Referral Fee incentives will not show up.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            incentive_status: Specify the incentive status to retrieve items with ELIGIBLE or ENROLLED incentives.
                Allowed values include ENROLLED and ELIGIBLE.<br><b style='color:green;'>Market availability: US</b>
            limit: Specify number of items to return. Max limit value is 200 and min is 1.<br><b
                style='color:green;'>Market availability: US</b>
            offset: Specify the offset of item list to be returned. Min offset value is 0.<br><b
                style='color:green;'>Market availability: US</b>
            sort_by: Specify the sort criteria for items. Examples of the allowed values are ITEM_ID, PRODUCT_NAME,
                CURRENT_PRICE, EXPIRATION_DATE, ENROLLMENT_DATE.<br><b style='color:green;'>Market availability: US</b>
            sort_order: Specify the sort order for given sort criteria. Examples of the allowed values are ASC or
                DESC.<br><b style='color:green;'>Market availability: US</b>
            incentive_type: Specify the incentive type to filter the incentive items. Allowed values include
                REDUCED_REFERRAL, WALMART_FUNDED.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/price/incentives"),
            query_params=[
                param[IncentiveStatusOrStr]("incentiveStatus", incentive_status),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[SortBy1OrStr | None]("sortBy", sort_by),
                param[OrderOrStr | None]("sortOrder", sort_order),
                param[IncentiveTypeOrStr | None]("incentiveType", incentive_type),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3PriceIncentivesResponse],
            error_mapper=get_all_incentives_error_mapper,
            request_options=request_options,
        )

    def get_repricer_feed(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, GetRepricerFeedErrorBody]:
        """Add/Remove one or more items from a strategy.<br><b style='color:green;'>Market availability: US | CA |
        MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/repricerFeeds"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerFeedsRequest | V3RepricerFeedsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId1],
            error_mapper=get_repricer_feed_error_mapper,
            request_options=request_options,
        )

    def get_strategies(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        offset: str | None = "0",
        limit: str | None = "10",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategiesResponse, GetStrategiesErrorBody]:
        """Get the list of strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            offset: The response object starts at 0, representing the first entity that can be retrieved.<br><b
                style='color:green;'>Market availability: CA | MX</b>
            limit: The number of entities to return, with a maximum limit of 25.<br><b style='color:green;'>Market
                availability: CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/repricer/strategies"),
            query_params=[param[str | None]("offset", offset), param[str | None]("limit", limit)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3RepricerStrategiesResponse],
            error_mapper=get_strategies_error_mapper,
            request_options=request_options,
        )

    def price_and_promotion_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, PriceAndPromotionBulkUploadsErrorBody]:
        """Updates prices and promotions in bulk for multiple items. You can modify the prices of multiple items in bulk
        using a price feed. This is useful for implementing pricing strategies across your catalog, such as seasonal
        discounts, competitive pricing adjustments, or clearance sales.

        Each price feed can contain up to 10,000 items. To ensure optimal performance (feed processing time), we
        recommend limiting feeds to 1,000 items and keeping the payload under 10 MB.

        Use this API instead of the single price update API when updating prices for multiple items. For newly created
        items, ensure that the Walmart Part ID (WPID) has been assigned and that at least 24 hours have passed since
        item creation before submitting a bulk price update feed. The bulk price update Service Level Agreement (SLA) is
        15 minutes.

        The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:

        <ul><li>You may include the same Stock Keeping Unit (SKU) multiple times in a single feed. However, if a SKU is
        repeated in a feed, only one price will be applied.</li><li>The price sequence guarantee ensures that the latest
        price update, based on its creation timestamp, is the one that changes the item's price, overwriting the
        previous version.</li><li>Price updates received with an earlier timestamp are ignored. We recommend using UTC
        timestamps for the value of <code>feedDate</code> in all feed-based bulk updates.</li></ul>

        After submitting the price feed, wait at least 5 minutes before checking whether the bulk price update was
        successful. If a price update fails, for example, due to duplicate SKU entries, an error response will be
        returned.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/global-marketplace/docs/update-pricing-for-multiple-items-bulk">Pricing API
        Guide</a>.

        <strong style="color: green;">Market availability: Global</strong>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PRICE_AND_PROMOTION"),
            query_params=[param[FeedType21OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId],
            error_mapper=price_and_promotion_bulk_uploads_error_mapper,
            request_options=request_options,
        )

    def reduced_referral_fee_incentives_enrollment(
        self,
        feed_type: FeedType11OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsFeedTypeIncentiveEnrollmentResponse, ReducedReferralFeeIncentivesEnrollmentErrorBody]:
        """You can use this API endpoint to enroll any eligible reduced referral fee incentive and unenroll any active
        reduced referral fee incentives.<br><b style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists referralFeeIncentiveEnrollment through which sku opt-in using Y and opt-out
                using N.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=INCENTIVE_ENROLLMENT"),
            query_params=[param[FeedType11OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3FeedsFeedTypeIncentiveEnrollmentResponse],
            error_mapper=reduced_referral_fee_incentives_enrollment_error_mapper,
            request_options=request_options,
        )

    def update_price(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceResponse, UpdatePriceErrorBody]:
        """Updates the price of an item listed on Walmart Marketplace. Use this API to change the price of a single
        item. If you want to update pricing for multiple items, we recommend using the <a
        href="https://developer.walmart.com/global-marketplace/reference/priceandpromotionbulkuploads">Update pricing
        for multiple items in bulk</a> API.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/us-marketplace/docs/update-pricing-for-a-single-item">Pricing API
        Guide</a>.<br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/price"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3PriceRequest | V3PriceRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3PriceResponse],
            error_mapper=update_price_error_mapper,
            request_options=request_options,
        )

    def update_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategyResponse, UpdateStrategyErrorBody]:
        """Updates the existing strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/repricer/strategy/{strategyCollectionId}"),
            path_params=[param[str]("strategyCollectionId", strategy_collection_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerStrategyRequest | V3RepricerStrategyRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3RepricerStrategyResponse],
            error_mapper=update_strategy_error_mapper,
            request_options=request_options,
        )

    def update_walmart_funded_incentives_enrollment_status(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        auto_enroll_enabled: bool = True,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceIncentivesWfpreferenceResponse, UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody]:
        """If you wish to permanently disable Walmart-funded incentives for all items of your catalog, you can use this
        API to set the Walmart-funded incentives program as OFF.

        The default value of this variable is ON.

        Any changes to preferences will lock in (disable) the preference option for a period of 4 hours as indicated by
        isDisabled response field of the API.<br><b style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            auto_enroll_enabled: Specify the boolean for enabling auto enrollment. Examples of the allowed values are
                true or false.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/price/incentives/wfpreference"),
            query_params=[param[bool]("autoEnrollEnabled", auto_enroll_enabled)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3PriceIncentivesWfpreferenceResponse],
            error_mapper=update_walmart_funded_incentives_enrollment_status_error_mapper,
            request_options=request_options,
        )

    def walmart_funded_incentives_enrollment(
        self,
        feed_type: FeedType2OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
            | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, WalmartFundedIncentivesEnrollmentErrorBody]:
        """While all Walmart-funded incentives are auto-enrolled by default, you can use this API endpoint to 'Opt-out'
        specific Walmart-funded items whose price you don't wish to lower.

        You can also 'Opt-in' items which were previously Opted-out by you at any time using this API.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists walmartFundedIncentivesEnrollment through which Opt-in / Opt-out has to be
                updated
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=WALMART_FUNDED_INCENTIVES_ENROLLMENT"),
            query_params=[param[FeedType2OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
                    | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
                )
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId],
            error_mapper=walmart_funded_incentives_enrollment_error_mapper,
            request_options=request_options,
        )


class AsyncPricesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_strategy(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategyResponse2, CreateStrategyErrorBody]:
        """Creates a new strategy for the seller.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information.<br><b style='color:green;'>Market
                availability: US | CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/repricer/strategy"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3RepricerStrategyResponse2],
            error_mapper=create_strategy_error_mapper,
            request_options=request_options,
        )

    async def delete_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, DeleteStrategyErrorBody]:
        """Deletes the strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/repricer/strategy/{strategyCollectionId}"),
            path_params=[param[str]("strategyCollectionId", strategy_collection_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=delete_strategy_error_mapper,
            request_options=request_options,
        )

    async def get_all_incentives(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE,
        limit: int | None = 25,
        offset: int | None = 0,
        sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE,
        sort_order: OrderOrStr | None = Order.DESC,
        incentive_type: IncentiveTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceIncentivesResponse, GetAllIncentivesErrorBody]:
        """Get Incentives API endpoint gives you the list of all price incentives for items in your catalog.

        The details include Item Id, Product Name, Product Url, SKU Id, Target Price, current Price, Incentive Type,
        Incentive Status, Base referral fee, Reduced Referral Fee, Enrollment Type, Inventory count, Enrollment Date
        (epoch Timestamp), Start date (epoch Timestamp), Expiration date (epoch Timestamp), and Incentive Id.

        Target Price, Expiration date, Start date, Incentive Id, and Reduced Ref fee and Enrollment Type for WF items
        would not be shown (null values).

        Enrollment Type and Date for Eligible Reduced Referral Fee incentives will not show up.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            incentive_status: Specify the incentive status to retrieve items with ELIGIBLE or ENROLLED incentives.
                Allowed values include ENROLLED and ELIGIBLE.<br><b style='color:green;'>Market availability: US</b>
            limit: Specify number of items to return. Max limit value is 200 and min is 1.<br><b
                style='color:green;'>Market availability: US</b>
            offset: Specify the offset of item list to be returned. Min offset value is 0.<br><b
                style='color:green;'>Market availability: US</b>
            sort_by: Specify the sort criteria for items. Examples of the allowed values are ITEM_ID, PRODUCT_NAME,
                CURRENT_PRICE, EXPIRATION_DATE, ENROLLMENT_DATE.<br><b style='color:green;'>Market availability: US</b>
            sort_order: Specify the sort order for given sort criteria. Examples of the allowed values are ASC or
                DESC.<br><b style='color:green;'>Market availability: US</b>
            incentive_type: Specify the incentive type to filter the incentive items. Allowed values include
                REDUCED_REFERRAL, WALMART_FUNDED.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/price/incentives"),
            query_params=[
                param[IncentiveStatusOrStr]("incentiveStatus", incentive_status),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[SortBy1OrStr | None]("sortBy", sort_by),
                param[OrderOrStr | None]("sortOrder", sort_order),
                param[IncentiveTypeOrStr | None]("incentiveType", incentive_type),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3PriceIncentivesResponse],
            error_mapper=get_all_incentives_error_mapper,
            request_options=request_options,
        )

    async def get_repricer_feed(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, GetRepricerFeedErrorBody]:
        """Add/Remove one or more items from a strategy.<br><b style='color:green;'>Market availability: US | CA |
        MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/repricerFeeds"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerFeedsRequest | V3RepricerFeedsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId1],
            error_mapper=get_repricer_feed_error_mapper,
            request_options=request_options,
        )

    async def get_strategies(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        offset: str | None = "0",
        limit: str | None = "10",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategiesResponse, GetStrategiesErrorBody]:
        """Get the list of strategies.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            offset: The response object starts at 0, representing the first entity that can be retrieved.<br><b
                style='color:green;'>Market availability: CA | MX</b>
            limit: The number of entities to return, with a maximum limit of 25.<br><b style='color:green;'>Market
                availability: CA | MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/repricer/strategies"),
            query_params=[param[str | None]("offset", offset), param[str | None]("limit", limit)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3RepricerStrategiesResponse],
            error_mapper=get_strategies_error_mapper,
            request_options=request_options,
        )

    async def price_and_promotion_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, PriceAndPromotionBulkUploadsErrorBody]:
        """Updates prices and promotions in bulk for multiple items. You can modify the prices of multiple items in bulk
        using a price feed. This is useful for implementing pricing strategies across your catalog, such as seasonal
        discounts, competitive pricing adjustments, or clearance sales.

        Each price feed can contain up to 10,000 items. To ensure optimal performance (feed processing time), we
        recommend limiting feeds to 1,000 items and keeping the payload under 10 MB.

        Use this API instead of the single price update API when updating prices for multiple items. For newly created
        items, ensure that the Walmart Part ID (WPID) has been assigned and that at least 24 hours have passed since
        item creation before submitting a bulk price update feed. The bulk price update Service Level Agreement (SLA) is
        15 minutes.

        The price sequence guarantee is observed by the bulk price update functionality, subject to the following rules:

        <ul><li>You may include the same Stock Keeping Unit (SKU) multiple times in a single feed. However, if a SKU is
        repeated in a feed, only one price will be applied.</li><li>The price sequence guarantee ensures that the latest
        price update, based on its creation timestamp, is the one that changes the item's price, overwriting the
        previous version.</li><li>Price updates received with an earlier timestamp are ignored. We recommend using UTC
        timestamps for the value of <code>feedDate</code> in all feed-based bulk updates.</li></ul>

        After submitting the price feed, wait at least 5 minutes before checking whether the bulk price update was
        successful. If a price update fails, for example, due to duplicate SKU entries, an error response will be
        returned.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/global-marketplace/docs/update-pricing-for-multiple-items-bulk">Pricing API
        Guide</a>.

        <strong style="color: green;">Market availability: Global</strong>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PRICE_AND_PROMOTION"),
            query_params=[param[FeedType21OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId],
            error_mapper=price_and_promotion_bulk_uploads_error_mapper,
            request_options=request_options,
        )

    async def reduced_referral_fee_incentives_enrollment(
        self,
        feed_type: FeedType11OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsFeedTypeIncentiveEnrollmentResponse, ReducedReferralFeeIncentivesEnrollmentErrorBody]:
        """You can use this API endpoint to enroll any eligible reduced referral fee incentive and unenroll any active
        reduced referral fee incentives.<br><b style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists referralFeeIncentiveEnrollment through which sku opt-in using Y and opt-out
                using N.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=INCENTIVE_ENROLLMENT"),
            query_params=[param[FeedType11OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3FeedsFeedTypeIncentiveEnrollmentResponse],
            error_mapper=reduced_referral_fee_incentives_enrollment_error_mapper,
            request_options=request_options,
        )

    async def update_price(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceResponse, UpdatePriceErrorBody]:
        """Updates the price of an item listed on Walmart Marketplace. Use this API to change the price of a single
        item. If you want to update pricing for multiple items, we recommend using the <a
        href="https://developer.walmart.com/global-marketplace/reference/priceandpromotionbulkuploads">Update pricing
        for multiple items in bulk</a> API.

        For more information and usage examples, refer to the <a
        href="https://developer.walmart.com/us-marketplace/docs/update-pricing-for-a-single-item">Pricing API
        Guide</a>.<br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
                .<br><b style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/price"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3PriceRequest | V3PriceRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3PriceResponse],
            error_mapper=update_price_error_mapper,
            request_options=request_options,
        )

    async def update_strategy(
        self,
        strategy_collection_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3RepricerStrategyResponse, UpdateStrategyErrorBody]:
        """Updates the existing strategy.<br><b style='color:green;'>Market availability: US | CA | MX</b>

        Args:
            strategy_collection_id: Unique identifier used to group and manage repricing strategies across different
                resources.<br><b style='color:green;'>Market availability: US | CA | MX</span></b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</span></b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</span></b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</span></b>
            body: The request body will have the strategy related information
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</span></b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/repricer/strategy/{strategyCollectionId}"),
            path_params=[param[str]("strategyCollectionId", strategy_collection_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3RepricerStrategyRequest | V3RepricerStrategyRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3RepricerStrategyResponse],
            error_mapper=update_strategy_error_mapper,
            request_options=request_options,
        )

    async def update_walmart_funded_incentives_enrollment_status(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        auto_enroll_enabled: bool = True,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceIncentivesWfpreferenceResponse, UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody]:
        """If you wish to permanently disable Walmart-funded incentives for all items of your catalog, you can use this
        API to set the Walmart-funded incentives program as OFF.

        The default value of this variable is ON.

        Any changes to preferences will lock in (disable) the preference option for a period of 4 hours as indicated by
        isDisabled response field of the API.<br><b style='color:green;'>Market availability: US</b>

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            auto_enroll_enabled: Specify the boolean for enabling auto enrollment. Examples of the allowed values are
                true or false.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/price/incentives/wfpreference"),
            query_params=[param[bool]("autoEnrollEnabled", auto_enroll_enabled)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3PriceIncentivesWfpreferenceResponse],
            error_mapper=update_walmart_funded_incentives_enrollment_status_error_mapper,
            request_options=request_options,
        )

    async def walmart_funded_incentives_enrollment(
        self,
        feed_type: FeedType2OrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: (
            V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
            | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
        ),
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, WalmartFundedIncentivesEnrollmentErrorBody]:
        """While all Walmart-funded incentives are auto-enrolled by default, you can use this API endpoint to 'Opt-out'
        specific Walmart-funded items whose price you don't wish to lower.

        You can also 'Opt-in' items which were previously Opted-out by you at any time using this API.<br><b
        style='color:green;'>Market availability: US</b>

        Args:
            feed_type: The feed Type.<br><b style='color:green;'>Market availability: US</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            body: The request body consists walmartFundedIncentivesEnrollment through which Opt-in / Opt-out has to be
                updated
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=WALMART_FUNDED_INCENTIVES_ENROLLMENT"),
            query_params=[param[FeedType2OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                (
                    V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest
                    | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict
                )
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId],
            error_mapper=walmart_funded_incentives_enrollment_error_mapper,
            request_options=request_options,
        )

from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileResponse,
    AsyncRawClient,
    FileResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_file_decoder,
    async_json_decoder,
    file_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.get_all_feed_statuses_error import GetAllFeedStatusesErrorBody, get_all_feed_statuses_error_mapper
from ..errors.get_feed_item_status_error import GetFeedItemStatusErrorBody, get_feed_item_status_error_mapper
from ..models.enums.feed_status1 import FeedStatus1OrStr
from ..models.enums.feed_type import FeedTypeOrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_record_response import FeedRecordResponse
from ..models.v3_feeds_response1 import V3FeedsResponse1
from ..server.server import Server


class FeedsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FeedsApiWithRawResponse(client, server, auth)

    def get_all_feed_statuses(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        feed_id: str | None = None,
        feed_type: str | None = None,
        feed_status: FeedStatus1OrStr | None = None,
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedRecordResponse:
        """This API returns the feed statuses for all the specified feed IDs. Use the specified feedTypes to query the
        status of each feed and identify whether it was processed successfully, failed, or is still in progress.

        | FeedTypes | Availability |
        |--------|----------|
        | MP_MAINTENANCE, MP_ITEM_MATCH, LAGTIME | Global |
        | MP_INVENTORY, SKU_TEMPLATE_MAP | US, CA, MX |
        | MP_ITEM_INTL | CA, MX, CL |
        | MP_ITEM, MP_WFS_ITEM, WALMART_FUNDED_INCENTIVES_ENROLLMENT, INCENTIVE_ENROLLMENT,PRICE_AND_PROMOTION | US Only
            |
        | OMNI_WFS, RETIRE_ITEM, SHIPPING_OVERRIDES, FITMENT_ACES, FITMENT_PIES, SPLIT_AND_MERGE | US Only |
        | OMNI_WFSSETUP, OMNI_WFSCONVERT | CA, MX |

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_type: The feedType parameter defines the type of feed whose status you are querying. Feed types are
                specific to each market, so be sure to provide a value that is supported for your target market. <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_status: Status of the feed. <strong style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. <strong
                style="color: green;">**Market availability: Global**</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found Internal Server Error ``error`` is ``FeedRecordResponse | RawError``."""
        return unwrap(
            self._with_raw_response.get_all_feed_statuses(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                feed_id=feed_id,
                feed_type=feed_type,
                feed_status=feed_status,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_feed_error_report(
        self,
        feed_id: str,
        feed_type: FeedTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponse:
        """Get Feed Error Report API allows you to download a detailed error report for a submitted feed.

        Currently the API supports error report download for the following feeds:
        * FITMENT_ACES
        * FITMENT_PIES

         This API returns a zipped .csv file, which contains line item level detailed error messages. For details and a
            sample, please refer to the guide section link below.
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            feed_id: Feed Id of the feed. <strong style="color: green;">**Market availability: US only**</strong>
            feed_type: Feed type for which Error Report needs to be downloaded. <strong style="color: green;">**Market
                availability: US only**</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_feed_error_report(
                feed_id,
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_feed_item_status(
        self,
        feed_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        include_details: str | None = "false",
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsResponse1:
        """Returns the feed and item status for a specified Feed ID. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            include_details: Includes details for each entity in the feed. When set to true, returns detailed
                information about each item in the feed, including individual success or failure statuses and any
                specific error messages. Defaults to false, which returns only high-level feed status. <strong
                style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found Internal Server Error ``error`` is ``V3Feeds404Error21 | V3Feeds500Error21 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_feed_item_status(
                feed_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                include_details=include_details,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> FeedsApiWithRawResponse:
        return self._with_raw_response


class AsyncFeedsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFeedsApiWithRawResponse(client, server, auth)

    async def get_all_feed_statuses(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        feed_id: str | None = None,
        feed_type: str | None = None,
        feed_status: FeedStatus1OrStr | None = None,
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedRecordResponse:
        """This API returns the feed statuses for all the specified feed IDs. Use the specified feedTypes to query the
        status of each feed and identify whether it was processed successfully, failed, or is still in progress.

        | FeedTypes | Availability |
        |--------|----------|
        | MP_MAINTENANCE, MP_ITEM_MATCH, LAGTIME | Global |
        | MP_INVENTORY, SKU_TEMPLATE_MAP | US, CA, MX |
        | MP_ITEM_INTL | CA, MX, CL |
        | MP_ITEM, MP_WFS_ITEM, WALMART_FUNDED_INCENTIVES_ENROLLMENT, INCENTIVE_ENROLLMENT,PRICE_AND_PROMOTION | US Only
            |
        | OMNI_WFS, RETIRE_ITEM, SHIPPING_OVERRIDES, FITMENT_ACES, FITMENT_PIES, SPLIT_AND_MERGE | US Only |
        | OMNI_WFSSETUP, OMNI_WFSCONVERT | CA, MX |

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_type: The feedType parameter defines the type of feed whose status you are querying. Feed types are
                specific to each market, so be sure to provide a value that is supported for your target market. <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_status: Status of the feed. <strong style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. <strong
                style="color: green;">**Market availability: Global**</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found Internal Server Error ``error`` is ``FeedRecordResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.get_all_feed_statuses(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                feed_id=feed_id,
                feed_type=feed_type,
                feed_status=feed_status,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_feed_error_report(
        self,
        feed_id: str,
        feed_type: FeedTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsyncFileResponse:
        """Get Feed Error Report API allows you to download a detailed error report for a submitted feed.

        Currently the API supports error report download for the following feeds:
        * FITMENT_ACES
        * FITMENT_PIES

         This API returns a zipped .csv file, which contains line item level detailed error messages. For details and a
            sample, please refer to the guide section link below.
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            feed_id: Feed Id of the feed. <strong style="color: green;">**Market availability: US only**</strong>
            feed_type: Feed type for which Error Report needs to be downloaded. <strong style="color: green;">**Market
                availability: US only**</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_feed_error_report(
                feed_id,
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_feed_item_status(
        self,
        feed_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        include_details: str | None = "false",
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsResponse1:
        """Returns the feed and item status for a specified Feed ID. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            include_details: Includes details for each entity in the feed. When set to true, returns detailed
                information about each item in the feed, including individual success or failure statuses and any
                specific error messages. Defaults to false, which returns only high-level feed status. <strong
                style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found Internal Server Error ``error`` is ``V3Feeds404Error21 | V3Feeds500Error21 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_feed_item_status(
                feed_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                include_details=include_details,
                offset=offset,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFeedsApiWithRawResponse:
        return self._with_raw_response


class FeedsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_all_feed_statuses(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        feed_id: str | None = None,
        feed_type: str | None = None,
        feed_status: FeedStatus1OrStr | None = None,
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedRecordResponse, GetAllFeedStatusesErrorBody]:
        """This API returns the feed statuses for all the specified feed IDs. Use the specified feedTypes to query the
        status of each feed and identify whether it was processed successfully, failed, or is still in progress.

        | FeedTypes | Availability |
        |--------|----------|
        | MP_MAINTENANCE, MP_ITEM_MATCH, LAGTIME | Global |
        | MP_INVENTORY, SKU_TEMPLATE_MAP | US, CA, MX |
        | MP_ITEM_INTL | CA, MX, CL |
        | MP_ITEM, MP_WFS_ITEM, WALMART_FUNDED_INCENTIVES_ENROLLMENT, INCENTIVE_ENROLLMENT,PRICE_AND_PROMOTION | US Only
            |
        | OMNI_WFS, RETIRE_ITEM, SHIPPING_OVERRIDES, FITMENT_ACES, FITMENT_PIES, SPLIT_AND_MERGE | US Only |
        | OMNI_WFSSETUP, OMNI_WFSCONVERT | CA, MX |

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_type: The feedType parameter defines the type of feed whose status you are querying. Feed types are
                specific to each market, so be sure to provide a value that is supported for your target market. <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_status: Status of the feed. <strong style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. <strong
                style="color: green;">**Market availability: Global**</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds"),
            query_params=[
                param[str | None]("feedId", feed_id),
                param[str | None]("feedType", feed_type),
                param[FeedStatus1OrStr | None]("feedStatus", feed_status),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedRecordResponse],
            error_mapper=get_all_feed_statuses_error_mapper,
            request_options=request_options,
        )

    def get_feed_error_report(
        self,
        feed_id: str,
        feed_type: FeedTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponse, RawError]:
        """Get Feed Error Report API allows you to download a detailed error report for a submitted feed.

        Currently the API supports error report download for the following feeds:
        * FITMENT_ACES
        * FITMENT_PIES

         This API returns a zipped .csv file, which contains line item level detailed error messages. For details and a
            sample, please refer to the guide section link below.
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            feed_id: Feed Id of the feed. <strong style="color: green;">**Market availability: US only**</strong>
            feed_type: Feed type for which Error Report needs to be downloaded. <strong style="color: green;">**Market
                availability: US only**</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds/{feedId}/errorReport"),
            path_params=[param[str]("feedId", feed_id)],
            query_params=[param[FeedTypeOrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=file_decoder,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_feed_item_status(
        self,
        feed_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        include_details: str | None = "false",
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsResponse1, GetFeedItemStatusErrorBody]:
        """Returns the feed and item status for a specified Feed ID. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            include_details: Includes details for each entity in the feed. When set to true, returns detailed
                information about each item in the feed, including individual success or failure statuses and any
                specific error messages. Defaults to false, which returns only high-level feed status. <strong
                style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            query_params=[
                param[str | None]("includeDetails", include_details),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3FeedsResponse1],
            error_mapper=get_feed_item_status_error_mapper,
            request_options=request_options,
        )


class AsyncFeedsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_all_feed_statuses(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        feed_id: str | None = None,
        feed_type: str | None = None,
        feed_status: FeedStatus1OrStr | None = None,
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedRecordResponse, GetAllFeedStatusesErrorBody]:
        """This API returns the feed statuses for all the specified feed IDs. Use the specified feedTypes to query the
        status of each feed and identify whether it was processed successfully, failed, or is still in progress.

        | FeedTypes | Availability |
        |--------|----------|
        | MP_MAINTENANCE, MP_ITEM_MATCH, LAGTIME | Global |
        | MP_INVENTORY, SKU_TEMPLATE_MAP | US, CA, MX |
        | MP_ITEM_INTL | CA, MX, CL |
        | MP_ITEM, MP_WFS_ITEM, WALMART_FUNDED_INCENTIVES_ENROLLMENT, INCENTIVE_ENROLLMENT,PRICE_AND_PROMOTION | US Only
            |
        | OMNI_WFS, RETIRE_ITEM, SHIPPING_OVERRIDES, FITMENT_ACES, FITMENT_PIES, SPLIT_AND_MERGE | US Only |
        | OMNI_WFSSETUP, OMNI_WFSCONVERT | CA, MX |

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_type: The feedType parameter defines the type of feed whose status you are querying. Feed types are
                specific to each market, so be sure to provide a value that is supported for your target market. <strong
                style="color: green;">**Market availability: Global**</strong>
            feed_status: Status of the feed. <strong style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. <strong
                style="color: green;">**Market availability: Global**</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. <strong style="color:
                green;">**Market availability: Global**</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds"),
            query_params=[
                param[str | None]("feedId", feed_id),
                param[str | None]("feedType", feed_type),
                param[FeedStatus1OrStr | None]("feedStatus", feed_status),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedRecordResponse],
            error_mapper=get_all_feed_statuses_error_mapper,
            request_options=request_options,
        )

    async def get_feed_error_report(
        self,
        feed_id: str,
        feed_type: FeedTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsyncFileResponse, RawError]:
        """Get Feed Error Report API allows you to download a detailed error report for a submitted feed.

        Currently the API supports error report download for the following feeds:
        * FITMENT_ACES
        * FITMENT_PIES

         This API returns a zipped .csv file, which contains line item level detailed error messages. For details and a
            sample, please refer to the guide section link below.
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            feed_id: Feed Id of the feed. <strong style="color: green;">**Market availability: US only**</strong>
            feed_type: Feed type for which Error Report needs to be downloaded. <strong style="color: green;">**Market
                availability: US only**</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds/{feedId}/errorReport"),
            path_params=[param[str]("feedId", feed_id)],
            query_params=[param[FeedTypeOrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_file_decoder,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_feed_item_status(
        self,
        feed_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        include_details: str | None = "false",
        offset: str | None = "0",
        limit: str | None = "50",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsResponse1, GetFeedItemStatusErrorBody]:
        """Returns the feed and item status for a specified Feed ID. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            feed_id: A unique ID returned from the Bulk Upload API, used for tracking the Feed File. Special characters
                must be escaped. (e.g., feedId: '...3456@789...' must be entered in the URL as '...3456%40789). <strong
                style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            include_details: Includes details for each entity in the feed. When set to true, returns detailed
                information about each item in the feed, including individual success or failure statuses and any
                specific error messages. Defaults to false, which returns only high-level feed status. <strong
                style="color: green;">**Market availability: Global**</strong>
            offset: The object response to start with, where 0 is the first entity that can be requested. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            limit: The number of entities to be returned. It cannot be more than 50 entities. Use only when
                ``includeDetails`` is set to true. <strong style="color: green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            query_params=[
                param[str | None]("includeDetails", include_details),
                param[str | None]("offset", offset),
                param[str | None]("limit", limit),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3FeedsResponse1],
            error_mapper=get_feed_item_status_error_mapper,
            request_options=request_options,
        )

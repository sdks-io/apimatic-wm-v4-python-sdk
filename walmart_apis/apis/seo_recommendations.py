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
from ..errors.get_seo_recommendations_error import GetSeoRecommendationsErrorBody, get_seo_recommendations_error_mapper
from ..errors.update_seo_recommendations_error import (
    UpdateSeoRecommendationsErrorBody,
    update_seo_recommendations_error_mapper,
)
from ..models.enums.decision import DecisionOrStr
from ..models.enums.status2 import Status2OrStr
from ..models.v3_seo_recommendation_get_items_request import (
    V3SeoRecommendationGetItemsRequest,
    V3SeoRecommendationGetItemsRequestDict,
)
from ..models.v3_seo_recommendation_get_items_response import V3SeoRecommendationGetItemsResponse
from ..models.v3_seo_recommendation_update_items_request import (
    V3SeoRecommendationUpdateItemsRequest,
    V3SeoRecommendationUpdateItemsRequestDict,
)
from ..models.v3_seo_recommendation_update_items_response import V3SeoRecommendationUpdateItemsResponse
from ..server.server import Server


class SeoRecommendations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SeoRecommendationsWithRawResponse(client, server, auth)

    def get_seo_recommendations(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        status: Status2OrStr | None = None,
        limit: str | None = None,
        next_cursor: str | None = None,
        previous_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3SeoRecommendationGetItemsResponse:
        """Get list of items with SEO recommendations. Sellers can filter items by status (all, new, accepted,
        rejected), search for specific items using identifiers like (itemId, sku, or name) and paginate results for
        large datasets..

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            status: Specifies the type of items to retrieve. Default when type not provided it will return new items.
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.
            next_cursor: Link to go to the next page
            previous_cursor: Link to go to the previous page
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: This will contain the wild card search related details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK. The request was successful. The server returned the requested data.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``V3SeoRecommendationGetItems400Error1
                | V3SeoRecommendationGetItems500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_seo_recommendations(
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                status=status,
                limit=limit,
                next_cursor=next_cursor,
                previous_cursor=previous_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    def update_seo_recommendations(
        self,
        item_id: str,
        decision: DecisionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3SeoRecommendationUpdateItemsResponse:
        """Sellers can accept or reject SEO recommendations with optimal feedback for rejected recommendations

        Args:
            item_id: Unique Item Identifier
            decision: approve/reject a recommendation
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: Additional details required for submission
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK. The SEO recommendation update was successful

        Raises:
            ApiError: Bad request. Seo Recommended Item Unavailable Bad request. ``error`` is
                ``V3SeoRecommendationUpdateItems400Error1 | V3SeoRecommendationUpdateItems404Error1 |
                V3SeoRecommendationUpdateItems500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_seo_recommendations(
                item_id,
                decision,
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SeoRecommendationsWithRawResponse:
        return self._with_raw_response


class AsyncSeoRecommendations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSeoRecommendationsWithRawResponse(client, server, auth)

    async def get_seo_recommendations(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        status: Status2OrStr | None = None,
        limit: str | None = None,
        next_cursor: str | None = None,
        previous_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3SeoRecommendationGetItemsResponse:
        """Get list of items with SEO recommendations. Sellers can filter items by status (all, new, accepted,
        rejected), search for specific items using identifiers like (itemId, sku, or name) and paginate results for
        large datasets..

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            status: Specifies the type of items to retrieve. Default when type not provided it will return new items.
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.
            next_cursor: Link to go to the next page
            previous_cursor: Link to go to the previous page
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: This will contain the wild card search related details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK. The request was successful. The server returned the requested data.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``V3SeoRecommendationGetItems400Error1
                | V3SeoRecommendationGetItems500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_seo_recommendations(
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                status=status,
                limit=limit,
                next_cursor=next_cursor,
                previous_cursor=previous_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    async def update_seo_recommendations(
        self,
        item_id: str,
        decision: DecisionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3SeoRecommendationUpdateItemsResponse:
        """Sellers can accept or reject SEO recommendations with optimal feedback for rejected recommendations

        Args:
            item_id: Unique Item Identifier
            decision: approve/reject a recommendation
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: Additional details required for submission
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK. The SEO recommendation update was successful

        Raises:
            ApiError: Bad request. Seo Recommended Item Unavailable Bad request. ``error`` is
                ``V3SeoRecommendationUpdateItems400Error1 | V3SeoRecommendationUpdateItems404Error1 |
                V3SeoRecommendationUpdateItems500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_seo_recommendations(
                item_id,
                decision,
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSeoRecommendationsWithRawResponse:
        return self._with_raw_response


class SeoRecommendationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_seo_recommendations(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        status: Status2OrStr | None = None,
        limit: str | None = None,
        next_cursor: str | None = None,
        previous_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3SeoRecommendationGetItemsResponse, GetSeoRecommendationsErrorBody]:
        """Get list of items with SEO recommendations. Sellers can filter items by status (all, new, accepted,
        rejected), search for specific items using identifiers like (itemId, sku, or name) and paginate results for
        large datasets..

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            status: Specifies the type of items to retrieve. Default when type not provided it will return new items.
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.
            next_cursor: Link to go to the next page
            previous_cursor: Link to go to the previous page
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: This will contain the wild card search related details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/seo/recommendation/getItems"),
            query_params=[
                param[Status2OrStr | None]("status", status),
                param[str | None]("limit", limit),
                param[str | None]("next_cursor", next_cursor),
                param[str | None]("previous_cursor", previous_cursor),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3SeoRecommendationGetItemsResponse],
            error_mapper=get_seo_recommendations_error_mapper,
            request_options=request_options,
        )

    def update_seo_recommendations(
        self,
        item_id: str,
        decision: DecisionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3SeoRecommendationUpdateItemsResponse, UpdateSeoRecommendationsErrorBody]:
        """Sellers can accept or reject SEO recommendations with optimal feedback for rejected recommendations

        Args:
            item_id: Unique Item Identifier
            decision: approve/reject a recommendation
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: Additional details required for submission
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/seo/recommendation/updateItems/{itemId}/{decision}"),
            path_params=[param[str]("itemId", item_id), param[DecisionOrStr]("decision", decision)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3SeoRecommendationUpdateItemsResponse],
            error_mapper=update_seo_recommendations_error_mapper,
            request_options=request_options,
        )


class AsyncSeoRecommendationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_seo_recommendations(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        status: Status2OrStr | None = None,
        limit: str | None = None,
        next_cursor: str | None = None,
        previous_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3SeoRecommendationGetItemsResponse, GetSeoRecommendationsErrorBody]:
        """Get list of items with SEO recommendations. Sellers can filter items by status (all, new, accepted,
        rejected), search for specific items using identifiers like (itemId, sku, or name) and paginate results for
        large datasets..

        Args:
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            status: Specifies the type of items to retrieve. Default when type not provided it will return new items.
            limit: Specify number of items to return. If no limit is specified, API returns 200 items by default.
            next_cursor: Link to go to the next page
            previous_cursor: Link to go to the previous page
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: This will contain the wild card search related details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/seo/recommendation/getItems"),
            query_params=[
                param[Status2OrStr | None]("status", status),
                param[str | None]("limit", limit),
                param[str | None]("next_cursor", next_cursor),
                param[str | None]("previous_cursor", previous_cursor),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3SeoRecommendationGetItemsResponse],
            error_mapper=get_seo_recommendations_error_mapper,
            request_options=request_options,
        )

    async def update_seo_recommendations(
        self,
        item_id: str,
        decision: DecisionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3SeoRecommendationUpdateItemsResponse, UpdateSeoRecommendationsErrorBody]:
        """Sellers can accept or reject SEO recommendations with optimal feedback for rejected recommendations

        Args:
            item_id: Unique Item Identifier
            decision: approve/reject a recommendation
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            accept: Only supported Media Type : application/json
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            body: Additional details required for submission
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/seo/recommendation/updateItems/{itemId}/{decision}"),
            path_params=[param[str]("itemId", item_id), param[DecisionOrStr]("decision", decision)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3SeoRecommendationUpdateItemsResponse],
            error_mapper=update_seo_recommendations_error_mapper,
            request_options=request_options,
        )

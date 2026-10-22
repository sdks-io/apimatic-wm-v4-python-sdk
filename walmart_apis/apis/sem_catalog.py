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
from ..errors.get_eligible_items_error import GetEligibleItemsErrorBody, get_eligible_items_error_mapper
from ..errors.get_item_recommendations_error import (
    GetItemRecommendationsErrorBody,
    get_item_recommendations_error_mapper,
)
from ..models.sem_catalogue_response import SemCatalogueResponse
from ..models.sem_item_eligibility_request import SemItemEligibilityRequest, SemItemEligibilityRequestDict
from ..server.server import Server


class SemCatalog:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SemCatalogWithRawResponse(client, server, auth)

    def get_eligible_items(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemItemEligibilityRequest | SemItemEligibilityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCatalogueResponse:
        """This API allows you to check whether an item from your catalog meets the required conditions for Search
        Engine Marketing ads.<br><b style='color:green;'>Market availability: US only</b>

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
            self._with_raw_response.get_eligible_items(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_item_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 100,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCatalogueResponse:
        """This API allows you to fetch a list of top recommended items from your catalog. You can customize the number
        of recommendations to be returned by adjusting the request parameter.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            limit: Specifies the maximum number of recommended items to be returned. This value cannot exceed 200.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.get_item_recommendations(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SemCatalogWithRawResponse:
        return self._with_raw_response


class AsyncSemCatalog:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSemCatalogWithRawResponse(client, server, auth)

    async def get_eligible_items(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemItemEligibilityRequest | SemItemEligibilityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCatalogueResponse:
        """This API allows you to check whether an item from your catalog meets the required conditions for Search
        Engine Marketing ads.<br><b style='color:green;'>Market availability: US only</b>

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
            await self._with_raw_response.get_eligible_items(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_item_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 100,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCatalogueResponse:
        """This API allows you to fetch a list of top recommended items from your catalog. You can customize the number
        of recommendations to be returned by adjusting the request parameter.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            limit: Specifies the maximum number of recommended items to be returned. This value cannot exceed 200.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_item_recommendations(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                limit=limit,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSemCatalogWithRawResponse:
        return self._with_raw_response


class SemCatalogWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_eligible_items(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemItemEligibilityRequest | SemItemEligibilityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCatalogueResponse, GetEligibleItemsErrorBody]:
        """This API allows you to check whether an item from your catalog meets the required conditions for Search
        Engine Marketing ads.<br><b style='color:green;'>Market availability: US only</b>

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
            url_template=self._server.default("/v3/advertising/sem/items/eligibility"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemItemEligibilityRequest | SemItemEligibilityRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCatalogueResponse],
            error_mapper=get_eligible_items_error_mapper,
            request_options=request_options,
        )

    def get_item_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 100,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCatalogueResponse, GetItemRecommendationsErrorBody]:
        """This API allows you to fetch a list of top recommended items from your catalog. You can customize the number
        of recommendations to be returned by adjusting the request parameter.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            limit: Specifies the maximum number of recommended items to be returned. This value cannot exceed 200.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/items/recommendations"),
            query_params=[param[int | None]("limit", limit)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCatalogueResponse],
            error_mapper=get_item_recommendations_error_mapper,
            request_options=request_options,
        )


class AsyncSemCatalogWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_eligible_items(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: SemItemEligibilityRequest | SemItemEligibilityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCatalogueResponse, GetEligibleItemsErrorBody]:
        """This API allows you to check whether an item from your catalog meets the required conditions for Search
        Engine Marketing ads.<br><b style='color:green;'>Market availability: US only</b>

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
            url_template=self._server.default("/v3/advertising/sem/items/eligibility"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemItemEligibilityRequest | SemItemEligibilityRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCatalogueResponse],
            error_mapper=get_eligible_items_error_mapper,
            request_options=request_options,
        )

    async def get_item_recommendations(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 100,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCatalogueResponse, GetItemRecommendationsErrorBody]:
        """This API allows you to fetch a list of top recommended items from your catalog. You can customize the number
        of recommendations to be returned by adjusting the request parameter.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            limit: Specifies the maximum number of recommended items to be returned. This value cannot exceed 200.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/items/recommendations"),
            query_params=[param[int | None]("limit", limit)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCatalogueResponse],
            error_mapper=get_item_recommendations_error_mapper,
            request_options=request_options,
        )

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
from ..errors.post_contest_error import PostContestErrorBody, post_contest_error_mapper
from ..errors.post_status_error import PostStatusErrorBody, post_status_error_mapper
from ..models.dispute_contest_responses import DisputeContestResponses
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.v3_items_dispute_duplicates_contest_request import (
    V3ItemsDisputeDuplicatesContestRequest,
    V3ItemsDisputeDuplicatesContestRequestDict,
)
from ..models.v3_items_dispute_duplicates_status_request import (
    V3ItemsDisputeDuplicatesStatusRequest,
    V3ItemsDisputeDuplicatesStatusRequestDict,
)
from ..models.v3_items_dispute_duplicates_status_response import V3ItemsDisputeDuplicatesStatusResponse
from ..server.server import Server


class Disputes:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = DisputesWithRawResponse(client, server)

    def post_contest(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisputeContestResponses:
        """Use this API to submit dispute for up to 100 items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/contest
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden Not Found Internal Server Error ``error`` is ``V3ItemsDisputeDuplicatesContest403Error1
                | V3ItemsDisputeDuplicatesContest404Error1 | V3ItemsDisputeDuplicatesContest500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_contest(
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

    def post_status(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ItemsDisputeDuplicatesStatusResponse:
        """Use this API to retrieve the status of up to 100 disputed items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/status

        Responses will be based on the item status:

        * 404: No item Response

        * 200: Response received for all items

        * 206: Partial response received

        An Item can be in 4 different stages:
        * ``IN_REVIEW``, ``IS_DUPLICATE``, ``ERROR``, ``NOT_DUPLICATE``
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Response received for all the items.

        Raises:
            ApiError: Forbidden Not Found Internal Server Error ``error`` is ``V3ItemsDisputeDuplicatesStatus403Error1 |
                V3ItemsDisputeDuplicatesStatus404Error1 | V3ItemsDisputeDuplicatesStatus500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_status(
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
    def with_raw_response(self) -> DisputesWithRawResponse:
        return self._with_raw_response


class AsyncDisputes:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncDisputesWithRawResponse(client, server)

    async def post_contest(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DisputeContestResponses:
        """Use this API to submit dispute for up to 100 items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/contest
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden Not Found Internal Server Error ``error`` is ``V3ItemsDisputeDuplicatesContest403Error1
                | V3ItemsDisputeDuplicatesContest404Error1 | V3ItemsDisputeDuplicatesContest500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_contest(
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

    async def post_status(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ItemsDisputeDuplicatesStatusResponse:
        """Use this API to retrieve the status of up to 100 disputed items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/status

        Responses will be based on the item status:

        * 404: No item Response

        * 200: Response received for all items

        * 206: Partial response received

        An Item can be in 4 different stages:
        * ``IN_REVIEW``, ``IS_DUPLICATE``, ``ERROR``, ``NOT_DUPLICATE``
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Response received for all the items.

        Raises:
            ApiError: Forbidden Not Found Internal Server Error ``error`` is ``V3ItemsDisputeDuplicatesStatus403Error1 |
                V3ItemsDisputeDuplicatesStatus404Error1 | V3ItemsDisputeDuplicatesStatus500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_status(
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
    def with_raw_response(self) -> AsyncDisputesWithRawResponse:
        return self._with_raw_response


class DisputesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_contest(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisputeContestResponses, PostContestErrorBody]:
        """Use this API to submit dispute for up to 100 items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/contest
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/items/dispute/duplicates/contest"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict](body),
            decoder=json_decoder[DisputeContestResponses],
            error_mapper=post_contest_error_mapper,
            request_options=request_options,
        )

    def post_status(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ItemsDisputeDuplicatesStatusResponse, PostStatusErrorBody]:
        """Use this API to retrieve the status of up to 100 disputed items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/status

        Responses will be based on the item status:

        * 404: No item Response

        * 200: Response received for all items

        * 206: Partial response received

        An Item can be in 4 different stages:
        * ``IN_REVIEW``, ``IS_DUPLICATE``, ``ERROR``, ``NOT_DUPLICATE``
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/items/dispute/duplicates/status"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict](body),
            decoder=json_decoder[V3ItemsDisputeDuplicatesStatusResponse],
            error_mapper=post_status_error_mapper,
            request_options=request_options,
        )


class AsyncDisputesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_contest(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DisputeContestResponses, PostContestErrorBody]:
        """Use this API to submit dispute for up to 100 items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/contest
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/items/dispute/duplicates/contest"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict](body),
            decoder=async_json_decoder[DisputeContestResponses],
            error_mapper=post_contest_error_mapper,
            request_options=request_options,
        )

    async def post_status(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ItemsDisputeDuplicatesStatusResponse, PostStatusErrorBody]:
        """Use this API to retrieve the status of up to 100 disputed items at a time.

        We need to pass ``productId``, and ``productIdType`` in the body for creating a dispute.

        * POST {{url}}/v3/items/dispute/duplicates/status

        Responses will be based on the item status:

        * 404: No item Response

        * 200: Response received for all items

        * 206: Partial response received

        An Item can be in 4 different stages:
        * ``IN_REVIEW``, ``IS_DUPLICATE``, ``ERROR``, ``NOT_DUPLICATE``
        <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <strong style="color: green;">Market availability:
                Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <strong style="color: green;">Market availability: Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Required fields for the dispute.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/items/dispute/duplicates/status"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict](body),
            decoder=async_json_decoder[V3ItemsDisputeDuplicatesStatusResponse],
            error_mapper=post_status_error_mapper,
            request_options=request_options,
        )

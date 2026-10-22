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
from ..errors.get_billing_history_error import GetBillingHistoryErrorBody, get_billing_history_error_mapper
from ..errors.get_campaign_level_summary_error import (
    GetCampaignLevelSummaryErrorBody,
    get_campaign_level_summary_error_mapper,
)
from ..errors.get_item_level_summary_error import GetItemLevelSummaryErrorBody, get_item_level_summary_error_mapper
from ..models.sem_billing_history_request import SemBillingHistoryRequest, SemBillingHistoryRequestDict
from ..models.sem_billing_history_response import SemBillingHistoryResponse
from ..models.sem_campaign_level_report_response import SemCampaignLevelReportResponse
from ..models.sem_item_level_report_response import SemItemLevelReportResponse
from ..models.sem_report_request import SemReportRequest, SemReportRequestDict
from ..server.server import Server


class SemReporting:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SemReportingWithRawResponse(client, server, auth)

    def get_billing_history(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemBillingHistoryResponse:
        """This API allows you to fetch your billing history.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.get_billing_history(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    def get_campaign_level_summary(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignLevelReportResponse:
        """This API allows you to fetch comprehensive performance metrics for all campaigns, allowing you to analyze key
        performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.get_campaign_level_summary(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    def get_item_level_summary(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemItemLevelReportResponse:
        """This API allows you to fetch comprehensive performance metrics for all the items in a specific campaign,
        allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose item-level performance report is to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            self._with_raw_response.get_item_level_summary(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SemReportingWithRawResponse:
        return self._with_raw_response


class AsyncSemReporting:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSemReportingWithRawResponse(client, server, auth)

    async def get_billing_history(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemBillingHistoryResponse:
        """This API allows you to fetch your billing history.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_billing_history(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    async def get_campaign_level_summary(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemCampaignLevelReportResponse:
        """This API allows you to fetch comprehensive performance metrics for all campaigns, allowing you to analyze key
        performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_campaign_level_summary(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    async def get_item_level_summary(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SemItemLevelReportResponse:
        """This API allows you to fetch comprehensive performance metrics for all the items in a specific campaign,
        allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose item-level performance report is to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal server error ``error`` is ``SemErrorResponse400 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_item_level_summary(
                campaign_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSemReportingWithRawResponse:
        return self._with_raw_response


class SemReportingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_billing_history(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemBillingHistoryResponse, GetBillingHistoryErrorBody]:
        """This API allows you to fetch your billing history.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/billing-history"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemBillingHistoryRequest | SemBillingHistoryRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemBillingHistoryResponse],
            error_mapper=get_billing_history_error_mapper,
            request_options=request_options,
        )

    def get_campaign_level_summary(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignLevelReportResponse, GetCampaignLevelSummaryErrorBody]:
        """This API allows you to fetch comprehensive performance metrics for all campaigns, allowing you to analyze key
        performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/performance-summary"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemReportRequest | SemReportRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemCampaignLevelReportResponse],
            error_mapper=get_campaign_level_summary_error_mapper,
            request_options=request_options,
        )

    def get_item_level_summary(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemItemLevelReportResponse, GetItemLevelSummaryErrorBody]:
        """This API allows you to fetch comprehensive performance metrics for all the items in a specific campaign,
        allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose item-level performance report is to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}/item-level-summary"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemReportRequest | SemReportRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SemItemLevelReportResponse],
            error_mapper=get_item_level_summary_error_mapper,
            request_options=request_options,
        )


class AsyncSemReportingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_billing_history(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemBillingHistoryResponse, GetBillingHistoryErrorBody]:
        """This API allows you to fetch your billing history.<br><b style='color:green;'>Market availability: US
        only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/billing-history"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemBillingHistoryRequest | SemBillingHistoryRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemBillingHistoryResponse],
            error_mapper=get_billing_history_error_mapper,
            request_options=request_options,
        )

    async def get_campaign_level_summary(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemCampaignLevelReportResponse, GetCampaignLevelSummaryErrorBody]:
        """This API allows you to fetch comprehensive performance metrics for all campaigns, allowing you to analyze key
        performance indicators based on specified filtering and sorting criteria.<br><b style='color:green;'>Market
        availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/performance-summary"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemReportRequest | SemReportRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemCampaignLevelReportResponse],
            error_mapper=get_campaign_level_summary_error_mapper,
            request_options=request_options,
        )

    async def get_item_level_summary(
        self,
        campaign_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: SemReportRequest | SemReportRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SemItemLevelReportResponse, GetItemLevelSummaryErrorBody]:
        """This API allows you to fetch comprehensive performance metrics for all the items in a specific campaign,
        allowing you to analyze key performance indicators based on specified filtering and sorting criteria.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            campaign_id: Campaign ID of the campaign whose item-level performance report is to be retrieved.
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Request Payload
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/campaigns/{campaignId}/item-level-summary"),
            path_params=[param[str]("campaignId", campaign_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[SemReportRequest | SemReportRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SemItemLevelReportResponse],
            error_mapper=get_item_level_summary_error_mapper,
            request_options=request_options,
        )

from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncRawClient,
    BaseRawResponse,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    file_part,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.walmart_plus_enrollment_error import WalmartPlusEnrollmentErrorBody, walmart_plus_enrollment_error_mapper
from ..models.enums.feed_type3 import FeedType3OrStr
from ..models.enums.request_type import RequestTypeOrStr
from ..models.enums.wm_market import WmMarketOrStr
from ..models.v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff_response import (
    V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse,
)
from ..server.server import Server


class WalmartSellerFulfilled:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = WalmartSellerFulfilledWithRawResponse(client, server)

    def walmart_plus_enrollment(
        self,
        feed_type: FeedType3OrStr,
        request_type: RequestTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        file_name: FileInput,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse:
        """This API endpoint allows you to efficiently manage item participation in the Walmart+ program. Use it to
        enroll eligible items in Walmart+ or to unenroll items that are currently part of the program.<br><b
        style='color:green;'>Market availability: US</b>

        <b>Download and review the <a
        href="/file/mp/us/PROGRAM_ACTIONS_5.0.20250617-00_03_34_US_WalmartPlusEnrollment.xlsx">Excel template sample
        </a> and the <a href="/file/mp/us/bulk-enroll-requestBody-template.json">JSON body sample</a> to ensure proper
        formatting of the updated file before uploading it for processing.</b>

        Args:
            feed_type: The type of feed, which specifies the nature of the update.<br><b style='color:green;'>Market
                availability: US</b>
            request_type: Specifies the type of request for the Walmart+ SFF (Seller-Fulfilled) program.<br><b
                style='color:green;'>Market availability: US</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            file_name: Upload an Excel file or a JSON file containing the data for Walmart+ enrollment or
                unenrollment.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Indicates successful operation. The response provides details on both successful and failed item enrollments
            or unenrollments, allowing you to review which items were updated and which encountered issues.

        Raises:
            ApiError: Bad Request Internal Server Error ``error`` is
                ``V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1 |
                V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.walmart_plus_enrollment(
                feed_type,
                request_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                file_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> WalmartSellerFulfilledWithRawResponse:
        return self._with_raw_response


class AsyncWalmartSellerFulfilled:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncWalmartSellerFulfilledWithRawResponse(client, server)

    async def walmart_plus_enrollment(
        self,
        feed_type: FeedType3OrStr,
        request_type: RequestTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        file_name: AsyncFileInput,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse:
        """This API endpoint allows you to efficiently manage item participation in the Walmart+ program. Use it to
        enroll eligible items in Walmart+ or to unenroll items that are currently part of the program.<br><b
        style='color:green;'>Market availability: US</b>

        <b>Download and review the <a
        href="/file/mp/us/PROGRAM_ACTIONS_5.0.20250617-00_03_34_US_WalmartPlusEnrollment.xlsx">Excel template sample
        </a> and the <a href="/file/mp/us/bulk-enroll-requestBody-template.json">JSON body sample</a> to ensure proper
        formatting of the updated file before uploading it for processing.</b>

        Args:
            feed_type: The type of feed, which specifies the nature of the update.<br><b style='color:green;'>Market
                availability: US</b>
            request_type: Specifies the type of request for the Walmart+ SFF (Seller-Fulfilled) program.<br><b
                style='color:green;'>Market availability: US</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            file_name: Upload an Excel file or a JSON file containing the data for Walmart+ enrollment or
                unenrollment.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Indicates successful operation. The response provides details on both successful and failed item enrollments
            or unenrollments, allowing you to review which items were updated and which encountered issues.

        Raises:
            ApiError: Bad Request Internal Server Error ``error`` is
                ``V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1 |
                V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.walmart_plus_enrollment(
                feed_type,
                request_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                file_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWalmartSellerFulfilledWithRawResponse:
        return self._with_raw_response


class WalmartSellerFulfilledWithRawResponse(BaseRawResponse[RawClient, Server]):
    def walmart_plus_enrollment(
        self,
        feed_type: FeedType3OrStr,
        request_type: RequestTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        file_name: FileInput,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse, WalmartPlusEnrollmentErrorBody]:
        """This API endpoint allows you to efficiently manage item participation in the Walmart+ program. Use it to
        enroll eligible items in Walmart+ or to unenroll items that are currently part of the program.<br><b
        style='color:green;'>Market availability: US</b>

        <b>Download and review the <a
        href="/file/mp/us/PROGRAM_ACTIONS_5.0.20250617-00_03_34_US_WalmartPlusEnrollment.xlsx">Excel template sample
        </a> and the <a href="/file/mp/us/bulk-enroll-requestBody-template.json">JSON body sample</a> to ensure proper
        formatting of the updated file before uploading it for processing.</b>

        Args:
            feed_type: The type of feed, which specifies the nature of the update.<br><b style='color:green;'>Market
                availability: US</b>
            request_type: Specifies the type of request for the Walmart+ SFF (Seller-Fulfilled) program.<br><b
                style='color:green;'>Market availability: US</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            file_name: Upload an Excel file or a JSON file containing the data for Walmart+ enrollment or
                unenrollment.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PROGRAM_ACTIONS&requestType=WALMART_PLUS_SFF"),
            query_params=[
                param[FeedType3OrStr]("feedType", feed_type), param[RequestTypeOrStr]("requestType", request_type)
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("fileName", file_name)),
            decoder=json_decoder[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse],
            error_mapper=walmart_plus_enrollment_error_mapper,
            request_options=request_options,
        )


class AsyncWalmartSellerFulfilledWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def walmart_plus_enrollment(
        self,
        feed_type: FeedType3OrStr,
        request_type: RequestTypeOrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        file_name: AsyncFileInput,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse, WalmartPlusEnrollmentErrorBody]:
        """This API endpoint allows you to efficiently manage item participation in the Walmart+ program. Use it to
        enroll eligible items in Walmart+ or to unenroll items that are currently part of the program.<br><b
        style='color:green;'>Market availability: US</b>

        <b>Download and review the <a
        href="/file/mp/us/PROGRAM_ACTIONS_5.0.20250617-00_03_34_US_WalmartPlusEnrollment.xlsx">Excel template sample
        </a> and the <a href="/file/mp/us/bulk-enroll-requestBody-template.json">JSON body sample</a> to ensure proper
        formatting of the updated file before uploading it for processing.</b>

        Args:
            feed_type: The type of feed, which specifies the nature of the update.<br><b style='color:green;'>Market
                availability: US</b>
            request_type: Specifies the type of request for the Walmart+ SFF (Seller-Fulfilled) program.<br><b
                style='color:green;'>Market availability: US</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            file_name: Upload an Excel file or a JSON file containing the data for Walmart+ enrollment or
                unenrollment.<br><b style='color:green;'>Market availability: US</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PROGRAM_ACTIONS&requestType=WALMART_PLUS_SFF"),
            query_params=[
                param[FeedType3OrStr]("feedType", feed_type), param[RequestTypeOrStr]("requestType", request_type)
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("fileName", file_name)),
            decoder=async_json_decoder[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse],
            error_mapper=walmart_plus_enrollment_error_mapper,
            request_options=request_options,
        )

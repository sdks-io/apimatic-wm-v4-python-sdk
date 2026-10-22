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
from ..errors.generate_report_error import GenerateReportErrorBody, generate_report_error_mapper
from ..models.enums.report_type4 import ReportType4OrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.v3_reports_report_requests_request import (
    V3ReportsReportRequestsRequest,
    V3ReportsReportRequestsRequestDict,
)
from ..models.v3_reports_report_requests_response1 import V3ReportsReportRequestsResponse1
from ..server.server import Server


class OnRequestReport:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OnRequestReportWithRawResponse(client, server, auth)

    def generate_report(
        self,
        report_type: ReportType4OrStr,
        report_version: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsReportRequestsResponse1:
        """Creates a new request for report by specifying the ``reportType`` and ``reportVersion``. <br><b
        style='color:green;'>Market availability: Global</b>

        **Max reporting window:** For ``ITEM_PERFORMANCE`` v3, the date range between ``dataStartTime`` and
        ``dataEndTime`` must not exceed 2 years (730 days). Exceeding this limit will return a ``400`` error.

        **Row limit:** There is no limit on the number of rows returned in the report.

        Args:
            report_type: Type of report for which the request is created. Example, ITEM for Item Report. <strong
                style="color: green;">Market availability: ITEM: Global INVENTORY: Global LAGTIME: US|CA|MX Other
                Reports: US only</strong>
            report_version: Version of report for which the request is created. <strong style="color: green;">Market
                availability: Global</strong> |ReportType |Market Availabilty |Version Supported
                |--------|----------|---------- | ITEM |Global| v1 (**v3 to v6 : US only**) |INVENTORY|Global| v1
                |LAGTIME|US,CA,MX| v1 |DELIVERY_DEFECT|US only| v1 |ITEM_PERFORMANCE|US only| v1 to v3 |PROMO|US only|
                v1 |RETURN_OVERRIDES|US only| v1 |CPA|US only| v1 |SHIPPING_CONFIGURATION|US only| v1
                |SHIPPING_PROGRAM|US only| v1 |FITMENT_MISSING_ATTR|US only| v1 |FITMENT_ACES_COVERAGE|US only| v1
                |BUYBOX|US only| v1 |ASSORTMENT_RECOMMENDATIONS|US only| v1 |CANCELLATION|US only| v1
                |INVENTORY_RECOMMENDATIONS|US only| v1 |
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            accept: Only supported Media Type : application/json <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request. The request contains invalid or missing parameters. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.generate_report(
                report_type,
                report_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> OnRequestReportWithRawResponse:
        return self._with_raw_response


class AsyncOnRequestReport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOnRequestReportWithRawResponse(client, server, auth)

    async def generate_report(
        self,
        report_type: ReportType4OrStr,
        report_version: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsReportRequestsResponse1:
        """Creates a new request for report by specifying the ``reportType`` and ``reportVersion``. <br><b
        style='color:green;'>Market availability: Global</b>

        **Max reporting window:** For ``ITEM_PERFORMANCE`` v3, the date range between ``dataStartTime`` and
        ``dataEndTime`` must not exceed 2 years (730 days). Exceeding this limit will return a ``400`` error.

        **Row limit:** There is no limit on the number of rows returned in the report.

        Args:
            report_type: Type of report for which the request is created. Example, ITEM for Item Report. <strong
                style="color: green;">Market availability: ITEM: Global INVENTORY: Global LAGTIME: US|CA|MX Other
                Reports: US only</strong>
            report_version: Version of report for which the request is created. <strong style="color: green;">Market
                availability: Global</strong> |ReportType |Market Availabilty |Version Supported
                |--------|----------|---------- | ITEM |Global| v1 (**v3 to v6 : US only**) |INVENTORY|Global| v1
                |LAGTIME|US,CA,MX| v1 |DELIVERY_DEFECT|US only| v1 |ITEM_PERFORMANCE|US only| v1 to v3 |PROMO|US only|
                v1 |RETURN_OVERRIDES|US only| v1 |CPA|US only| v1 |SHIPPING_CONFIGURATION|US only| v1
                |SHIPPING_PROGRAM|US only| v1 |FITMENT_MISSING_ATTR|US only| v1 |FITMENT_ACES_COVERAGE|US only| v1
                |BUYBOX|US only| v1 |ASSORTMENT_RECOMMENDATIONS|US only| v1 |CANCELLATION|US only| v1
                |INVENTORY_RECOMMENDATIONS|US only| v1 |
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            accept: Only supported Media Type : application/json <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request. The request contains invalid or missing parameters. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.generate_report(
                report_type,
                report_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOnRequestReportWithRawResponse:
        return self._with_raw_response


class OnRequestReportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def generate_report(
        self,
        report_type: ReportType4OrStr,
        report_version: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsReportRequestsResponse1, GenerateReportErrorBody]:
        """Creates a new request for report by specifying the ``reportType`` and ``reportVersion``. <br><b
        style='color:green;'>Market availability: Global</b>

        **Max reporting window:** For ``ITEM_PERFORMANCE`` v3, the date range between ``dataStartTime`` and
        ``dataEndTime`` must not exceed 2 years (730 days). Exceeding this limit will return a ``400`` error.

        **Row limit:** There is no limit on the number of rows returned in the report.

        Args:
            report_type: Type of report for which the request is created. Example, ITEM for Item Report. <strong
                style="color: green;">Market availability: ITEM: Global INVENTORY: Global LAGTIME: US|CA|MX Other
                Reports: US only</strong>
            report_version: Version of report for which the request is created. <strong style="color: green;">Market
                availability: Global</strong> |ReportType |Market Availabilty |Version Supported
                |--------|----------|---------- | ITEM |Global| v1 (**v3 to v6 : US only**) |INVENTORY|Global| v1
                |LAGTIME|US,CA,MX| v1 |DELIVERY_DEFECT|US only| v1 |ITEM_PERFORMANCE|US only| v1 to v3 |PROMO|US only|
                v1 |RETURN_OVERRIDES|US only| v1 |CPA|US only| v1 |SHIPPING_CONFIGURATION|US only| v1
                |SHIPPING_PROGRAM|US only| v1 |FITMENT_MISSING_ATTR|US only| v1 |FITMENT_ACES_COVERAGE|US only| v1
                |BUYBOX|US only| v1 |ASSORTMENT_RECOMMENDATIONS|US only| v1 |CANCELLATION|US only| v1
                |INVENTORY_RECOMMENDATIONS|US only| v1 |
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            accept: Only supported Media Type : application/json <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/reports/reportRequests"),
            query_params=[
                param[ReportType4OrStr]("reportType", report_type), param[str]("reportVersion", report_version)
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ReportsReportRequestsResponse1],
            error_mapper=generate_report_error_mapper,
            request_options=request_options,
        )


class AsyncOnRequestReportWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def generate_report(
        self,
        report_type: ReportType4OrStr,
        report_version: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsReportRequestsResponse1, GenerateReportErrorBody]:
        """Creates a new request for report by specifying the ``reportType`` and ``reportVersion``. <br><b
        style='color:green;'>Market availability: Global</b>

        **Max reporting window:** For ``ITEM_PERFORMANCE`` v3, the date range between ``dataStartTime`` and
        ``dataEndTime`` must not exceed 2 years (730 days). Exceeding this limit will return a ``400`` error.

        **Row limit:** There is no limit on the number of rows returned in the report.

        Args:
            report_type: Type of report for which the request is created. Example, ITEM for Item Report. <strong
                style="color: green;">Market availability: ITEM: Global INVENTORY: Global LAGTIME: US|CA|MX Other
                Reports: US only</strong>
            report_version: Version of report for which the request is created. <strong style="color: green;">Market
                availability: Global</strong> |ReportType |Market Availabilty |Version Supported
                |--------|----------|---------- | ITEM |Global| v1 (**v3 to v6 : US only**) |INVENTORY|Global| v1
                |LAGTIME|US,CA,MX| v1 |DELIVERY_DEFECT|US only| v1 |ITEM_PERFORMANCE|US only| v1 to v3 |PROMO|US only|
                v1 |RETURN_OVERRIDES|US only| v1 |CPA|US only| v1 |SHIPPING_CONFIGURATION|US only| v1
                |SHIPPING_PROGRAM|US only| v1 |FITMENT_MISSING_ATTR|US only| v1 |FITMENT_ACES_COVERAGE|US only| v1
                |BUYBOX|US only| v1 |ASSORTMENT_RECOMMENDATIONS|US only| v1 |CANCELLATION|US only| v1
                |INVENTORY_RECOMMENDATIONS|US only| v1 |
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            accept: Only supported Media Type : application/json <strong style="color: green;">Market availability:
                Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            body: Request body
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/reports/reportRequests"),
            query_params=[
                param[ReportType4OrStr]("reportType", report_type), param[str]("reportVersion", report_version)
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ReportsReportRequestsResponse1],
            error_mapper=generate_report_error_mapper,
            request_options=request_options,
        )

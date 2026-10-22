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
from ..errors.get_recon_report_error import GetReconReportErrorBody, get_recon_report_error_mapper
from ..errors.get_recon_report_v1_error import GetReconReportV1ErrorBody, get_recon_report_v1_error_mapper
from ..models.partner_program_performance_res import PartnerProgramPerformanceRes
from ..models.partner_program_statement_res import PartnerProgramStatementRes
from ..models.recon_report_date_response import ReconReportDateResponse
from ..models.recon_report_v1_as_json_response import ReconReportV1AsJsonResponse
from ..server.server import Server


class ReportsApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReportsApiWithRawResponse(client, server, auth)

    def get_available_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportDateResponse:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_available_recon_report_dates(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_available_v1_recon_report_as_json(
        self,
        report_date: str,
        offset: int,
        no_of_records: int,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportV1AsJsonResponse:
        """This API will get a partner’s transaction details in JSON format for a specific date range (available only
        for v1 reports). Dates for accessing the report can be found by using the ‘GET Available recon report dates’
        API.

        Args:
            report_date: Date of the settlement report
            offset: starting number of the bytes, initial value for the offset is zero
            no_of_records: number of records in the report (max limit 1000)
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_available_v1_recon_report_as_json(
                report_date,
                offset,
                no_of_records,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_available_v1_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportDateResponse:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_available_v1_recon_report_dates(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_partner_performance(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PartnerProgramPerformanceRes:
        """This API will get a partner's current cycle performance

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_partner_performance(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_partner_statement(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PartnerProgramStatementRes:
        """This API will get a partner's current cycle statement

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_partner_statement(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_recon_report(
        self,
        report_date: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponse:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Failure Operation ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_recon_report(
                report_date,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_recon_report_v1(
        self,
        report_date: str,
        report_version: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponse:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            report_version: Report Version
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Failure Operation ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_recon_report_v1(
                report_date,
                report_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ReportsApiWithRawResponse:
        return self._with_raw_response


class AsyncReportsApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReportsApiWithRawResponse(client, server, auth)

    async def get_available_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportDateResponse:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_available_recon_report_dates(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_available_v1_recon_report_as_json(
        self,
        report_date: str,
        offset: int,
        no_of_records: int,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportV1AsJsonResponse:
        """This API will get a partner’s transaction details in JSON format for a specific date range (available only
        for v1 reports). Dates for accessing the report can be found by using the ‘GET Available recon report dates’
        API.

        Args:
            report_date: Date of the settlement report
            offset: starting number of the bytes, initial value for the offset is zero
            no_of_records: number of records in the report (max limit 1000)
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_available_v1_recon_report_as_json(
                report_date,
                offset,
                no_of_records,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_available_v1_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReconReportDateResponse:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_available_v1_recon_report_dates(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_partner_performance(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PartnerProgramPerformanceRes:
        """This API will get a partner's current cycle performance

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_partner_performance(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_partner_statement(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PartnerProgramStatementRes:
        """This API will get a partner's current cycle statement

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_partner_statement(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_recon_report(
        self,
        report_date: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsyncFileResponse:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Failure Operation ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_recon_report(
                report_date,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_recon_report_v1(
        self,
        report_date: str,
        report_version: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsyncFileResponse:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            report_version: Report Version
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Failure Operation ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_recon_report_v1(
                report_date,
                report_version,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReportsApiWithRawResponse:
        return self._with_raw_response


class ReportsApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_available_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportDateResponse, RawError]:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/availableReconFiles"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ReconReportDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_available_v1_recon_report_as_json(
        self,
        report_date: str,
        offset: int,
        no_of_records: int,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportV1AsJsonResponse, RawError]:
        """This API will get a partner’s transaction details in JSON format for a specific date range (available only
        for v1 reports). Dates for accessing the report can be found by using the ‘GET Available recon report dates’
        API.

        Args:
            report_date: Date of the settlement report
            offset: starting number of the bytes, initial value for the offset is zero
            no_of_records: number of records in the report (max limit 1000)
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFileJson"),
            query_params=[
                param[str]("reportDate", report_date),
                param[int]("offset", offset),
                param[int]("noOfRecords", no_of_records),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ReconReportV1AsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_available_v1_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportDateResponse, RawError]:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/availableReconFiles?reportVersion=v1"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ReconReportDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_partner_performance(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PartnerProgramPerformanceRes, RawError]:
        """This API will get a partner's current cycle performance

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/payment/performance"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[PartnerProgramPerformanceRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_partner_statement(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PartnerProgramStatementRes, RawError]:
        """This API will get a partner's current cycle statement

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/payment/statement"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[PartnerProgramStatementRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_recon_report(
        self,
        report_date: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponse, GetReconReportErrorBody]:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFile"),
            query_params=[param[str]("reportDate", report_date)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=file_decoder,
            error_mapper=get_recon_report_error_mapper,
            request_options=request_options,
        )

    def get_recon_report_v1(
        self,
        report_date: str,
        report_version: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponse, GetReconReportV1ErrorBody]:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            report_version: Report Version
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFile?reportVersion=v1"),
            query_params=[param[str]("reportDate", report_date), param[str]("reportVersion", report_version)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=file_decoder,
            error_mapper=get_recon_report_v1_error_mapper,
            request_options=request_options,
        )


class AsyncReportsApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_available_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportDateResponse, RawError]:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/availableReconFiles"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ReconReportDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_available_v1_recon_report_as_json(
        self,
        report_date: str,
        offset: int,
        no_of_records: int,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportV1AsJsonResponse, RawError]:
        """This API will get a partner’s transaction details in JSON format for a specific date range (available only
        for v1 reports). Dates for accessing the report can be found by using the ‘GET Available recon report dates’
        API.

        Args:
            report_date: Date of the settlement report
            offset: starting number of the bytes, initial value for the offset is zero
            no_of_records: number of records in the report (max limit 1000)
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFileJson"),
            query_params=[
                param[str]("reportDate", report_date),
                param[int]("offset", offset),
                param[int]("noOfRecords", no_of_records),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ReconReportV1AsJsonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_available_v1_recon_report_dates(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReconReportDateResponse, RawError]:
        """This API will list all the available Marketplace reconciliation report dates for the Seller.

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/availableReconFiles?reportVersion=v1"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ReconReportDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_partner_performance(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PartnerProgramPerformanceRes, RawError]:
        """This API will get a partner's current cycle performance

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/payment/performance"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[PartnerProgramPerformanceRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_partner_statement(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PartnerProgramStatementRes, RawError]:
        """This API will get a partner's current cycle statement

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/payment/statement"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[PartnerProgramStatementRes],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_recon_report(
        self,
        report_date: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsyncFileResponse, GetReconReportErrorBody]:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFile"),
            query_params=[param[str]("reportDate", report_date)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_file_decoder,
            error_mapper=get_recon_report_error_mapper,
            request_options=request_options,
        )

    async def get_recon_report_v1(
        self,
        report_date: str,
        report_version: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsyncFileResponse, GetReconReportV1ErrorBody]:
        """Seller can download the reconciliation report for a specific date using this API. Dates available to be
        downloaded can be found by using the Get available reconciliation report dates API.

        Args:
            report_date: The date for which the reconcilation file is available
            report_version: Report Version
            wm_sec_access_token: The access token retrieved in the Token API call
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            wm_svc_name: Walmart Service Name
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/report/reconreport/reconFile?reportVersion=v1"),
            query_params=[param[str]("reportDate", report_date), param[str]("reportVersion", report_version)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_file_decoder,
            error_mapper=get_recon_report_v1_error_mapper,
            request_options=request_options,
        )

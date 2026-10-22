from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.report_type10 import ReportType10OrStr
from ..models.reject_recommendations_response_payload import RejectRecommendationsResponsePayload
from ..models.v3_reports_schedules_request import V3ReportsSchedulesRequest, V3ReportsSchedulesRequestDict
from ..models.v3_reports_schedules_response import V3ReportsSchedulesResponse
from ..models.v3_reports_schedules_response1 import V3ReportsSchedulesResponse1
from ..server.server import Server


class ReportScheduler:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReportSchedulerWithRawResponse(client, server, auth)

    def delete_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """This API allows you to remove an existing report schedule.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    def get_all_report_schedules(
        self,
        report_type: ReportType10OrStr,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse:
        """The Get All Report Schedules API retrieves a list of all existing report schedules. This helps you to easily
        view and manage all scheduled reports in one place.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            report_type: Specifies the type of report to be generated. Example: ITEM for Item Report.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_all_report_schedules(
                report_type, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    def get_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse1:
        """This API retrieves the details of a single report schedule based on the specified scheduleId.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: Value sent with the request.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    def update_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse1:
        """This API allows you to modify an existing report schedule. You can change the parameters to better suit your
        needs, ensuring that reports are generated and delivered according to the most current requirements.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ReportSchedulerWithRawResponse:
        return self._with_raw_response


class AsyncReportScheduler:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReportSchedulerWithRawResponse(client, server, auth)

    async def delete_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RejectRecommendationsResponsePayload:
        """This API allows you to remove an existing report schedule.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    async def get_all_report_schedules(
        self,
        report_type: ReportType10OrStr,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse:
        """The Get All Report Schedules API retrieves a list of all existing report schedules. This helps you to easily
        view and manage all scheduled reports in one place.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            report_type: Specifies the type of report to be generated. Example: ITEM for Item Report.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_all_report_schedules(
                report_type, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    async def get_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse1:
        """This API retrieves the details of a single report schedule based on the specified scheduleId.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: Value sent with the request.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, request_options=request_options
            ),
        )

    async def update_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ReportsSchedulesResponse1:
        """This API allows you to modify an existing report schedule. You can change the parameters to better suit your
        needs, ensuring that reports are generated and delivered according to the most current requirements.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_report_schedule(
                schedule_id, wm_svc_name, wm_qos_correlation_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReportSchedulerWithRawResponse:
        return self._with_raw_response


class ReportSchedulerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, RawError]:
        """This API allows you to remove an existing report schedule.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_all_report_schedules(
        self,
        report_type: ReportType10OrStr,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse, RawError]:
        """The Get All Report Schedules API retrieves a list of all existing report schedules. This helps you to easily
        view and manage all scheduled reports in one place.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            report_type: Specifies the type of report to be generated. Example: ITEM for Item Report.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/reports/schedules"),
            query_params=[param[ReportType10OrStr]("reportType", report_type)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name), param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id)
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ReportsSchedulesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse1, RawError]:
        """This API retrieves the details of a single report schedule based on the specified scheduleId.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: Value sent with the request.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name), param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id)
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ReportsSchedulesResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse1, RawError]:
        """This API allows you to modify an existing report schedule. You can change the parameters to better suit your
        needs, ensuring that reports are generated and delivered according to the most current requirements.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ReportsSchedulesResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncReportSchedulerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RejectRecommendationsResponsePayload, RawError]:
        """This API allows you to remove an existing report schedule.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[RejectRecommendationsResponsePayload],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_all_report_schedules(
        self,
        report_type: ReportType10OrStr,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse, RawError]:
        """The Get All Report Schedules API retrieves a list of all existing report schedules. This helps you to easily
        view and manage all scheduled reports in one place.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            report_type: Specifies the type of report to be generated. Example: ITEM for Item Report.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/reports/schedules"),
            query_params=[param[ReportType10OrStr]("reportType", report_type)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name), param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id)
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ReportsSchedulesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse1, RawError]:
        """This API retrieves the details of a single report schedule based on the specified scheduleId.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: Value sent with the request.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name), param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id)
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ReportsSchedulesResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_report_schedule(
        self,
        schedule_id: str,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ReportsSchedulesResponse1, RawError]:
        """This API allows you to modify an existing report schedule. You can change the parameters to better suit your
        needs, ensuring that reports are generated and delivered according to the most current requirements.

        <strong style="color: green;">Market availability: US only</strong>

        Args:
            schedule_id: A unique identifier assigned to the report schedule.
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/reports/schedules/{scheduleId}"),
            path_params=[param[str]("scheduleId", schedule_id)],
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ReportsSchedulesResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

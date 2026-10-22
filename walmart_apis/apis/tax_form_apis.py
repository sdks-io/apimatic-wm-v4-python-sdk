from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_decoder,
    param,
    unwrap,
)
from ..errors.download_tax_form_error import DownloadTaxFormErrorBody, download_tax_form_error_mapper
from ..errors.get_tax_forms_error import GetTaxFormsErrorBody, get_tax_forms_error_mapper
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.v1_settings_gettaxformprofile_response import V1SettingsGettaxformprofileResponse
from ..server.server import Server


class TaxFormApis:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TaxFormApisWithRawResponse(client, server, auth)

    def download_tax_form(
        self,
        payout_year: str,
        tax_form_type: str,
        form_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """The Download Tax Form API downloads the selected tax form document as a byte stream.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            payout_year: The tax year associated with the payout (for example, 2024). <br><b style='color:green;'>Market
                availability: US only</b>
            tax_form_type: The tax form type to download (for example, 1099-K).<br><b style='color:green;'>Market
                availability: US only</b>
            form_id: The unique form ID returned by the list tax forms endpoint.<br><b style='color:green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tax form bytes returned.

        Raises:
            ApiError: Error calling downstream service. No record found for the given parameters. Missing mandatory
                input parameters. Internal server error occurred while processing the request. ``error`` is
                ``V1SettingsDownloadtaxformprofile400Error1 | V1SettingsDownloadtaxformprofile404Error1 |
                V1SettingsDownloadtaxformprofile500Error1 | V1SettingsDownloadtaxformprofile502Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.download_tax_form(
                payout_year,
                tax_form_type,
                form_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_global_version,
                wm_market,
                wm_partner_id,
                wm_tenant_id,
                request_options=request_options,
            ),
        )

    def get_tax_forms(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1SettingsGettaxformprofileResponse:
        """The Get Tax Forms API returns available tax forms for the authenticated seller, including form type and form
        ID. The response is a JSON object containing tax form metadata.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier for multi-tenant contexts. <br><b style='color:green;'>Market
                availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tax forms retrieved successfully.

        Raises:
            ApiError: No record found for the given parameters. Missing mandatory input parameters. Internal server
                error occurred while processing the request. ``error`` is ``V1SettingsGettaxformprofile400Error1 |
                V1SettingsGettaxformprofile404Error1 | V1SettingsGettaxformprofile500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_tax_forms(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_global_version,
                wm_market,
                wm_partner_id,
                wm_tenant_id,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> TaxFormApisWithRawResponse:
        return self._with_raw_response


class AsyncTaxFormApis:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTaxFormApisWithRawResponse(client, server, auth)

    async def download_tax_form(
        self,
        payout_year: str,
        tax_form_type: str,
        form_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """The Download Tax Form API downloads the selected tax form document as a byte stream.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            payout_year: The tax year associated with the payout (for example, 2024). <br><b style='color:green;'>Market
                availability: US only</b>
            tax_form_type: The tax form type to download (for example, 1099-K).<br><b style='color:green;'>Market
                availability: US only</b>
            form_id: The unique form ID returned by the list tax forms endpoint.<br><b style='color:green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tax form bytes returned.

        Raises:
            ApiError: Error calling downstream service. No record found for the given parameters. Missing mandatory
                input parameters. Internal server error occurred while processing the request. ``error`` is
                ``V1SettingsDownloadtaxformprofile400Error1 | V1SettingsDownloadtaxformprofile404Error1 |
                V1SettingsDownloadtaxformprofile500Error1 | V1SettingsDownloadtaxformprofile502Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.download_tax_form(
                payout_year,
                tax_form_type,
                form_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_global_version,
                wm_market,
                wm_partner_id,
                wm_tenant_id,
                request_options=request_options,
            ),
        )

    async def get_tax_forms(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1SettingsGettaxformprofileResponse:
        """The Get Tax Forms API returns available tax forms for the authenticated seller, including form type and form
        ID. The response is a JSON object containing tax form metadata.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier for multi-tenant contexts. <br><b style='color:green;'>Market
                availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tax forms retrieved successfully.

        Raises:
            ApiError: No record found for the given parameters. Missing mandatory input parameters. Internal server
                error occurred while processing the request. ``error`` is ``V1SettingsGettaxformprofile400Error1 |
                V1SettingsGettaxformprofile404Error1 | V1SettingsGettaxformprofile500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_tax_forms(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_global_version,
                wm_market,
                wm_partner_id,
                wm_tenant_id,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTaxFormApisWithRawResponse:
        return self._with_raw_response


class TaxFormApisWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def download_tax_form(
        self,
        payout_year: str,
        tax_form_type: str,
        form_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DownloadTaxFormErrorBody]:
        """The Download Tax Form API downloads the selected tax form document as a byte stream.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            payout_year: The tax year associated with the payout (for example, 2024). <br><b style='color:green;'>Market
                availability: US only</b>
            tax_form_type: The tax form type to download (for example, 1099-K).<br><b style='color:green;'>Market
                availability: US only</b>
            form_id: The unique form ID returned by the list tax forms endpoint.<br><b style='color:green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/settings/downloadtaxformprofile"),
            query_params=[
                param[str]("payoutYear", payout_year),
                param[str]("taxFormType", tax_form_type),
                param[str]("formId", form_id),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("WM_PARTNER_ID", wm_partner_id),
                param[str]("WM.TENANT_ID", wm_tenant_id),
            ],
            auth_scheme=self._auth.access_token,
            decoder=empty_response,
            error_mapper=download_tax_form_error_mapper,
            request_options=request_options,
        )

    def get_tax_forms(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1SettingsGettaxformprofileResponse, GetTaxFormsErrorBody]:
        """The Get Tax Forms API returns available tax forms for the authenticated seller, including form type and form
        ID. The response is a JSON object containing tax form metadata.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier for multi-tenant contexts. <br><b style='color:green;'>Market
                availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/settings/gettaxformprofile"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("WM_PARTNER_ID", wm_partner_id),
                param[str]("WM.TENANT_ID", wm_tenant_id),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V1SettingsGettaxformprofileResponse],
            error_mapper=get_tax_forms_error_mapper,
            request_options=request_options,
        )


class AsyncTaxFormApisWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def download_tax_form(
        self,
        payout_year: str,
        tax_form_type: str,
        form_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DownloadTaxFormErrorBody]:
        """The Download Tax Form API downloads the selected tax form document as a byte stream.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            payout_year: The tax year associated with the payout (for example, 2024). <br><b style='color:green;'>Market
                availability: US only</b>
            tax_form_type: The tax form type to download (for example, 1099-K).<br><b style='color:green;'>Market
                availability: US only</b>
            form_id: The unique form ID returned by the list tax forms endpoint.<br><b style='color:green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/settings/downloadtaxformprofile"),
            query_params=[
                param[str]("payoutYear", payout_year),
                param[str]("taxFormType", tax_form_type),
                param[str]("formId", form_id),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("WM_PARTNER_ID", wm_partner_id),
                param[str]("WM.TENANT_ID", wm_tenant_id),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_empty_response,
            error_mapper=download_tax_form_error_mapper,
            request_options=request_options,
        )

    async def get_tax_forms(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_global_version: WmGlobalVersionOrStr,
        wm_market: str,
        wm_partner_id: str,
        wm_tenant_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1SettingsGettaxformprofileResponse, GetTaxFormsErrorBody]:
        """The Get Tax Forms API returns available tax forms for the authenticated seller, including form type and form
        ID. The response is a JSON object containing tax form metadata.

        <b style='color:green;'>Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <br><b style='color:green;'>Market availability: Global</b>
            wm_partner_id: The partner (seller) identifier registered in Walmart Marketplace. <br><b
                style='color:green;'>Market availability: Global</b>
            wm_tenant_id: Specifies the tenant identifier for multi-tenant contexts. <br><b style='color:green;'>Market
                availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/settings/gettaxformprofile"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("WM_PARTNER_ID", wm_partner_id),
                param[str]("WM.TENANT_ID", wm_tenant_id),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V1SettingsGettaxformprofileResponse],
            error_mapper=get_tax_forms_error_mapper,
            request_options=request_options,
        )

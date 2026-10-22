from __future__ import annotations

from uuid import UUID, uuid4

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
    async_empty_response,
    async_file_decoder,
    async_json_decoder,
    empty_response,
    file_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.create_label_error import CreateLabelErrorBody, create_label_error_mapper
from ..errors.create_label_mps_error import CreateLabelMpsErrorBody, create_label_mps_error_mapper
from ..errors.discard_label_error import DiscardLabelErrorBody, discard_label_error_mapper
from ..errors.get_shipping_estimate_error import GetShippingEstimateErrorBody, get_shipping_estimate_error_mapper
from ..errors.scan_form_error import ScanFormErrorBody, scan_form_error_mapper
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market import WmMarketOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.enums.wm_market6 import WmMarket6OrStr
from ..models.enums.wm_market11 import WmMarket11OrStr
from ..models.v3_shipping_labels_carriers_package_types_response import V3ShippingLabelsCarriersPackageTypesResponse
from ..models.v3_shipping_labels_carriers_response import V3ShippingLabelsCarriersResponse
from ..models.v3_shipping_labels_carriers_trackings_response import V3ShippingLabelsCarriersTrackingsResponse
from ..models.v3_shipping_labels_purchase_orders_response import V3ShippingLabelsPurchaseOrdersResponse
from ..models.v3_shipping_labels_request import V3ShippingLabelsRequest, V3ShippingLabelsRequestDict
from ..models.v3_shipping_labels_response import V3ShippingLabelsResponse
from ..models.v3_shipping_labels_shipping_estimates_request import (
    V3ShippingLabelsShippingEstimatesRequest,
    V3ShippingLabelsShippingEstimatesRequestDict,
)
from ..models.v3_shipping_labels_shipping_estimates_response import V3ShippingLabelsShippingEstimatesResponse
from ..models.v3_shipping_multi_package_labels_request import (
    V3ShippingMultiPackageLabelsRequest,
    V3ShippingMultiPackageLabelsRequestDict,
)
from ..models.v3_shipping_multi_package_labels_response import V3ShippingMultiPackageLabelsResponse
from ..models.v3_shipping_scan_form_request import V3ShippingScanFormRequest, V3ShippingScanFormRequestDict
from ..models.v3_shipping_scan_form_response import V3ShippingScanFormResponse
from ..server.server import Server


class ShipWithWalmart:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShipWithWalmartWithRawResponse(client, server, auth)

    def create_label(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsResponse:
        """Generates a shipping label using the provided shipment information. A successful response includes a tracking
        number and a label file in the media type specified in the Accept header.<br><br>This API is supported for
        <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>• application/json, application/pdf →
        Returns label in PDF format. • application/json, image/png → Returns label in PNG format. • application/json →
        Returns tracking info only in JSON. <br><br> <b>Note:</b> The <b>Ship with Walmart service from China to the
        U.S.</b> is <b>paused until further notice</b>.

        <b style="color: green;">Market availability: Global</b>

        Args:
            accept: Specifies the desired response format. The order of media types determines the priority for format
                selection. **Supported values:** - ``application/json`` : Returns tracking information only (no label
                file). - ``application/json, application/pdf`` : Returns the label in PDF format. - ``application/json,
                image/png`` : Returns the label in PNG format. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL, US <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Internal Server Error ``error`` is ``V3ShippingLabels500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_label(
                accept,
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

    def create_label_mps(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingMultiPackageLabelsResponse:
        """Creates a shipping label for items, supporting multiple packages per request. A successful response includes
        a tracking number and a label file in the media type specified by the Accept header. This API supports <b>all
        shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>•application/json, application/pdf → Returns
        the label in PDF format.<br>•application/json → Returns tracking info only, in JSON format.

        <b style="color: green;">Market availability: CA | MX</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: CA</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request Internal Server Error ``error`` is ``list[Error5] |
                V3ShippingMultiPackageLabels500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.create_label_mps(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def discard_label(
        self,
        carrier_short_name: str,
        tracking_no: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket6OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersTrackingsResponse:
        """Marks a previously generated shipping label as discarded. This API is used when the label should no longer be
        used for shipment processing. <br><br> <b>Applicable Shipping Programs:</b><br>This API is supported for the
        following <b>shipping programs: Walmart Provided Shipping (WPS) and Ship with Walmart (SWW).</b>

        <b style="color: green;">Market availability: US | CA | MX</b>

        Args:
            carrier_short_name: The short name of the shipping carrier.<br>Use the carrierShortName value returned from
                the Supported Carriers API to ensure compatibility. <b style="color: green;">Market availability: US |
                CA | MX</b>
            tracking_no: The shipment tracking number. <b style="color: green;">Market availability: US | CA | MX</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global </b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br> Example: b3261d2d-028a-4ef7-8602-633c23200af6 <br> <b
                style="color: green;">Market availability: Global </b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace. <b
                style="color: green;">Market availability: Global </b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, US <b style="color: green;">Market availability: Global </b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global </b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global </b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request ``error`` is ``list[V3ShippingLabelsCarriersTrackings400Error1] | RawError``."""
        return unwrap(
            self._with_raw_response.discard_label(
                carrier_short_name,
                tracking_no,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_carrier_package_types(
        self,
        carrier_short_name: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersPackageTypesResponse:
        """This API retrieves all supported package types for the selected carrier.

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName fetched from carrier API response or pass 'ALL' to fetch all package
                types of supported carriers <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a random generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_carrier_package_types(
                carrier_short_name,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_carriers(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersResponse:
        """This API retrieves all carriers supported by Ship With Walmart.

        <b style="color: green;">Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <b style="color: green;">Market
                availability:Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_carriers(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_label(
        self,
        purchase_order_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsPurchaseOrdersResponse:
        """This API retrieves all label details generated for a purchase order id.

        <b style="color: green;">Market availability: Global</b>

        Args:
            purchase_order_id: purchaseOrderId <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. <b style="color: green;">Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_label(
                purchase_order_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_label_by_tracking_and_carrier(
        self,
        carrier_short_name: str,
        tracking_no: str,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        r"""Retrieves the shipping label for a specific carrier and tracking number combination. The response includes
        the tracking number and the label in the requested media type (PDF or PNG), based on the Accept header provided.
        <br><br> <b>Media Type Options:</b><br>•Accept: application/json,application/pdf → Returns label in PDF
        format.<br>•Accept: application/json,image/png → Returns label in PNG format. <br><br><b>Market and Shipment
        Program Applicability:</b><br>•<b>CL</b> : Applicable for <b>International</b> shipments only.<br>•<b>US, MX,
        CA</b>: Applicable for <b>Domestic and International</b> shipments across <b>all shipping programs</b>
        (including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>).

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName <b style="color: green;">Market availability: Global</b>
            tracking_no: trackingNo <b style="color: green;">Market availability: Global</b>
            accept: Supported media types for US, CA, MX are:\napplication/pdf, image/png. For CL, the supported media
                type is\napplication/pdf, image/png, application/zpl.\n\n<b style=\"color: green;\">Market availability:
                Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_label_by_tracking_and_carrier(
                carrier_short_name,
                tracking_no,
                accept,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_scan_form_by_manifest_id(
        self,
        manifest_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponse:
        """This API retrieves a scan form for a given manifest ID.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox returns a stub binary document for
        any valid sandbox ``manifestId``. The ``documentFormat`` selection (PDF/ZPL/PNG) is honored in production; in
        sandbox, a PDF stub is always returned regardless of the format requested during scan form creation.

        **Note:** This endpoint returns a binary document stream (application/octet-stream). Treat the response body as
        bytes and save it to a file. The underlying document format aligns with the scan form documentFormat selected
        during creation (for example, PDF, ZPL, PNG).

        Args:
            manifest_id: Manifest ID returned by the create scan form API. Use this value to download the scan form
                document.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Requested response media type. This endpoint returns a binary document stream
                (application/octet-stream). Treat the response body as bytes. <b style="color: green;">Market
                availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_scan_form_by_manifest_id(
                manifest_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_shipping_estimate(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsShippingEstimatesResponse:
        """This API retrieves shipping cost estimates for available shipping services based on address and package
        (example, customer address, packaged weight.)

        <b style="color: green;">Market availability: US only</b>

        Args:
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br>Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Shipping fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request ``error`` is ``list[V3ShippingLabelsShippingEstimates400Error1] | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipping_estimate(
                accept,
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

    def scan_form(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingScanFormResponse:
        """This API generates a scan form using the provided tracking numbers. The scan form is a consolidated document
        that contains all the tracking numbers and shipping details for the packages being shipped out on a particular
        day. It is used by carriers to verify and process the shipments during pickup and delivery. Currently, only USPS
        supports scan forms.

        **Idempotency:** ``scanFormId`` acts as a natural idempotency key — the client supplies it in the request body
        before the call. Submitting a second POST with a ``scanFormId`` that was already successfully processed returns
        ``409 Conflict``; no duplicate scan form is created. On network failure or timeout, clients may safely retry
        using the same ``scanFormId``. This guarantee is critical for EOD automation — a duplicate manifest can cause
        carrier processing errors and shipment delays.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox accepts test tracking numbers and
        returns a synthetic ``manifestId`` (e.g. ``SANDBOX-12345``). Use that ``manifestId`` with the GET endpoint to
        retrieve the stub scan form document.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response media type. Only supported media type: application/json. <b style="color: green;">Market
                availability: Global</b>
            body: Scan form request payload, including carrier, ship date, origin address, and tracking numbers to
                include in the manifest.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid operation Conflict — a scan form with the given scanFormId already exists. No duplicate is
                created. Retrieve the existing scan form using the GET endpoint with the previously returned manifestId.
                ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.scan_form(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ShipWithWalmartWithRawResponse:
        return self._with_raw_response


class AsyncShipWithWalmart:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShipWithWalmartWithRawResponse(client, server, auth)

    async def create_label(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsResponse:
        """Generates a shipping label using the provided shipment information. A successful response includes a tracking
        number and a label file in the media type specified in the Accept header.<br><br>This API is supported for
        <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>• application/json, application/pdf →
        Returns label in PDF format. • application/json, image/png → Returns label in PNG format. • application/json →
        Returns tracking info only in JSON. <br><br> <b>Note:</b> The <b>Ship with Walmart service from China to the
        U.S.</b> is <b>paused until further notice</b>.

        <b style="color: green;">Market availability: Global</b>

        Args:
            accept: Specifies the desired response format. The order of media types determines the priority for format
                selection. **Supported values:** - ``application/json`` : Returns tracking information only (no label
                file). - ``application/json, application/pdf`` : Returns the label in PDF format. - ``application/json,
                image/png`` : Returns the label in PNG format. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL, US <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Internal Server Error ``error`` is ``V3ShippingLabels500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_label(
                accept,
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

    async def create_label_mps(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingMultiPackageLabelsResponse:
        """Creates a shipping label for items, supporting multiple packages per request. A successful response includes
        a tracking number and a label file in the media type specified by the Accept header. This API supports <b>all
        shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>•application/json, application/pdf → Returns
        the label in PDF format.<br>•application/json → Returns tracking info only, in JSON format.

        <b style="color: green;">Market availability: CA | MX</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: CA</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request Internal Server Error ``error`` is ``list[Error5] |
                V3ShippingMultiPackageLabels500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.create_label_mps(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def discard_label(
        self,
        carrier_short_name: str,
        tracking_no: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket6OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersTrackingsResponse:
        """Marks a previously generated shipping label as discarded. This API is used when the label should no longer be
        used for shipment processing. <br><br> <b>Applicable Shipping Programs:</b><br>This API is supported for the
        following <b>shipping programs: Walmart Provided Shipping (WPS) and Ship with Walmart (SWW).</b>

        <b style="color: green;">Market availability: US | CA | MX</b>

        Args:
            carrier_short_name: The short name of the shipping carrier.<br>Use the carrierShortName value returned from
                the Supported Carriers API to ensure compatibility. <b style="color: green;">Market availability: US |
                CA | MX</b>
            tracking_no: The shipment tracking number. <b style="color: green;">Market availability: US | CA | MX</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global </b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br> Example: b3261d2d-028a-4ef7-8602-633c23200af6 <br> <b
                style="color: green;">Market availability: Global </b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace. <b
                style="color: green;">Market availability: Global </b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, US <b style="color: green;">Market availability: Global </b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global </b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global </b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request ``error`` is ``list[V3ShippingLabelsCarriersTrackings400Error1] | RawError``."""
        return unwrap(
            await self._with_raw_response.discard_label(
                carrier_short_name,
                tracking_no,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_carrier_package_types(
        self,
        carrier_short_name: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersPackageTypesResponse:
        """This API retrieves all supported package types for the selected carrier.

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName fetched from carrier API response or pass 'ALL' to fetch all package
                types of supported carriers <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a random generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_carrier_package_types(
                carrier_short_name,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_carriers(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsCarriersResponse:
        """This API retrieves all carriers supported by Ship With Walmart.

        <b style="color: green;">Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <b style="color: green;">Market
                availability:Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_carriers(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_label(
        self,
        purchase_order_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsPurchaseOrdersResponse:
        """This API retrieves all label details generated for a purchase order id.

        <b style="color: green;">Market availability: Global</b>

        Args:
            purchase_order_id: purchaseOrderId <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. <b style="color: green;">Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_label(
                purchase_order_id,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_label_by_tracking_and_carrier(
        self,
        carrier_short_name: str,
        tracking_no: str,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        r"""Retrieves the shipping label for a specific carrier and tracking number combination. The response includes
        the tracking number and the label in the requested media type (PDF or PNG), based on the Accept header provided.
        <br><br> <b>Media Type Options:</b><br>•Accept: application/json,application/pdf → Returns label in PDF
        format.<br>•Accept: application/json,image/png → Returns label in PNG format. <br><br><b>Market and Shipment
        Program Applicability:</b><br>•<b>CL</b> : Applicable for <b>International</b> shipments only.<br>•<b>US, MX,
        CA</b>: Applicable for <b>Domestic and International</b> shipments across <b>all shipping programs</b>
        (including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>).

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName <b style="color: green;">Market availability: Global</b>
            tracking_no: trackingNo <b style="color: green;">Market availability: Global</b>
            accept: Supported media types for US, CA, MX are:\napplication/pdf, image/png. For CL, the supported media
                type is\napplication/pdf, image/png, application/zpl.\n\n<b style=\"color: green;\">Market availability:
                Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_label_by_tracking_and_carrier(
                carrier_short_name,
                tracking_no,
                accept,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_scan_form_by_manifest_id(
        self,
        manifest_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsyncFileResponse:
        """This API retrieves a scan form for a given manifest ID.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox returns a stub binary document for
        any valid sandbox ``manifestId``. The ``documentFormat`` selection (PDF/ZPL/PNG) is honored in production; in
        sandbox, a PDF stub is always returned regardless of the format requested during scan form creation.

        **Note:** This endpoint returns a binary document stream (application/octet-stream). Treat the response body as
        bytes and save it to a file. The underlying document format aligns with the scan form documentFormat selected
        during creation (for example, PDF, ZPL, PNG).

        Args:
            manifest_id: Manifest ID returned by the create scan form API. Use this value to download the scan form
                document.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Requested response media type. This endpoint returns a binary document stream
                (application/octet-stream). Treat the response body as bytes. <b style="color: green;">Market
                availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_scan_form_by_manifest_id(
                manifest_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_shipping_estimate(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingLabelsShippingEstimatesResponse:
        """This API retrieves shipping cost estimates for available shipping services based on address and package
        (example, customer address, packaged weight.)

        <b style="color: green;">Market availability: US only</b>

        Args:
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br>Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Shipping fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad request ``error`` is ``list[V3ShippingLabelsShippingEstimates400Error1] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipping_estimate(
                accept,
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

    async def scan_form(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ShippingScanFormResponse:
        """This API generates a scan form using the provided tracking numbers. The scan form is a consolidated document
        that contains all the tracking numbers and shipping details for the packages being shipped out on a particular
        day. It is used by carriers to verify and process the shipments during pickup and delivery. Currently, only USPS
        supports scan forms.

        **Idempotency:** ``scanFormId`` acts as a natural idempotency key — the client supplies it in the request body
        before the call. Submitting a second POST with a ``scanFormId`` that was already successfully processed returns
        ``409 Conflict``; no duplicate scan form is created. On network failure or timeout, clients may safely retry
        using the same ``scanFormId``. This guarantee is critical for EOD automation — a duplicate manifest can cause
        carrier processing errors and shipment delays.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox accepts test tracking numbers and
        returns a synthetic ``manifestId`` (e.g. ``SANDBOX-12345``). Use that ``manifestId`` with the GET endpoint to
        retrieve the stub scan form document.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response media type. Only supported media type: application/json. <b style="color: green;">Market
                availability: Global</b>
            body: Scan form request payload, including carrier, ship date, origin address, and tracking numbers to
                include in the manifest.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Invalid operation Conflict — a scan form with the given scanFormId already exists. No duplicate is
                created. Retrieve the existing scan form using the GET endpoint with the previously returned manifestId.
                ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.scan_form(
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                accept,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncShipWithWalmartWithRawResponse:
        return self._with_raw_response


class ShipWithWalmartWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_label(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsResponse, CreateLabelErrorBody]:
        """Generates a shipping label using the provided shipment information. A successful response includes a tracking
        number and a label file in the media type specified in the Accept header.<br><br>This API is supported for
        <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>• application/json, application/pdf →
        Returns label in PDF format. • application/json, image/png → Returns label in PNG format. • application/json →
        Returns tracking info only in JSON. <br><br> <b>Note:</b> The <b>Ship with Walmart service from China to the
        U.S.</b> is <b>paused until further notice</b>.

        <b style="color: green;">Market availability: Global</b>

        Args:
            accept: Specifies the desired response format. The order of media types determines the priority for format
                selection. **Supported values:** - ``application/json`` : Returns tracking information only (no label
                file). - ``application/json, application/pdf`` : Returns the label in PDF format. - ``application/json,
                image/png`` : Returns the label in PNG format. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL, US <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/labels"),
            headers=[
                param[str]("Accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingLabelsRequest | V3ShippingLabelsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsResponse],
            error_mapper=create_label_error_mapper,
            request_options=request_options,
        )

    def create_label_mps(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingMultiPackageLabelsResponse, CreateLabelMpsErrorBody]:
        """Creates a shipping label for items, supporting multiple packages per request. A successful response includes
        a tracking number and a label file in the media type specified by the Accept header. This API supports <b>all
        shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>•application/json, application/pdf → Returns
        the label in PDF format.<br>•application/json → Returns tracking info only, in JSON format.

        <b style="color: green;">Market availability: CA | MX</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: CA</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/multi-package/labels"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingMultiPackageLabelsResponse],
            error_mapper=create_label_mps_error_mapper,
            request_options=request_options,
        )

    def discard_label(
        self,
        carrier_short_name: str,
        tracking_no: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket6OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersTrackingsResponse, DiscardLabelErrorBody]:
        """Marks a previously generated shipping label as discarded. This API is used when the label should no longer be
        used for shipment processing. <br><br> <b>Applicable Shipping Programs:</b><br>This API is supported for the
        following <b>shipping programs: Walmart Provided Shipping (WPS) and Ship with Walmart (SWW).</b>

        <b style="color: green;">Market availability: US | CA | MX</b>

        Args:
            carrier_short_name: The short name of the shipping carrier.<br>Use the carrierShortName value returned from
                the Supported Carriers API to ensure compatibility. <b style="color: green;">Market availability: US |
                CA | MX</b>
            tracking_no: The shipment tracking number. <b style="color: green;">Market availability: US | CA | MX</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global </b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br> Example: b3261d2d-028a-4ef7-8602-633c23200af6 <br> <b
                style="color: green;">Market availability: Global </b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace. <b
                style="color: green;">Market availability: Global </b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, US <b style="color: green;">Market availability: Global </b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global </b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global </b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}"),
            path_params=[param[str]("carrierShortName", carrier_short_name), param[str]("trackingNo", tracking_no)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket6OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsCarriersTrackingsResponse],
            error_mapper=discard_label_error_mapper,
            request_options=request_options,
        )

    def get_carrier_package_types(
        self,
        carrier_short_name: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersPackageTypesResponse, RawError]:
        """This API retrieves all supported package types for the selected carrier.

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName fetched from carrier API response or pass 'ALL' to fetch all package
                types of supported carriers <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a random generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/package-types"),
            path_params=[param[str]("carrierShortName", carrier_short_name)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsCarriersPackageTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_carriers(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersResponse, RawError]:
        """This API retrieves all carriers supported by Ship With Walmart.

        <b style="color: green;">Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <b style="color: green;">Market
                availability:Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsCarriersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_label(
        self,
        purchase_order_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsPurchaseOrdersResponse, RawError]:
        """This API retrieves all label details generated for a purchase order id.

        <b style="color: green;">Market availability: Global</b>

        Args:
            purchase_order_id: purchaseOrderId <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. <b style="color: green;">Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/purchase-orders/{purchaseOrderId}"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsPurchaseOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_label_by_tracking_and_carrier(
        self,
        carrier_short_name: str,
        tracking_no: str,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        r"""Retrieves the shipping label for a specific carrier and tracking number combination. The response includes
        the tracking number and the label in the requested media type (PDF or PNG), based on the Accept header provided.
        <br><br> <b>Media Type Options:</b><br>•Accept: application/json,application/pdf → Returns label in PDF
        format.<br>•Accept: application/json,image/png → Returns label in PNG format. <br><br><b>Market and Shipment
        Program Applicability:</b><br>•<b>CL</b> : Applicable for <b>International</b> shipments only.<br>•<b>US, MX,
        CA</b>: Applicable for <b>Domestic and International</b> shipments across <b>all shipping programs</b>
        (including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>).

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName <b style="color: green;">Market availability: Global</b>
            tracking_no: trackingNo <b style="color: green;">Market availability: Global</b>
            accept: Supported media types for US, CA, MX are:\napplication/pdf, image/png. For CL, the supported media
                type is\napplication/pdf, image/png, application/zpl.\n\n<b style=\"color: green;\">Market availability:
                Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}"),
            path_params=[param[str]("carrierShortName", carrier_short_name), param[str]("trackingNo", tracking_no)],
            headers=[
                param[str]("accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_scan_form_by_manifest_id(
        self,
        manifest_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponse, RawError]:
        """This API retrieves a scan form for a given manifest ID.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox returns a stub binary document for
        any valid sandbox ``manifestId``. The ``documentFormat`` selection (PDF/ZPL/PNG) is honored in production; in
        sandbox, a PDF stub is always returned regardless of the format requested during scan form creation.

        **Note:** This endpoint returns a binary document stream (application/octet-stream). Treat the response body as
        bytes and save it to a file. The underlying document format aligns with the scan form documentFormat selected
        during creation (for example, PDF, ZPL, PNG).

        Args:
            manifest_id: Manifest ID returned by the create scan form API. Use this value to download the scan form
                document.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Requested response media type. This endpoint returns a binary document stream
                (application/octet-stream). Treat the response body as bytes. <b style="color: green;">Market
                availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/scan-form"),
            query_params=[param[str]("manifestId", manifest_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=file_decoder,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_shipping_estimate(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsShippingEstimatesResponse, GetShippingEstimateErrorBody]:
        """This API retrieves shipping cost estimates for available shipping services based on address and package
        (example, customer address, packaged weight.)

        <b style="color: green;">Market availability: US only</b>

        Args:
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br>Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Shipping fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/labels/shipping-estimates"),
            headers=[
                param[str]("Accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingLabelsShippingEstimatesResponse],
            error_mapper=get_shipping_estimate_error_mapper,
            request_options=request_options,
        )

    def scan_form(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingScanFormResponse, ScanFormErrorBody]:
        """This API generates a scan form using the provided tracking numbers. The scan form is a consolidated document
        that contains all the tracking numbers and shipping details for the packages being shipped out on a particular
        day. It is used by carriers to verify and process the shipments during pickup and delivery. Currently, only USPS
        supports scan forms.

        **Idempotency:** ``scanFormId`` acts as a natural idempotency key — the client supplies it in the request body
        before the call. Submitting a second POST with a ``scanFormId`` that was already successfully processed returns
        ``409 Conflict``; no duplicate scan form is created. On network failure or timeout, clients may safely retry
        using the same ``scanFormId``. This guarantee is critical for EOD automation — a duplicate manifest can cause
        carrier processing errors and shipment delays.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox accepts test tracking numbers and
        returns a synthetic ``manifestId`` (e.g. ``SANDBOX-12345``). Use that ``manifestId`` with the GET endpoint to
        retrieve the stub scan form document.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response media type. Only supported media type: application/json. <b style="color: green;">Market
                availability: Global</b>
            body: Scan form request payload, including carrier, ship date, origin address, and tracking numbers to
                include in the manifest.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/scan-form"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingScanFormRequest | V3ShippingScanFormRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3ShippingScanFormResponse],
            error_mapper=scan_form_error_mapper,
            request_options=request_options,
        )


class AsyncShipWithWalmartWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_label(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsResponse, CreateLabelErrorBody]:
        """Generates a shipping label using the provided shipment information. A successful response includes a tracking
        number and a label file in the media type specified in the Accept header.<br><br>This API is supported for
        <b>all shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>• application/json, application/pdf →
        Returns label in PDF format. • application/json, image/png → Returns label in PNG format. • application/json →
        Returns tracking info only in JSON. <br><br> <b>Note:</b> The <b>Ship with Walmart service from China to the
        U.S.</b> is <b>paused until further notice</b>.

        <b style="color: green;">Market availability: Global</b>

        Args:
            accept: Specifies the desired response format. The order of media types determines the priority for format
                selection. **Supported values:** - ``application/json`` : Returns tracking information only (no label
                file). - ``application/json, application/pdf`` : Returns the label in PDF format. - ``application/json,
                image/png`` : Returns the label in PNG format. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br>Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL, US <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/labels"),
            headers=[
                param[str]("Accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingLabelsRequest | V3ShippingLabelsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsResponse],
            error_mapper=create_label_error_mapper,
            request_options=request_options,
        )

    async def create_label_mps(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingMultiPackageLabelsResponse, CreateLabelMpsErrorBody]:
        """Creates a shipping label for items, supporting multiple packages per request. A successful response includes
        a tracking number and a label file in the media type specified by the Accept header. This API supports <b>all
        shipping programs</b>, including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart
        (SWW)</b>.<br><br><b>Media Type Options (via Accept header):</b><br>•application/json, application/pdf → Returns
        the label in PDF format.<br>•application/json → Returns tracking info only, in JSON format.

        <b style="color: green;">Market availability: CA | MX</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: CA</b>
            body: Label fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/multi-package/labels"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingMultiPackageLabelsResponse],
            error_mapper=create_label_mps_error_mapper,
            request_options=request_options,
        )

    async def discard_label(
        self,
        carrier_short_name: str,
        tracking_no: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket6OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersTrackingsResponse, DiscardLabelErrorBody]:
        """Marks a previously generated shipping label as discarded. This API is used when the label should no longer be
        used for shipment processing. <br><br> <b>Applicable Shipping Programs:</b><br>This API is supported for the
        following <b>shipping programs: Walmart Provided Shipping (WPS) and Ship with Walmart (SWW).</b>

        <b style="color: green;">Market availability: US | CA | MX</b>

        Args:
            carrier_short_name: The short name of the shipping carrier.<br>Use the carrierShortName value returned from
                the Supported Carriers API to ensure compatibility. <b style="color: green;">Market availability: US |
                CA | MX</b>
            tracking_no: The shipment tracking number. <b style="color: green;">Market availability: US | CA | MX</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <b style="color: green;">Market availability: Global </b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <br> Example: b3261d2d-028a-4ef7-8602-633c23200af6 <br> <b
                style="color: green;">Market availability: Global </b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace. <b
                style="color: green;">Market availability: Global </b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, US <b style="color: green;">Market availability: Global </b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global </b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global </b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}"),
            path_params=[param[str]("carrierShortName", carrier_short_name), param[str]("trackingNo", tracking_no)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket6OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsCarriersTrackingsResponse],
            error_mapper=discard_label_error_mapper,
            request_options=request_options,
        )

    async def get_carrier_package_types(
        self,
        carrier_short_name: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersPackageTypesResponse, RawError]:
        """This API retrieves all supported package types for the selected carrier.

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName fetched from carrier API response or pass 'ALL' to fetch all package
                types of supported carriers <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a random generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. Valid values: MX, CA, CL. <b style="color: green;">Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/package-types"),
            path_params=[param[str]("carrierShortName", carrier_short_name)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsCarriersPackageTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_carriers(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsCarriersResponse, RawError]:
        """This API retrieves all carriers supported by Ship With Walmart.

        <b style="color: green;">Market availability: Global</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call <b style="color: green;">Market
                availability:Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsCarriersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_label(
        self,
        purchase_order_id: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsPurchaseOrdersResponse, RawError]:
        """This API retrieves all label details generated for a purchase order id.

        <b style="color: green;">Market availability: Global</b>

        Args:
            purchase_order_id: purchaseOrderId <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs. <br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. <b style="color: green;">Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/purchase-orders/{purchaseOrderId}"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsPurchaseOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_label_by_tracking_and_carrier(
        self,
        carrier_short_name: str,
        tracking_no: str,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        r"""Retrieves the shipping label for a specific carrier and tracking number combination. The response includes
        the tracking number and the label in the requested media type (PDF or PNG), based on the Accept header provided.
        <br><br> <b>Media Type Options:</b><br>•Accept: application/json,application/pdf → Returns label in PDF
        format.<br>•Accept: application/json,image/png → Returns label in PNG format. <br><br><b>Market and Shipment
        Program Applicability:</b><br>•<b>CL</b> : Applicable for <b>International</b> shipments only.<br>•<b>US, MX,
        CA</b>: Applicable for <b>Domestic and International</b> shipments across <b>all shipping programs</b>
        (including <b>Walmart Provided Shipping (WPS)</b> and <b>Ship with Walmart (SWW)</b>).

        <b style="color: green;">Market availability: Global</b>

        Args:
            carrier_short_name: carrierShortName <b style="color: green;">Market availability: Global</b>
            tracking_no: trackingNo <b style="color: green;">Market availability: Global</b>
            accept: Supported media types for US, CA, MX are:\napplication/pdf, image/png. For CL, the supported media
                type is\napplication/pdf, image/png, application/zpl.\n\n<b style=\"color: green;\">Market availability:
                Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br> Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Walmart Service Name <b style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}"),
            path_params=[param[str]("carrierShortName", carrier_short_name), param[str]("trackingNo", tracking_no)],
            headers=[
                param[str]("accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_scan_form_by_manifest_id(
        self,
        manifest_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsyncFileResponse, RawError]:
        """This API retrieves a scan form for a given manifest ID.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox returns a stub binary document for
        any valid sandbox ``manifestId``. The ``documentFormat`` selection (PDF/ZPL/PNG) is honored in production; in
        sandbox, a PDF stub is always returned regardless of the format requested during scan form creation.

        **Note:** This endpoint returns a binary document stream (application/octet-stream). Treat the response body as
        bytes and save it to a file. The underlying document format aligns with the scan form documentFormat selected
        during creation (for example, PDF, ZPL, PNG).

        Args:
            manifest_id: Manifest ID returned by the create scan form API. Use this value to download the scan form
                document.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Requested response media type. This endpoint returns a binary document stream
                (application/octet-stream). Treat the response body as bytes. <b style="color: green;">Market
                availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/shipping/scan-form"),
            query_params=[param[str]("manifestId", manifest_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_file_decoder,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_shipping_estimate(
        self,
        accept: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket11OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingLabelsShippingEstimatesResponse, GetShippingEstimateErrorBody]:
        """This API retrieves shipping cost estimates for available shipping services based on address and package
        (example, customer address, packaged weight.)

        <b style="color: green;">Market availability: US only</b>

        Args:
            accept: Response type. The order of media types in the Accept header determines the priority for response
                format selection. <b style="color: green;">Market availability: Global</b>
            wm_sec_access_token: Access token obtained from the Token API. This is required for authenticating requests
                to Walmart Marketplace APIs.<br>Example:
                eyJraWQiOiIxNWNhNGIyYi0yODVjLTQ0ZDUtYmExNC05ZDk1NTlkZmUwNjgiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0....
                <b style="color: green;">Market availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <br> Example: Walmart Marketplace <b
                style="color: green;">Market availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: MX, CA, CL <b style="color: green;">Market
                availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            body: Shipping fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/labels/shipping-estimates"),
            headers=[
                param[str]("Accept", accept),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket11OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict](
                body
            ),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingLabelsShippingEstimatesResponse],
            error_mapper=get_shipping_estimate_error_mapper,
            request_options=request_options,
        )

    async def scan_form(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarketOrStr,
        wm_global_version: WmGlobalVersionOrStr,
        accept: str,
        body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ShippingScanFormResponse, ScanFormErrorBody]:
        """This API generates a scan form using the provided tracking numbers. The scan form is a consolidated document
        that contains all the tracking numbers and shipping details for the packages being shipped out on a particular
        day. It is used by carriers to verify and process the shipments during pickup and delivery. Currently, only USPS
        supports scan forms.

        **Idempotency:** ``scanFormId`` acts as a natural idempotency key — the client supplies it in the request body
        before the call. Submitting a second POST with a ``scanFormId`` that was already successfully processed returns
        ``409 Conflict``; no duplicate scan form is created. On network failure or timeout, clients may safely retry
        using the same ``scanFormId``. This guarantee is critical for EOD automation — a duplicate manifest can cause
        carrier processing errors and shipment delays.

        **Rate Limits:** This endpoint allows 100 requests per minute. Exceeding this limit returns a ``429 Too Many
        Requests`` response. See the `Rate Limiting guide
        <https://developer.walmart.com/us-marketplace/docs/rate-limiting>`__ for full details. The response includes
        ``x-current-token-count`` (remaining requests in the current window) and ``X-Next-Replenishment-Time`` (when the
        token count next increases).

        **Sandbox:** Use base URL ``https://sandbox.walmartapis.com``. The sandbox accepts test tracking numbers and
        returns a synthetic ``manifestId`` (e.g. ``SANDBOX-12345``). Use that ``manifestId`` with the GET endpoint to
        retrieve the stub scan form document.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            wm_market: Case-sensitive market identifier. Valid values: US <b style="color: green;">Market availability:
                Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1. <b style="color:
                green;">Market availability: Global</b>
            accept: Response media type. Only supported media type: application/json. <b style="color: green;">Market
                availability: Global</b>
            body: Scan form request payload, including carrier, ship date, origin address, and tracking numbers to
                include in the manifest.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/shipping/scan-form"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3ShippingScanFormRequest | V3ShippingScanFormRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3ShippingScanFormResponse],
            error_mapper=scan_form_error_mapper,
            request_options=request_options,
        )

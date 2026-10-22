from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncFileResponse,
    AsyncRawClient,
    BaseRawResponse,
    FileInput,
    FileResponse,
    RawClient,
    RequestOptionsOrDict,
    async_file_decoder,
    async_json_decoder,
    file_decoder,
    file_part,
    json_body,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.download_claim_documents_error import (
    DownloadClaimDocumentsErrorBody,
    download_claim_documents_error_mapper,
)
from ..errors.get_claim_details_error import GetClaimDetailsErrorBody, get_claim_details_error_mapper
from ..errors.get_claim_history_error import GetClaimHistoryErrorBody, get_claim_history_error_mapper
from ..errors.list_claims_error import ListClaimsErrorBody, list_claims_error_mapper
from ..errors.submit_additional_info_error import SubmitAdditionalInfoErrorBody, submit_additional_info_error_mapper
from ..errors.submit_claim_error import SubmitClaimErrorBody, submit_claim_error_mapper
from ..models.document_type import DocumentType, DocumentTypeDict
from ..models.document_type1 import DocumentType1, DocumentType1Dict
from ..models.enums.claims_group import ClaimsGroupOrStr
from ..models.enums.order import OrderOrStr
from ..models.enums.sort_by import SortByOrStr
from ..models.payload import Payload, PayloadDict
from ..models.v3_claims_shipment_protection_claim_documents_request import (
    V3ClaimsShipmentProtectionClaimDocumentsRequest,
    V3ClaimsShipmentProtectionClaimDocumentsRequestDict,
)
from ..models.v3_claims_shipment_protection_claim_history_response import V3ClaimsShipmentProtectionClaimHistoryResponse
from ..server.server import Server


class ShipmentProtection:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = ShipmentProtectionWithRawResponse(client, server)

    def download_claim_documents(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileResponse:
        """Returns a ZIP file containing one or more uploaded claim documents.<br><b style='color:green;'>Market
        availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            body: The request body.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file of documents

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaimDocuments400Error1 | V3ClaimsShipmentProtectionClaimDocuments404Error1
                | V3ClaimsShipmentProtectionClaimDocuments500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.download_claim_documents(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_claim_details(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Retrieves detailed information for a single claim.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Details retrieved successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim404Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_claim_details(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_claim_history(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ClaimsShipmentProtectionClaimHistoryResponse:
        """Returns a chronological log of status changes, notes, and uploaded documents.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            History retrieved successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaimHistory400Error1 | V3ClaimsShipmentProtectionClaimHistory404Error1 |
                V3ClaimsShipmentProtectionClaimHistory500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_claim_history(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def list_claims(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        claims_group: ClaimsGroupOrStr | None = None,
        claim_number: str | None = None,
        purchase_order_id: str | None = None,
        tracking_no: str | None = None,
        claim_types: str | None = None,
        claim_statuses: str | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: OrderOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns a paginated list of claims, with optional filters.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            limit: Maximum number of results to return in the response page (default 25, maximum 300).
            offset: Zero‑based index of the first result to return (default 0). Use together with ``limit`` for
                pagination.
            claims_group: Filter claims by broad status group: OPEN, ACTION_NEEDED, or CLOSED.
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            purchase_order_id: Filter by the Walmart purchase order ID associated with the claim.
            tracking_no: Filter by the package tracking number associated with the claim.
            claim_types: Comma‑separated list of claim types to include (LIT, LAD, DAMAGED).
            claim_statuses: Comma‑separated list of claim status codes to include (INITIATED, IN_REVIEW, NEED_INFO,
                etc.).
            sort_by: Field to sort by; currently supports ``claimDate``.
            sort_order: Sort direction: ``ASC`` for ascending or ``DESC`` for descending (default DESC).
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Claims retrieved successfully.

        Raises:
            ApiError: Bad request Unauthorized Internal server error ``error`` is ``V3ClaimsShipmentProtection400Error1
                | V3ClaimsShipmentProtection401Error1 | V3ClaimsShipmentProtection500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.list_claims(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                limit=limit,
                offset=offset,
                claims_group=claims_group,
                claim_number=claim_number,
                purchase_order_id=purchase_order_id,
                tracking_no=tracking_no,
                claim_types=claim_types,
                claim_statuses=claim_statuses,
                sort_by=sort_by,
                sort_order=sort_order,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def submit_additional_info(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: FileInput,
        document_types: list[DocumentType1 | DocumentType1Dict],
        *,
        wm_consumer_channel_type: str | None = None,
        notes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Adds documents or notes to an existing claim when Walmart requests more details.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Additional supporting file.
            document_types: Mapping for each uploaded file.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            notes: Additional information requested by Walmart
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Additional information submitted successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim404Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.submit_additional_info(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                files,
                document_types,
                wm_consumer_channel_type=wm_consumer_channel_type,
                notes=notes,
                request_options=request_options,
            ),
        )

    def submit_claim(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: FileInput,
        document_types: list[DocumentType | DocumentTypeDict],
        payload: Payload | PayloadDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Creates a shipment-protection claim. Send multipart/form-data with files, documentTypes, and payload.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Supporting file (image, PDF, etc.).
            document_types: Maps each uploaded file to its document category.
            payload: Claim details.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Claim submitted successfully

        Raises:
            ApiError: Bad request Unauthorized Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim401Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.submit_claim(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                files,
                document_types,
                payload,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ShipmentProtectionWithRawResponse:
        return self._with_raw_response


class AsyncShipmentProtection:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncShipmentProtectionWithRawResponse(client, server)

    async def download_claim_documents(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AsyncFileResponse:
        """Returns a ZIP file containing one or more uploaded claim documents.<br><b style='color:green;'>Market
        availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            body: The request body.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file of documents

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaimDocuments400Error1 | V3ClaimsShipmentProtectionClaimDocuments404Error1
                | V3ClaimsShipmentProtectionClaimDocuments500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.download_claim_documents(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_claim_details(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Retrieves detailed information for a single claim.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Details retrieved successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim404Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_claim_details(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_claim_history(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3ClaimsShipmentProtectionClaimHistoryResponse:
        """Returns a chronological log of status changes, notes, and uploaded documents.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            History retrieved successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaimHistory400Error1 | V3ClaimsShipmentProtectionClaimHistory404Error1 |
                V3ClaimsShipmentProtectionClaimHistory500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_claim_history(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def list_claims(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        claims_group: ClaimsGroupOrStr | None = None,
        claim_number: str | None = None,
        purchase_order_id: str | None = None,
        tracking_no: str | None = None,
        claim_types: str | None = None,
        claim_statuses: str | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: OrderOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns a paginated list of claims, with optional filters.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            limit: Maximum number of results to return in the response page (default 25, maximum 300).
            offset: Zero‑based index of the first result to return (default 0). Use together with ``limit`` for
                pagination.
            claims_group: Filter claims by broad status group: OPEN, ACTION_NEEDED, or CLOSED.
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            purchase_order_id: Filter by the Walmart purchase order ID associated with the claim.
            tracking_no: Filter by the package tracking number associated with the claim.
            claim_types: Comma‑separated list of claim types to include (LIT, LAD, DAMAGED).
            claim_statuses: Comma‑separated list of claim status codes to include (INITIATED, IN_REVIEW, NEED_INFO,
                etc.).
            sort_by: Field to sort by; currently supports ``claimDate``.
            sort_order: Sort direction: ``ASC`` for ascending or ``DESC`` for descending (default DESC).
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Claims retrieved successfully.

        Raises:
            ApiError: Bad request Unauthorized Internal server error ``error`` is ``V3ClaimsShipmentProtection400Error1
                | V3ClaimsShipmentProtection401Error1 | V3ClaimsShipmentProtection500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.list_claims(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                limit=limit,
                offset=offset,
                claims_group=claims_group,
                claim_number=claim_number,
                purchase_order_id=purchase_order_id,
                tracking_no=tracking_no,
                claim_types=claim_types,
                claim_statuses=claim_statuses,
                sort_by=sort_by,
                sort_order=sort_order,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def submit_additional_info(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: AsyncFileInput,
        document_types: list[DocumentType1 | DocumentType1Dict],
        *,
        wm_consumer_channel_type: str | None = None,
        notes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Adds documents or notes to an existing claim when Walmart requests more details.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Additional supporting file.
            document_types: Mapping for each uploaded file.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            notes: Additional information requested by Walmart
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Additional information submitted successfully.

        Raises:
            ApiError: Bad request Not found Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim404Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.submit_additional_info(
                claim_number,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                files,
                document_types,
                wm_consumer_channel_type=wm_consumer_channel_type,
                notes=notes,
                request_options=request_options,
            ),
        )

    async def submit_claim(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: AsyncFileInput,
        document_types: list[DocumentType | DocumentTypeDict],
        payload: Payload | PayloadDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Creates a shipment-protection claim. Send multipart/form-data with files, documentTypes, and payload.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Supporting file (image, PDF, etc.).
            document_types: Maps each uploaded file to its document category.
            payload: Claim details.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Claim submitted successfully

        Raises:
            ApiError: Bad request Unauthorized Internal server error ``error`` is
                ``V3ClaimsShipmentProtectionClaim400Error1 | V3ClaimsShipmentProtectionClaim401Error1 |
                V3ClaimsShipmentProtectionClaim500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.submit_claim(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                files,
                document_types,
                payload,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncShipmentProtectionWithRawResponse:
        return self._with_raw_response


class ShipmentProtectionWithRawResponse(BaseRawResponse[RawClient, Server]):
    def download_claim_documents(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileResponse, DownloadClaimDocumentsErrorBody]:
        """Returns a ZIP file containing one or more uploaded claim documents.<br><b style='color:green;'>Market
        availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            body: The request body.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}/documents"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict
            ](body),
            decoder=file_decoder,
            error_mapper=download_claim_documents_error_mapper,
            request_options=request_options,
        )

    def get_claim_details(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetClaimDetailsErrorBody]:
        """Retrieves detailed information for a single claim.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[Any],
            error_mapper=get_claim_details_error_mapper,
            request_options=request_options,
        )

    def get_claim_history(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ClaimsShipmentProtectionClaimHistoryResponse, GetClaimHistoryErrorBody]:
        """Returns a chronological log of status changes, notes, and uploaded documents.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}/history"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[V3ClaimsShipmentProtectionClaimHistoryResponse],
            error_mapper=get_claim_history_error_mapper,
            request_options=request_options,
        )

    def list_claims(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        claims_group: ClaimsGroupOrStr | None = None,
        claim_number: str | None = None,
        purchase_order_id: str | None = None,
        tracking_no: str | None = None,
        claim_types: str | None = None,
        claim_statuses: str | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: OrderOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListClaimsErrorBody]:
        """Returns a paginated list of claims, with optional filters.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            limit: Maximum number of results to return in the response page (default 25, maximum 300).
            offset: Zero‑based index of the first result to return (default 0). Use together with ``limit`` for
                pagination.
            claims_group: Filter claims by broad status group: OPEN, ACTION_NEEDED, or CLOSED.
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            purchase_order_id: Filter by the Walmart purchase order ID associated with the claim.
            tracking_no: Filter by the package tracking number associated with the claim.
            claim_types: Comma‑separated list of claim types to include (LIT, LAD, DAMAGED).
            claim_statuses: Comma‑separated list of claim status codes to include (INITIATED, IN_REVIEW, NEED_INFO,
                etc.).
            sort_by: Field to sort by; currently supports ``claimDate``.
            sort_order: Sort direction: ``ASC`` for ascending or ``DESC`` for descending (default DESC).
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[ClaimsGroupOrStr | None]("claimsGroup", claims_group),
                param[str | None]("claimNumber", claim_number),
                param[str | None]("purchaseOrderId", purchase_order_id),
                param[str | None]("trackingNo", tracking_no),
                param[str | None]("claimTypes", claim_types),
                param[str | None]("claimStatuses", claim_statuses),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[OrderOrStr | None]("sortOrder", sort_order),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[Any],
            error_mapper=list_claims_error_mapper,
            request_options=request_options,
        )

    def submit_additional_info(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: FileInput,
        document_types: list[DocumentType1 | DocumentType1Dict],
        *,
        wm_consumer_channel_type: str | None = None,
        notes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SubmitAdditionalInfoErrorBody]:
        """Adds documents or notes to an existing claim when Walmart requests more details.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Additional supporting file.
            document_types: Mapping for each uploaded file.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            notes: Additional information requested by Walmart
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(
                file_part("files", files),
                param[list[DocumentType1 | DocumentType1Dict]]("documentTypes", document_types),
                param[str | None]("notes", notes),
            ),
            decoder=json_decoder[Any],
            error_mapper=submit_additional_info_error_mapper,
            request_options=request_options,
        )

    def submit_claim(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: FileInput,
        document_types: list[DocumentType | DocumentTypeDict],
        payload: Payload | PayloadDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SubmitClaimErrorBody]:
        """Creates a shipment-protection claim. Send multipart/form-data with files, documentTypes, and payload.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Supporting file (image, PDF, etc.).
            document_types: Maps each uploaded file to its document category.
            payload: Claim details.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/claims/shipment-protection/claim"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(
                file_part("files", files),
                param[list[DocumentType | DocumentTypeDict]]("documentTypes", document_types),
                param[Payload | PayloadDict]("payload", payload),
            ),
            decoder=json_decoder[Any],
            error_mapper=submit_claim_error_mapper,
            request_options=request_options,
        )


class AsyncShipmentProtectionWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def download_claim_documents(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AsyncFileResponse, DownloadClaimDocumentsErrorBody]:
        """Returns a ZIP file containing one or more uploaded claim documents.<br><b style='color:green;'>Market
        availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            body: The request body.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}/documents"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3ClaimsShipmentProtectionClaimDocumentsRequest | V3ClaimsShipmentProtectionClaimDocumentsRequestDict
            ](body),
            decoder=async_file_decoder,
            error_mapper=download_claim_documents_error_mapper,
            request_options=request_options,
        )

    async def get_claim_details(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetClaimDetailsErrorBody]:
        """Retrieves detailed information for a single claim.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[Any],
            error_mapper=get_claim_details_error_mapper,
            request_options=request_options,
        )

    async def get_claim_history(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3ClaimsShipmentProtectionClaimHistoryResponse, GetClaimHistoryErrorBody]:
        """Returns a chronological log of status changes, notes, and uploaded documents.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}/history"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[V3ClaimsShipmentProtectionClaimHistoryResponse],
            error_mapper=get_claim_history_error_mapper,
            request_options=request_options,
        )

    async def list_claims(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        claims_group: ClaimsGroupOrStr | None = None,
        claim_number: str | None = None,
        purchase_order_id: str | None = None,
        tracking_no: str | None = None,
        claim_types: str | None = None,
        claim_statuses: str | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: OrderOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListClaimsErrorBody]:
        """Returns a paginated list of claims, with optional filters.<br><b style='color:green;'>Market availability: US
        Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            limit: Maximum number of results to return in the response page (default 25, maximum 300).
            offset: Zero‑based index of the first result to return (default 0). Use together with ``limit`` for
                pagination.
            claims_group: Filter claims by broad status group: OPEN, ACTION_NEEDED, or CLOSED.
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            purchase_order_id: Filter by the Walmart purchase order ID associated with the claim.
            tracking_no: Filter by the package tracking number associated with the claim.
            claim_types: Comma‑separated list of claim types to include (LIT, LAD, DAMAGED).
            claim_statuses: Comma‑separated list of claim status codes to include (INITIATED, IN_REVIEW, NEED_INFO,
                etc.).
            sort_by: Field to sort by; currently supports ``claimDate``.
            sort_order: Sort direction: ``ASC`` for ascending or ``DESC`` for descending (default DESC).
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/claims/shipment-protection"),
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[ClaimsGroupOrStr | None]("claimsGroup", claims_group),
                param[str | None]("claimNumber", claim_number),
                param[str | None]("purchaseOrderId", purchase_order_id),
                param[str | None]("trackingNo", tracking_no),
                param[str | None]("claimTypes", claim_types),
                param[str | None]("claimStatuses", claim_statuses),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[OrderOrStr | None]("sortOrder", sort_order),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[Any],
            error_mapper=list_claims_error_mapper,
            request_options=request_options,
        )

    async def submit_additional_info(
        self,
        claim_number: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: AsyncFileInput,
        document_types: list[DocumentType1 | DocumentType1Dict],
        *,
        wm_consumer_channel_type: str | None = None,
        notes: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SubmitAdditionalInfoErrorBody]:
        """Adds documents or notes to an existing claim when Walmart requests more details.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            claim_number: Exact claim number for filtering (query) or identifying a specific claim (path).
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Additional supporting file.
            document_types: Mapping for each uploaded file.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            notes: Additional information requested by Walmart
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v3/claims/shipment-protection/claim/{claimNumber}"),
            path_params=[param[str]("claimNumber", claim_number)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(
                file_part("files", files),
                param[list[DocumentType1 | DocumentType1Dict]]("documentTypes", document_types),
                param[str | None]("notes", notes),
            ),
            decoder=async_json_decoder[Any],
            error_mapper=submit_additional_info_error_mapper,
            request_options=request_options,
        )

    async def submit_claim(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        files: AsyncFileInput,
        document_types: list[DocumentType | DocumentTypeDict],
        payload: Payload | PayloadDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SubmitClaimErrorBody]:
        """Creates a shipment-protection claim. Send multipart/form-data with files, documentTypes, and payload.<br><b
        style='color:green;'>Market availability: US Only</b>

        Args:
            wm_sec_access_token: The access token retrieved in the Token API call.
            wm_qos_correlation_id: A unique ID which identifies each API call and is used to track and debug issues; use
                a randomly generated GUID for this ID.
            wm_svc_name: Walmart service name—for Marketplace APIs simply use ``Walmart Service Name`` or the service
                identifier provided by Walmart.
            files: Supporting file (image, PDF, etc.).
            document_types: Maps each uploaded file to its document category.
            payload: Claim details.
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/claims/shipment-protection/claim"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(
                file_part("files", files),
                param[list[DocumentType | DocumentTypeDict]]("documentTypes", document_types),
                param[Payload | PayloadDict]("payload", payload),
            ),
            decoder=async_json_decoder[Any],
            error_mapper=submit_claim_error_mapper,
            request_options=request_options,
        )

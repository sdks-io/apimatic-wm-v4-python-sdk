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
from ..errors.get_issue_types_error import GetIssueTypesErrorBody, get_issue_types_error_mapper
from ..errors.search_item_issues_error import SearchItemIssuesErrorBody, search_item_issues_error_mapper
from ..models.enums.accept import Accept, AcceptOrStr
from ..models.enums.wm_global_version import WmGlobalVersion, WmGlobalVersionOrStr
from ..models.enums.wm_market import WmMarket, WmMarketOrStr
from ..models.issue_metadata import IssueMetadata
from ..models.item_diagnostic_search_request import ItemDiagnosticSearchRequest, ItemDiagnosticSearchRequestDict
from ..models.item_diagnostic_search_response import ItemDiagnosticSearchResponse
from ..server.server import Server


class SemItemDiagnostics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SemItemDiagnosticsWithRawResponse(client, server, auth)

    def get_issue_types(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> dict[str, IssueMetadata]:
        """Returns the complete, authoritative metadata for all SEM eligibility issue types (~61 issue types,
        ~5KB).<br><b style='color:green;'>Market availability: US only</b>

        Items used in Search Engine Marketing (SEM) campaigns such as Google Shopping Ads must meet specific content,
        quality, and policy requirements before they can be advertised on search engines. When items fail to meet these
        requirements, they are flagged with specific issue types that either **block** the item from being advertised
        entirely or **limit** its visibility and performance in SEM.

        This endpoint returns the complete catalog of all issue types that can affect an item's SEM eligibility, along
        with human-readable names, descriptions, remediation guidance, severity categories, and help links. It serves as
        the **single source of truth** for issue metadata.

        ### Current scope The issue types returned by this endpoint apply to items that are currently part of active SEM
        campaigns. The ``POST /item-issues/search`` endpoint uses these issue types to report diagnostics on campaign
        items.

        ### Future extensibility In a future release, the ``POST /item-issues/search`` endpoint will support querying
        diagnostic issues for any item in the seller's catalog — even items not yet added to a campaign — using the
        ``itemId`` filter. The same issue types returned by this endpoint will apply to those items as well, enabling
        sellers to proactively diagnose and fix issues before campaign onboarding.

        ### SEM eligibility issue categories Each issue type belongs to one of three categories that indicate its impact
        on an item's ability to be advertised on search engines:

        | Category | Count | SEM Impact |
        |--------------|-------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | ~49 | Item **cannot be advertised** on search engines. Must be resolved before the item can
            appear in SEM ads. Examples: ``ITEM_OUT_OF_STOCK``, ``POLICY_VIOLATION``, ``MISSING_INVALID_TITLE``,
            ``INVALID_IMAGE``, ``BUYBOX_NOT_WINNER`` |
        | ``LIMITED`` | ~11 | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: ``TITLE_TOO_LONG``,
            ``LOW_IMAGE_QUALITY``, ``DESCRIPTION_TOO_SHORT``, ``LOW_OFFER_LISTING_QUALITY`` |
        | ``NO_ISSUES`` | ~1 | Informational statuses such as ``DUPLICATE_OFFER`` — item has no SEM eligibility issues |

        ### Actionable vs non-actionable issues Each issue type includes an ``isFixable`` flag that indicates whether
        the seller can resolve the issue:
        - ``isFixable=true``: Seller can take action to restore or improve SEM eligibility (For example, restock
            inventory, update title, improve image quality). Partners should surface these with a "Fix Now" UI
            affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations, BuyBox
            eligibility). Partners should display these as informational — the seller cannot directly resolve them.

        ### Response structure The response is a map keyed by ``issueType`` (string), where each value is an
        ``IssueMetadata`` object containing:
        - ``issueName``: Human-readable short headline for UI display (For example, "Item Out of Stock")
        - ``issueCategory``: SEM eligibility impact — ``BLOCKED`` (cannot advertise on search engines) or ``LIMITED``
            (reduced SEM visibility)
        - ``isFixable``: Whether the partner can remediate this issue to restore SEM eligibility
        - ``issueDescription``: Human-readable description with specific remediation guidance (For example, "Item is out
            of stock. Add inventory to make the item available.")
        - ``learnMoreUrl``: Help link to Walmart-hosted or Google support documentation for step-by-step remediation.
            May be null for some issue types.

        ### Recommended usage pattern
        1. Call this endpoint **once** on application initialization
        2. Cache the result locally (recommended **TTL: 24 hours**)
        3. Use cached metadata to enrich items returned by the ``POST /item-issues/search`` endpoint — match each item's
            ``issueType`` to the cached metadata for display name, description, and help links
        4. Use ``isFixable`` to drive UI affordances: show "Fix Now" buttons for fixable SEM issues, informational
            badges for non-fixable ones
        5. Use ``learnMoreUrl`` to deep-link to help documentation for step-by-step remediation guidance
        6. Use ``issueCategory`` to color-code or badge issues in your UI: red for ``BLOCKED`` (cannot advertise),
            yellow for ``LIMITED`` (reduced SEM performance)

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Issue types metadata retrieved successfully

        Raises:
            ApiError: Unauthorized - Missing, invalid, or expired bearer token. Forbidden - Seller does not have access
                to SEM advertising features. Rate limit exceeded - You have exceeded your API calls threshold. Internal
                server error - Unexpected server error. Service Unavailable - Service is temporarily unavailable.
                ``error`` is ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            self._with_raw_response.get_issue_types(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def search_item_issues(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemDiagnosticSearchResponse:
        """Search for item-level diagnostic issues that block or limit items from being used in Search Engine Marketing
        (SEM). Returns paginated, item-level diagnostic details including campaign associations, issue types, severity,
        remediation guidance, and overall item status.<br><b style='color:green;'>Market availability: US only</b>

        Items in SEM campaigns must meet content, quality, and policy requirements before they can be advertised on
        search engines (For example, Google Shopping Ads). This endpoint surfaces the specific issues preventing or
        limiting an item's SEM eligibility, along with actionable remediation guidance so sellers can resolve problems
        and restore advertising reach.

        ### Current scope This endpoint currently returns diagnostics for **items that are part of active SEM
        campaigns** for the authenticated seller. Each item in the response includes its ``campaignAssociations`` — the
        list of campaigns the item belongs to. Items not associated with any campaign are not included in the results.

        ### Default behavior
        - When no request body is provided, defaults to ``offset=0``, ``limit=100`` with no filters
        - When no ``issueCategory`` filter is provided, returns **only items with issues** (``BLOCKED`` or ``LIMITED``)
        - To include healthy items, explicitly pass ``issueCategory`` filter with ``NO_ISSUES`` or all three values
        - By default, the API prioritizes returning actionable diagnostic issues rather than healthy items. This reduces
            payload size and improves relevance

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Max Values | Description |
        |-----------------|-------------------------------------------|------------|----------------------------------------------------------|
        | ``issues`` | Any valid ``issueType`` enum value | 100 | Filter by specific SEM issue types (For example,
            ``ITEM_OUT_OF_STOCK``, ``TITLE_TOO_LONG``, ``POLICY_VIOLATION``) |
        | ``issueCategory`` | ``LIMITED``, ``BLOCKED``, ``NO_ISSUES`` | 100 | Filter by SEM issue severity — ``BLOCKED``
            items cannot be advertised at all, ``LIMITED`` items have reduced SEM performance |
        | ``itemId`` | Numeric string item IDs | 100 | Filter by Walmart catalog item identifiers within the seller's
            active campaigns. *In a future release, this filter will also support items outside of campaigns.* |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata including ``hasNextPage``/``hasPreviousPage`` for convenient UI
            navigation
        - ``data``: Array of item-level diagnostics. Each item appears **once** per unique ``offerId`` with all campaign
            associations listed. Each item includes an ``issueCategory`` field representing the overall SEM eligibility
            status of the item, and an ``issues`` array containing issue type identifiers. Issues are item-level, not
            campaign-specific — a blocked item is blocked in all SEM campaigns it belongs to.

        Issue metadata (name, description, fixability, help links) is not included in this response. Partners should use
        the dedicated ``GET /item-issues/issue-types`` endpoint to retrieve complete issue metadata and cache it locally
        (TTL: 24 hours).

        ### Issue categories
        | Category | SEM Impact |
        |--------------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in
            SEM ads. Examples: out of stock, missing title, policy violation, invalid image. |
        | ``LIMITED`` | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: title too long, low image quality,
            description too short. |
        | ``NO_ISSUES`` | Item has no SEM issues and can be advertised normally with full visibility. |

        ### Actionable vs non-actionable issues Each issue type has an ``isFixable`` flag available via the ``GET
        /item-issues/issue-types`` reference endpoint:
        - ``isFixable=true``: Seller can fix the issue to restore SEM eligibility (For example, restock inventory,
            update title, fix image). Partners should surface these with a "Fix Now" UI affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations). Partners
            should display these as informational — the seller cannot directly resolve them.

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination and filters. Defaults to ``offset=0``, ``limit=100`` with no
                filters if body is absent. When no ``issueCategory`` filter is provided, only items with issues
                (``BLOCKED`` or ``LIMITED``) are returned. This reduces payload size and improves relevance —
                diagnostics API consumers typically want problems, not healthy-item confirmation. To include all items,
                explicitly pass ``issueCategory`` filter with all three values: ``LIMITED``, ``BLOCKED``, ``NO_ISSUES``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters or malformed request body. Unauthorized - Missing,
                invalid, or expired bearer token. Forbidden - Seller does not have access to SEM advertising features.
                Unprocessable Entity - Request is malformed (For example, request body passed as string instead of JSON
                object). Rate limit exceeded - You have exceeded your API calls threshold. Internal server error -
                Unexpected server error. Service unavailable - Service is temporarily unavailable. ``error`` is
                ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            self._with_raw_response.search_item_issues(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                accept=accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SemItemDiagnosticsWithRawResponse:
        return self._with_raw_response


class AsyncSemItemDiagnostics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSemItemDiagnosticsWithRawResponse(client, server, auth)

    async def get_issue_types(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> dict[str, IssueMetadata]:
        """Returns the complete, authoritative metadata for all SEM eligibility issue types (~61 issue types,
        ~5KB).<br><b style='color:green;'>Market availability: US only</b>

        Items used in Search Engine Marketing (SEM) campaigns such as Google Shopping Ads must meet specific content,
        quality, and policy requirements before they can be advertised on search engines. When items fail to meet these
        requirements, they are flagged with specific issue types that either **block** the item from being advertised
        entirely or **limit** its visibility and performance in SEM.

        This endpoint returns the complete catalog of all issue types that can affect an item's SEM eligibility, along
        with human-readable names, descriptions, remediation guidance, severity categories, and help links. It serves as
        the **single source of truth** for issue metadata.

        ### Current scope The issue types returned by this endpoint apply to items that are currently part of active SEM
        campaigns. The ``POST /item-issues/search`` endpoint uses these issue types to report diagnostics on campaign
        items.

        ### Future extensibility In a future release, the ``POST /item-issues/search`` endpoint will support querying
        diagnostic issues for any item in the seller's catalog — even items not yet added to a campaign — using the
        ``itemId`` filter. The same issue types returned by this endpoint will apply to those items as well, enabling
        sellers to proactively diagnose and fix issues before campaign onboarding.

        ### SEM eligibility issue categories Each issue type belongs to one of three categories that indicate its impact
        on an item's ability to be advertised on search engines:

        | Category | Count | SEM Impact |
        |--------------|-------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | ~49 | Item **cannot be advertised** on search engines. Must be resolved before the item can
            appear in SEM ads. Examples: ``ITEM_OUT_OF_STOCK``, ``POLICY_VIOLATION``, ``MISSING_INVALID_TITLE``,
            ``INVALID_IMAGE``, ``BUYBOX_NOT_WINNER`` |
        | ``LIMITED`` | ~11 | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: ``TITLE_TOO_LONG``,
            ``LOW_IMAGE_QUALITY``, ``DESCRIPTION_TOO_SHORT``, ``LOW_OFFER_LISTING_QUALITY`` |
        | ``NO_ISSUES`` | ~1 | Informational statuses such as ``DUPLICATE_OFFER`` — item has no SEM eligibility issues |

        ### Actionable vs non-actionable issues Each issue type includes an ``isFixable`` flag that indicates whether
        the seller can resolve the issue:
        - ``isFixable=true``: Seller can take action to restore or improve SEM eligibility (For example, restock
            inventory, update title, improve image quality). Partners should surface these with a "Fix Now" UI
            affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations, BuyBox
            eligibility). Partners should display these as informational — the seller cannot directly resolve them.

        ### Response structure The response is a map keyed by ``issueType`` (string), where each value is an
        ``IssueMetadata`` object containing:
        - ``issueName``: Human-readable short headline for UI display (For example, "Item Out of Stock")
        - ``issueCategory``: SEM eligibility impact — ``BLOCKED`` (cannot advertise on search engines) or ``LIMITED``
            (reduced SEM visibility)
        - ``isFixable``: Whether the partner can remediate this issue to restore SEM eligibility
        - ``issueDescription``: Human-readable description with specific remediation guidance (For example, "Item is out
            of stock. Add inventory to make the item available.")
        - ``learnMoreUrl``: Help link to Walmart-hosted or Google support documentation for step-by-step remediation.
            May be null for some issue types.

        ### Recommended usage pattern
        1. Call this endpoint **once** on application initialization
        2. Cache the result locally (recommended **TTL: 24 hours**)
        3. Use cached metadata to enrich items returned by the ``POST /item-issues/search`` endpoint — match each item's
            ``issueType`` to the cached metadata for display name, description, and help links
        4. Use ``isFixable`` to drive UI affordances: show "Fix Now" buttons for fixable SEM issues, informational
            badges for non-fixable ones
        5. Use ``learnMoreUrl`` to deep-link to help documentation for step-by-step remediation guidance
        6. Use ``issueCategory`` to color-code or badge issues in your UI: red for ``BLOCKED`` (cannot advertise),
            yellow for ``LIMITED`` (reduced SEM performance)

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Issue types metadata retrieved successfully

        Raises:
            ApiError: Unauthorized - Missing, invalid, or expired bearer token. Forbidden - Seller does not have access
                to SEM advertising features. Rate limit exceeded - You have exceeded your API calls threshold. Internal
                server error - Unexpected server error. Service Unavailable - Service is temporarily unavailable.
                ``error`` is ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_issue_types(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def search_item_issues(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemDiagnosticSearchResponse:
        """Search for item-level diagnostic issues that block or limit items from being used in Search Engine Marketing
        (SEM). Returns paginated, item-level diagnostic details including campaign associations, issue types, severity,
        remediation guidance, and overall item status.<br><b style='color:green;'>Market availability: US only</b>

        Items in SEM campaigns must meet content, quality, and policy requirements before they can be advertised on
        search engines (For example, Google Shopping Ads). This endpoint surfaces the specific issues preventing or
        limiting an item's SEM eligibility, along with actionable remediation guidance so sellers can resolve problems
        and restore advertising reach.

        ### Current scope This endpoint currently returns diagnostics for **items that are part of active SEM
        campaigns** for the authenticated seller. Each item in the response includes its ``campaignAssociations`` — the
        list of campaigns the item belongs to. Items not associated with any campaign are not included in the results.

        ### Default behavior
        - When no request body is provided, defaults to ``offset=0``, ``limit=100`` with no filters
        - When no ``issueCategory`` filter is provided, returns **only items with issues** (``BLOCKED`` or ``LIMITED``)
        - To include healthy items, explicitly pass ``issueCategory`` filter with ``NO_ISSUES`` or all three values
        - By default, the API prioritizes returning actionable diagnostic issues rather than healthy items. This reduces
            payload size and improves relevance

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Max Values | Description |
        |-----------------|-------------------------------------------|------------|----------------------------------------------------------|
        | ``issues`` | Any valid ``issueType`` enum value | 100 | Filter by specific SEM issue types (For example,
            ``ITEM_OUT_OF_STOCK``, ``TITLE_TOO_LONG``, ``POLICY_VIOLATION``) |
        | ``issueCategory`` | ``LIMITED``, ``BLOCKED``, ``NO_ISSUES`` | 100 | Filter by SEM issue severity — ``BLOCKED``
            items cannot be advertised at all, ``LIMITED`` items have reduced SEM performance |
        | ``itemId`` | Numeric string item IDs | 100 | Filter by Walmart catalog item identifiers within the seller's
            active campaigns. *In a future release, this filter will also support items outside of campaigns.* |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata including ``hasNextPage``/``hasPreviousPage`` for convenient UI
            navigation
        - ``data``: Array of item-level diagnostics. Each item appears **once** per unique ``offerId`` with all campaign
            associations listed. Each item includes an ``issueCategory`` field representing the overall SEM eligibility
            status of the item, and an ``issues`` array containing issue type identifiers. Issues are item-level, not
            campaign-specific — a blocked item is blocked in all SEM campaigns it belongs to.

        Issue metadata (name, description, fixability, help links) is not included in this response. Partners should use
        the dedicated ``GET /item-issues/issue-types`` endpoint to retrieve complete issue metadata and cache it locally
        (TTL: 24 hours).

        ### Issue categories
        | Category | SEM Impact |
        |--------------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in
            SEM ads. Examples: out of stock, missing title, policy violation, invalid image. |
        | ``LIMITED`` | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: title too long, low image quality,
            description too short. |
        | ``NO_ISSUES`` | Item has no SEM issues and can be advertised normally with full visibility. |

        ### Actionable vs non-actionable issues Each issue type has an ``isFixable`` flag available via the ``GET
        /item-issues/issue-types`` reference endpoint:
        - ``isFixable=true``: Seller can fix the issue to restore SEM eligibility (For example, restock inventory,
            update title, fix image). Partners should surface these with a "Fix Now" UI affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations). Partners
            should display these as informational — the seller cannot directly resolve them.

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination and filters. Defaults to ``offset=0``, ``limit=100`` with no
                filters if body is absent. When no ``issueCategory`` filter is provided, only items with issues
                (``BLOCKED`` or ``LIMITED``) are returned. This reduces payload size and improves relevance —
                diagnostics API consumers typically want problems, not healthy-item confirmation. To include all items,
                explicitly pass ``issueCategory`` filter with all three values: ``LIMITED``, ``BLOCKED``, ``NO_ISSUES``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results retrieved successfully

        Raises:
            ApiError: Bad Request - Invalid request parameters or malformed request body. Unauthorized - Missing,
                invalid, or expired bearer token. Forbidden - Seller does not have access to SEM advertising features.
                Unprocessable Entity - Request is malformed (For example, request body passed as string instead of JSON
                object). Rate limit exceeded - You have exceeded your API calls threshold. Internal server error -
                Unexpected server error. Service unavailable - Service is temporarily unavailable. ``error`` is
                ``ErrorResponse | ErrorResponse429 | RawError``."""
        return unwrap(
            await self._with_raw_response.search_item_issues(
                wm_svc_name,
                wm_qos_correlation_id,
                wm_global_version=wm_global_version,
                wm_market=wm_market,
                accept=accept,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSemItemDiagnosticsWithRawResponse:
        return self._with_raw_response


class SemItemDiagnosticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_issue_types(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[dict[str, IssueMetadata], GetIssueTypesErrorBody]:
        """Returns the complete, authoritative metadata for all SEM eligibility issue types (~61 issue types,
        ~5KB).<br><b style='color:green;'>Market availability: US only</b>

        Items used in Search Engine Marketing (SEM) campaigns such as Google Shopping Ads must meet specific content,
        quality, and policy requirements before they can be advertised on search engines. When items fail to meet these
        requirements, they are flagged with specific issue types that either **block** the item from being advertised
        entirely or **limit** its visibility and performance in SEM.

        This endpoint returns the complete catalog of all issue types that can affect an item's SEM eligibility, along
        with human-readable names, descriptions, remediation guidance, severity categories, and help links. It serves as
        the **single source of truth** for issue metadata.

        ### Current scope The issue types returned by this endpoint apply to items that are currently part of active SEM
        campaigns. The ``POST /item-issues/search`` endpoint uses these issue types to report diagnostics on campaign
        items.

        ### Future extensibility In a future release, the ``POST /item-issues/search`` endpoint will support querying
        diagnostic issues for any item in the seller's catalog — even items not yet added to a campaign — using the
        ``itemId`` filter. The same issue types returned by this endpoint will apply to those items as well, enabling
        sellers to proactively diagnose and fix issues before campaign onboarding.

        ### SEM eligibility issue categories Each issue type belongs to one of three categories that indicate its impact
        on an item's ability to be advertised on search engines:

        | Category | Count | SEM Impact |
        |--------------|-------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | ~49 | Item **cannot be advertised** on search engines. Must be resolved before the item can
            appear in SEM ads. Examples: ``ITEM_OUT_OF_STOCK``, ``POLICY_VIOLATION``, ``MISSING_INVALID_TITLE``,
            ``INVALID_IMAGE``, ``BUYBOX_NOT_WINNER`` |
        | ``LIMITED`` | ~11 | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: ``TITLE_TOO_LONG``,
            ``LOW_IMAGE_QUALITY``, ``DESCRIPTION_TOO_SHORT``, ``LOW_OFFER_LISTING_QUALITY`` |
        | ``NO_ISSUES`` | ~1 | Informational statuses such as ``DUPLICATE_OFFER`` — item has no SEM eligibility issues |

        ### Actionable vs non-actionable issues Each issue type includes an ``isFixable`` flag that indicates whether
        the seller can resolve the issue:
        - ``isFixable=true``: Seller can take action to restore or improve SEM eligibility (For example, restock
            inventory, update title, improve image quality). Partners should surface these with a "Fix Now" UI
            affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations, BuyBox
            eligibility). Partners should display these as informational — the seller cannot directly resolve them.

        ### Response structure The response is a map keyed by ``issueType`` (string), where each value is an
        ``IssueMetadata`` object containing:
        - ``issueName``: Human-readable short headline for UI display (For example, "Item Out of Stock")
        - ``issueCategory``: SEM eligibility impact — ``BLOCKED`` (cannot advertise on search engines) or ``LIMITED``
            (reduced SEM visibility)
        - ``isFixable``: Whether the partner can remediate this issue to restore SEM eligibility
        - ``issueDescription``: Human-readable description with specific remediation guidance (For example, "Item is out
            of stock. Add inventory to make the item available.")
        - ``learnMoreUrl``: Help link to Walmart-hosted or Google support documentation for step-by-step remediation.
            May be null for some issue types.

        ### Recommended usage pattern
        1. Call this endpoint **once** on application initialization
        2. Cache the result locally (recommended **TTL: 24 hours**)
        3. Use cached metadata to enrich items returned by the ``POST /item-issues/search`` endpoint — match each item's
            ``issueType`` to the cached metadata for display name, description, and help links
        4. Use ``isFixable`` to drive UI affordances: show "Fix Now" buttons for fixable SEM issues, informational
            badges for non-fixable ones
        5. Use ``learnMoreUrl`` to deep-link to help documentation for step-by-step remediation guidance
        6. Use ``issueCategory`` to color-code or badge issues in your UI: red for ``BLOCKED`` (cannot advertise),
            yellow for ``LIMITED`` (reduced SEM performance)

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/item-issues/issue-types"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[dict[str, IssueMetadata]],
            error_mapper=get_issue_types_error_mapper,
            request_options=request_options,
        )

    def search_item_issues(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemDiagnosticSearchResponse, SearchItemIssuesErrorBody]:
        """Search for item-level diagnostic issues that block or limit items from being used in Search Engine Marketing
        (SEM). Returns paginated, item-level diagnostic details including campaign associations, issue types, severity,
        remediation guidance, and overall item status.<br><b style='color:green;'>Market availability: US only</b>

        Items in SEM campaigns must meet content, quality, and policy requirements before they can be advertised on
        search engines (For example, Google Shopping Ads). This endpoint surfaces the specific issues preventing or
        limiting an item's SEM eligibility, along with actionable remediation guidance so sellers can resolve problems
        and restore advertising reach.

        ### Current scope This endpoint currently returns diagnostics for **items that are part of active SEM
        campaigns** for the authenticated seller. Each item in the response includes its ``campaignAssociations`` — the
        list of campaigns the item belongs to. Items not associated with any campaign are not included in the results.

        ### Default behavior
        - When no request body is provided, defaults to ``offset=0``, ``limit=100`` with no filters
        - When no ``issueCategory`` filter is provided, returns **only items with issues** (``BLOCKED`` or ``LIMITED``)
        - To include healthy items, explicitly pass ``issueCategory`` filter with ``NO_ISSUES`` or all three values
        - By default, the API prioritizes returning actionable diagnostic issues rather than healthy items. This reduces
            payload size and improves relevance

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Max Values | Description |
        |-----------------|-------------------------------------------|------------|----------------------------------------------------------|
        | ``issues`` | Any valid ``issueType`` enum value | 100 | Filter by specific SEM issue types (For example,
            ``ITEM_OUT_OF_STOCK``, ``TITLE_TOO_LONG``, ``POLICY_VIOLATION``) |
        | ``issueCategory`` | ``LIMITED``, ``BLOCKED``, ``NO_ISSUES`` | 100 | Filter by SEM issue severity — ``BLOCKED``
            items cannot be advertised at all, ``LIMITED`` items have reduced SEM performance |
        | ``itemId`` | Numeric string item IDs | 100 | Filter by Walmart catalog item identifiers within the seller's
            active campaigns. *In a future release, this filter will also support items outside of campaigns.* |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata including ``hasNextPage``/``hasPreviousPage`` for convenient UI
            navigation
        - ``data``: Array of item-level diagnostics. Each item appears **once** per unique ``offerId`` with all campaign
            associations listed. Each item includes an ``issueCategory`` field representing the overall SEM eligibility
            status of the item, and an ``issues`` array containing issue type identifiers. Issues are item-level, not
            campaign-specific — a blocked item is blocked in all SEM campaigns it belongs to.

        Issue metadata (name, description, fixability, help links) is not included in this response. Partners should use
        the dedicated ``GET /item-issues/issue-types`` endpoint to retrieve complete issue metadata and cache it locally
        (TTL: 24 hours).

        ### Issue categories
        | Category | SEM Impact |
        |--------------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in
            SEM ads. Examples: out of stock, missing title, policy violation, invalid image. |
        | ``LIMITED`` | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: title too long, low image quality,
            description too short. |
        | ``NO_ISSUES`` | Item has no SEM issues and can be advertised normally with full visibility. |

        ### Actionable vs non-actionable issues Each issue type has an ``isFixable`` flag available via the ``GET
        /item-issues/issue-types`` reference endpoint:
        - ``isFixable=true``: Seller can fix the issue to restore SEM eligibility (For example, restock inventory,
            update title, fix image). Partners should surface these with a "Fix Now" UI affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations). Partners
            should display these as informational — the seller cannot directly resolve them.

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination and filters. Defaults to ``offset=0``, ``limit=100`` with no
                filters if body is absent. When no ``issueCategory`` filter is provided, only items with issues
                (``BLOCKED`` or ``LIMITED``) are returned. This reduces payload size and improves relevance —
                diagnostics API consumers typically want problems, not healthy-item confirmation. To include all items,
                explicitly pass ``issueCategory`` filter with all three values: ``LIMITED``, ``BLOCKED``, ``NO_ISSUES``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/item-issues/search"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[AcceptOrStr]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ItemDiagnosticSearchResponse],
            error_mapper=search_item_issues_error_mapper,
            request_options=request_options,
        )


class AsyncSemItemDiagnosticsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_issue_types(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[dict[str, IssueMetadata], GetIssueTypesErrorBody]:
        """Returns the complete, authoritative metadata for all SEM eligibility issue types (~61 issue types,
        ~5KB).<br><b style='color:green;'>Market availability: US only</b>

        Items used in Search Engine Marketing (SEM) campaigns such as Google Shopping Ads must meet specific content,
        quality, and policy requirements before they can be advertised on search engines. When items fail to meet these
        requirements, they are flagged with specific issue types that either **block** the item from being advertised
        entirely or **limit** its visibility and performance in SEM.

        This endpoint returns the complete catalog of all issue types that can affect an item's SEM eligibility, along
        with human-readable names, descriptions, remediation guidance, severity categories, and help links. It serves as
        the **single source of truth** for issue metadata.

        ### Current scope The issue types returned by this endpoint apply to items that are currently part of active SEM
        campaigns. The ``POST /item-issues/search`` endpoint uses these issue types to report diagnostics on campaign
        items.

        ### Future extensibility In a future release, the ``POST /item-issues/search`` endpoint will support querying
        diagnostic issues for any item in the seller's catalog — even items not yet added to a campaign — using the
        ``itemId`` filter. The same issue types returned by this endpoint will apply to those items as well, enabling
        sellers to proactively diagnose and fix issues before campaign onboarding.

        ### SEM eligibility issue categories Each issue type belongs to one of three categories that indicate its impact
        on an item's ability to be advertised on search engines:

        | Category | Count | SEM Impact |
        |--------------|-------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | ~49 | Item **cannot be advertised** on search engines. Must be resolved before the item can
            appear in SEM ads. Examples: ``ITEM_OUT_OF_STOCK``, ``POLICY_VIOLATION``, ``MISSING_INVALID_TITLE``,
            ``INVALID_IMAGE``, ``BUYBOX_NOT_WINNER`` |
        | ``LIMITED`` | ~11 | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: ``TITLE_TOO_LONG``,
            ``LOW_IMAGE_QUALITY``, ``DESCRIPTION_TOO_SHORT``, ``LOW_OFFER_LISTING_QUALITY`` |
        | ``NO_ISSUES`` | ~1 | Informational statuses such as ``DUPLICATE_OFFER`` — item has no SEM eligibility issues |

        ### Actionable vs non-actionable issues Each issue type includes an ``isFixable`` flag that indicates whether
        the seller can resolve the issue:
        - ``isFixable=true``: Seller can take action to restore or improve SEM eligibility (For example, restock
            inventory, update title, improve image quality). Partners should surface these with a "Fix Now" UI
            affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations, BuyBox
            eligibility). Partners should display these as informational — the seller cannot directly resolve them.

        ### Response structure The response is a map keyed by ``issueType`` (string), where each value is an
        ``IssueMetadata`` object containing:
        - ``issueName``: Human-readable short headline for UI display (For example, "Item Out of Stock")
        - ``issueCategory``: SEM eligibility impact — ``BLOCKED`` (cannot advertise on search engines) or ``LIMITED``
            (reduced SEM visibility)
        - ``isFixable``: Whether the partner can remediate this issue to restore SEM eligibility
        - ``issueDescription``: Human-readable description with specific remediation guidance (For example, "Item is out
            of stock. Add inventory to make the item available.")
        - ``learnMoreUrl``: Help link to Walmart-hosted or Google support documentation for step-by-step remediation.
            May be null for some issue types.

        ### Recommended usage pattern
        1. Call this endpoint **once** on application initialization
        2. Cache the result locally (recommended **TTL: 24 hours**)
        3. Use cached metadata to enrich items returned by the ``POST /item-issues/search`` endpoint — match each item's
            ``issueType`` to the cached metadata for display name, description, and help links
        4. Use ``isFixable`` to drive UI affordances: show "Fix Now" buttons for fixable SEM issues, informational
            badges for non-fixable ones
        5. Use ``learnMoreUrl`` to deep-link to help documentation for step-by-step remediation guidance
        6. Use ``issueCategory`` to color-code or badge issues in your UI: red for ``BLOCKED`` (cannot advertise),
            yellow for ``LIMITED`` (reduced SEM performance)

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/advertising/sem/item-issues/issue-types"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[dict[str, IssueMetadata]],
            error_mapper=get_issue_types_error_mapper,
            request_options=request_options,
        )

    async def search_item_issues(
        self,
        wm_svc_name: str,
        wm_qos_correlation_id: str,
        *,
        wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1,
        wm_market: WmMarketOrStr = WmMarket.US,
        accept: AcceptOrStr = Accept.APPLICATION_JSON,
        wm_consumer_channel_type: str | None = None,
        body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemDiagnosticSearchResponse, SearchItemIssuesErrorBody]:
        """Search for item-level diagnostic issues that block or limit items from being used in Search Engine Marketing
        (SEM). Returns paginated, item-level diagnostic details including campaign associations, issue types, severity,
        remediation guidance, and overall item status.<br><b style='color:green;'>Market availability: US only</b>

        Items in SEM campaigns must meet content, quality, and policy requirements before they can be advertised on
        search engines (For example, Google Shopping Ads). This endpoint surfaces the specific issues preventing or
        limiting an item's SEM eligibility, along with actionable remediation guidance so sellers can resolve problems
        and restore advertising reach.

        ### Current scope This endpoint currently returns diagnostics for **items that are part of active SEM
        campaigns** for the authenticated seller. Each item in the response includes its ``campaignAssociations`` — the
        list of campaigns the item belongs to. Items not associated with any campaign are not included in the results.

        ### Default behavior
        - When no request body is provided, defaults to ``offset=0``, ``limit=100`` with no filters
        - When no ``issueCategory`` filter is provided, returns **only items with issues** (``BLOCKED`` or ``LIMITED``)
        - To include healthy items, explicitly pass ``issueCategory`` filter with ``NO_ISSUES`` or all three values
        - By default, the API prioritizes returning actionable diagnostic issues rather than healthy items. This reduces
            payload size and improves relevance

        ### Supported filters Filters are combined with AND logic. Multiple values within a single filter act as OR.

        | Filter Field | Supported Values | Max Values | Description |
        |-----------------|-------------------------------------------|------------|----------------------------------------------------------|
        | ``issues`` | Any valid ``issueType`` enum value | 100 | Filter by specific SEM issue types (For example,
            ``ITEM_OUT_OF_STOCK``, ``TITLE_TOO_LONG``, ``POLICY_VIOLATION``) |
        | ``issueCategory`` | ``LIMITED``, ``BLOCKED``, ``NO_ISSUES`` | 100 | Filter by SEM issue severity — ``BLOCKED``
            items cannot be advertised at all, ``LIMITED`` items have reduced SEM performance |
        | ``itemId`` | Numeric string item IDs | 100 | Filter by Walmart catalog item identifiers within the seller's
            active campaigns. *In a future release, this filter will also support items outside of campaigns.* |

        ### Response structure Each response contains two top-level fields:
        - ``pagination``: Standard pagination metadata including ``hasNextPage``/``hasPreviousPage`` for convenient UI
            navigation
        - ``data``: Array of item-level diagnostics. Each item appears **once** per unique ``offerId`` with all campaign
            associations listed. Each item includes an ``issueCategory`` field representing the overall SEM eligibility
            status of the item, and an ``issues`` array containing issue type identifiers. Issues are item-level, not
            campaign-specific — a blocked item is blocked in all SEM campaigns it belongs to.

        Issue metadata (name, description, fixability, help links) is not included in this response. Partners should use
        the dedicated ``GET /item-issues/issue-types`` endpoint to retrieve complete issue metadata and cache it locally
        (TTL: 24 hours).

        ### Issue categories
        | Category | SEM Impact |
        |--------------|--------------------------------------------------------------------------------|
        | ``BLOCKED`` | Item **cannot be advertised** on search engines. Must be resolved before the item can appear in
            SEM ads. Examples: out of stock, missing title, policy violation, invalid image. |
        | ``LIMITED`` | Item **can be advertised but with reduced visibility** or performance on search engines.
            Resolving these issues improves ad reach and effectiveness. Examples: title too long, low image quality,
            description too short. |
        | ``NO_ISSUES`` | Item has no SEM issues and can be advertised normally with full visibility. |

        ### Actionable vs non-actionable issues Each issue type has an ``isFixable`` flag available via the ``GET
        /item-issues/issue-types`` reference endpoint:
        - ``isFixable=true``: Seller can fix the issue to restore SEM eligibility (For example, restock inventory,
            update title, fix image). Partners should surface these with a "Fix Now" UI affordance.
        - ``isFixable=false``: Requires Walmart or system intervention (For example, Google policy violations). Partners
            should display these as informational — the seller cannot directly resolve them.

        Args:
            wm_svc_name: Specifies the name of the Walmart service being called.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.
            wm_global_version: The version of the global API used.
            wm_market: Identifies the Walmart Marketplace region for the request.
            accept: The expected response content type.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.
            body: Optional search request with pagination and filters. Defaults to ``offset=0``, ``limit=100`` with no
                filters if body is absent. When no ``issueCategory`` filter is provided, only items with issues
                (``BLOCKED`` or ``LIMITED``) are returned. This reduces payload size and improves relevance —
                diagnostics API consumers typically want problems, not healthy-item confirmation. To include all items,
                explicitly pass ``issueCategory`` filter with all three values: ``LIMITED``, ``BLOCKED``, ``NO_ISSUES``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/advertising/sem/item-issues/search"),
            headers=[
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[WmMarketOrStr]("WM_MARKET", wm_market),
                param[AcceptOrStr]("Accept", accept),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ItemDiagnosticSearchResponse],
            error_mapper=search_item_issues_error_mapper,
            request_options=request_options,
        )

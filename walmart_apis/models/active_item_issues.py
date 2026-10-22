from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .campaign_ref import CampaignRef, CampaignRefDict
from .enums.issue_category import IssueCategoryOrStr
from .issue import Issue, IssueDict


class ActiveItemIssues(SdkBaseModel):
    """Item-level diagnostic data including product details, campaign associations, overall item status, and list of
    issues.

    Each ``ActiveItemIssues`` object appears **once** per unique ``offerId``. The ``campaignAssociations`` array lists
    all campaigns the item belongs to. Issues are **item-level**, not campaign-specific — the same issue applies
    regardless of which campaign the item is in.

    ### Identifier Contract
    | Field | Source | Format | Description |
    |-----------|------------------|-------------------------|--------------------------------------------------------------------------|
    | ``offerId`` | Walmart-assigned | String | Uniquely identifies a specific offer (item + seller). Recommended
        primary key for partner systems. |
    | ``itemId`` | Walmart-assigned | Numeric string | Walmart catalog item identifier. Shared across sellers offering
        the same product. |
    | ``sku`` | Partner-assigned | Alphanumeric (partner-defined) | The partner's own SKU. Never a Walmart-assigned
        value. |"""

    offer_id: Optional[str] = Field(default=UNSET, alias="offerId")
    """Unique offer identifier. Enables deep-linking, correlation with partner inventory systems, and disambiguation of
    items across campaigns."""

    item_id: Optional[str] = Field(default=UNSET, alias="itemId")
    """Walmart catalog item identifier (numeric string). Shared across sellers offering the same product."""

    sku: Optional[str] = UNSET
    """Partner-assigned Stock Keeping Unit. Always the partner's own SKU, never a Walmart-assigned value."""

    product_image_url: Optional[str] = Field(default=UNSET, alias="productImageUrl")
    """Product image URL."""

    product_name: Optional[str] = Field(default=UNSET, alias="productName")
    """Product display name."""

    campaign_associations: Optional[list[CampaignRef]] = Field(default=UNSET, alias="campaignAssociations")
    """List of all campaigns this item is associated with. A single item may participate in multiple campaigns."""

    issue_category: Optional[IssueCategoryOrStr] = Field(default=UNSET, alias="issueCategory")
    """Overall SEM eligibility status derived from all issues affecting this item.

    - **NO_ISSUES**: Item has no SEM issues and can be advertised on search engines with full visibility
    - **LIMITED**: Item has issues that reduce its visibility or performance in Search Engine Marketing
    - **BLOCKED**: Item has critical issues that completely prevent it from being advertised on search engines"""

    product_url: Optional[str] = Field(default=UNSET, alias="productUrl")
    """Link to item on Walmart.com."""

    issues: Optional[list[Issue]] = UNSET
    """List of issues affecting this item. Each issue contains an ``issueType`` that can be used as a lookup key into
    the issue metadata returned by the ``GET /item-issues/issue-types`` endpoint. Empty array when item has no
    issues."""


class ActiveItemIssuesDict(TypedDict):
    offer_id: NotRequired[str]
    item_id: NotRequired[str]
    sku: NotRequired[str]
    product_image_url: NotRequired[str]
    product_name: NotRequired[str]
    campaign_associations: NotRequired[list[CampaignRefDict]]
    issue_category: NotRequired[IssueCategoryOrStr]
    product_url: NotRequired[str]
    issues: NotRequired[list[IssueDict]]

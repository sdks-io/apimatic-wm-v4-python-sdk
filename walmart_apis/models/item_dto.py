from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemDto(SdkBaseModel):
    payer_id: Optional[str] = Field(default=UNSET, alias="payerId")
    """Identifier of the payer entity issuing the tax form."""

    tin: Optional[str] = UNSET
    """Taxpayer identification number associated with the payee."""

    group_id: Optional[str] = Field(default=UNSET, alias="groupId")
    """Logical grouping identifier for related transactions or sub-accounts."""

    account: Optional[str] = UNSET
    """Account identifier related to the payout or settlement."""

    form_id: Optional[str] = Field(default=UNSET, alias="formId")
    """Unique tax form identifier referenced by the download endpoint."""

    form_mod_level: Optional[str] = Field(default=UNSET, alias="formModLevel")
    """Form modification level or version indicator."""

    payee_mod_level: Optional[str] = Field(default=UNSET, alias="payeeModLevel")
    """Payee-level modification indicator."""

    tintype: Optional[str] = UNSET
    """Type of TIN provided (for example, SSN, EIN, ITIN)."""


class ItemDtoDict(TypedDict):
    payer_id: NotRequired[str]
    tin: NotRequired[str]
    group_id: NotRequired[str]
    account: NotRequired[str]
    form_id: NotRequired[str]
    form_mod_level: NotRequired[str]
    payee_mod_level: NotRequired[str]
    tintype: NotRequired[str]

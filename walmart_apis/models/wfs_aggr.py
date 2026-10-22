from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WfsAggr(SdkBaseModel):
    net_payable: Optional[float] = Field(default=UNSET, alias="netPayable")
    wfs_fullfillment_fee: Optional[float] = Field(default=UNSET, alias="wfsFullfillmentFee")
    wfs_storage_fee: Optional[float] = Field(default=UNSET, alias="wfsStorageFee")
    wfs_adjustment: Optional[float] = Field(default=UNSET, alias="wfsAdjustment")
    wfs_fee: Optional[float] = Field(default=UNSET, alias="wfsFee")
    inventory_removal_order: Optional[float] = Field(default=UNSET, alias="inventoryRemovalOrder")
    inventory_disposal_order: Optional[float] = Field(default=UNSET, alias="inventoryDisposalOrder")
    wfs_prep_service_fee: Optional[float] = Field(default=UNSET, alias="wfsPrepServiceFee")


class WfsAggrDict(TypedDict):
    net_payable: NotRequired[float]
    wfs_fullfillment_fee: NotRequired[float]
    wfs_storage_fee: NotRequired[float]
    wfs_adjustment: NotRequired[float]
    wfs_fee: NotRequired[float]
    inventory_removal_order: NotRequired[float]
    inventory_disposal_order: NotRequired[float]
    wfs_prep_service_fee: NotRequired[float]

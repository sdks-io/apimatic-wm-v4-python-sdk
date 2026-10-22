from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.inventories_dto import InventoriesDto

GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody: TypeAlias = InventoriesDto | RawError


@dataclass(frozen=True, slots=True)
class _GetMultiNodeInventoryForSkuAndAllShipnodesError:
    def map(self, status_code: int, content: bytes) -> GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[InventoriesDto](content)
            case _:
                return RawError(status_code, content)


get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper: Final[
    ErrorMapper[GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody]
] = _GetMultiNodeInventoryForSkuAndAllShipnodesError()

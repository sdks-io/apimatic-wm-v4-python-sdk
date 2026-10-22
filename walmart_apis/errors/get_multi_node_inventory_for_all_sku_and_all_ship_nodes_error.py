from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_inventories403_error1 import V3Inventories403Error1

GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody: TypeAlias = V3Inventories403Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetMultiNodeInventoryForAllSkuAndAllShipNodesError:
    def map(self, status_code: int, content: bytes) -> GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody:
        match status_code:
            case 403:
                return decode_json[V3Inventories403Error1](content)
            case _:
                return RawError(status_code, content)


get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper: Final[
    ErrorMapper[GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody]
] = _GetMultiNodeInventoryForAllSkuAndAllShipNodesError()

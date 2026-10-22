from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_fulfillment_inventory403_error1 import V3FulfillmentInventory403Error1

GetWfsinventoryErrorBody: TypeAlias = V3FulfillmentInventory403Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetWfsinventoryError:
    def map(self, status_code: int, content: bytes) -> GetWfsinventoryErrorBody:
        match status_code:
            case 403:
                return decode_json[V3FulfillmentInventory403Error1](content)
            case _:
                return RawError(status_code, content)


get_wfsinventory_error_mapper: Final[ErrorMapper[GetWfsinventoryErrorBody]] = _GetWfsinventoryError()

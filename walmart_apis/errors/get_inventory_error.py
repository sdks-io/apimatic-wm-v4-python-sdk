from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.inventory1 import Inventory1

GetInventoryErrorBody: TypeAlias = Inventory1 | RawError


@dataclass(frozen=True, slots=True)
class _GetInventoryError:
    def map(self, status_code: int, content: bytes) -> GetInventoryErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[Inventory1](content)
            case _:
                return RawError(status_code, content)


get_inventory_error_mapper: Final[ErrorMapper[GetInventoryErrorBody]] = _GetInventoryError()

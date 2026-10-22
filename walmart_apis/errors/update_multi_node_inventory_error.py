from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.multi_node_inventory_update_response_dto import MultiNodeInventoryUpdateResponseDto

UpdateMultiNodeInventoryErrorBody: TypeAlias = MultiNodeInventoryUpdateResponseDto | RawError


@dataclass(frozen=True, slots=True)
class _UpdateMultiNodeInventoryError:
    def map(self, status_code: int, content: bytes) -> UpdateMultiNodeInventoryErrorBody:
        match status_code:
            case 400 | 404:
                return decode_json[MultiNodeInventoryUpdateResponseDto](content)
            case _:
                return RawError(status_code, content)


update_multi_node_inventory_error_mapper: Final[
    ErrorMapper[UpdateMultiNodeInventoryErrorBody]
] = _UpdateMultiNodeInventoryError()

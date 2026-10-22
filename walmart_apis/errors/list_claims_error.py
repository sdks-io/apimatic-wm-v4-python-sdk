from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_claims_shipment_protection400_error1 import V3ClaimsShipmentProtection400Error1
from ..models.v3_claims_shipment_protection401_error1 import V3ClaimsShipmentProtection401Error1
from ..models.v3_claims_shipment_protection500_error1 import V3ClaimsShipmentProtection500Error1

ListClaimsErrorBody: TypeAlias = (
    V3ClaimsShipmentProtection400Error1
    | V3ClaimsShipmentProtection401Error1
    | V3ClaimsShipmentProtection500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ListClaimsError:
    def map(self, status_code: int, content: bytes) -> ListClaimsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3ClaimsShipmentProtection400Error1](content)
            case 401:
                return decode_json[V3ClaimsShipmentProtection401Error1](content)
            case 500:
                return decode_json[V3ClaimsShipmentProtection500Error1](content)
            case _:
                return RawError(status_code, content)


list_claims_error_mapper: Final[ErrorMapper[ListClaimsErrorBody]] = _ListClaimsError()

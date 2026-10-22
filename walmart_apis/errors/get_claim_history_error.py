from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_claims_shipment_protection_claim_history400_error1 import (
    V3ClaimsShipmentProtectionClaimHistory400Error1,
)
from ..models.v3_claims_shipment_protection_claim_history404_error1 import (
    V3ClaimsShipmentProtectionClaimHistory404Error1,
)
from ..models.v3_claims_shipment_protection_claim_history500_error1 import (
    V3ClaimsShipmentProtectionClaimHistory500Error1,
)

GetClaimHistoryErrorBody: TypeAlias = (
    V3ClaimsShipmentProtectionClaimHistory400Error1
    | V3ClaimsShipmentProtectionClaimHistory404Error1
    | V3ClaimsShipmentProtectionClaimHistory500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetClaimHistoryError:
    def map(self, status_code: int, content: bytes) -> GetClaimHistoryErrorBody:
        match status_code:
            case 400:
                return decode_json[V3ClaimsShipmentProtectionClaimHistory400Error1](content)
            case 404:
                return decode_json[V3ClaimsShipmentProtectionClaimHistory404Error1](content)
            case 500:
                return decode_json[V3ClaimsShipmentProtectionClaimHistory500Error1](content)
            case _:
                return RawError(status_code, content)


get_claim_history_error_mapper: Final[ErrorMapper[GetClaimHistoryErrorBody]] = _GetClaimHistoryError()

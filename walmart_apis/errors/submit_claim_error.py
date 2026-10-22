from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_claims_shipment_protection_claim400_error1 import V3ClaimsShipmentProtectionClaim400Error1
from ..models.v3_claims_shipment_protection_claim401_error1 import V3ClaimsShipmentProtectionClaim401Error1
from ..models.v3_claims_shipment_protection_claim500_error1 import V3ClaimsShipmentProtectionClaim500Error1

SubmitClaimErrorBody: TypeAlias = (
    V3ClaimsShipmentProtectionClaim400Error1
    | V3ClaimsShipmentProtectionClaim401Error1
    | V3ClaimsShipmentProtectionClaim500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _SubmitClaimError:
    def map(self, status_code: int, content: bytes) -> SubmitClaimErrorBody:
        match status_code:
            case 400:
                return decode_json[V3ClaimsShipmentProtectionClaim400Error1](content)
            case 401:
                return decode_json[V3ClaimsShipmentProtectionClaim401Error1](content)
            case 500:
                return decode_json[V3ClaimsShipmentProtectionClaim500Error1](content)
            case _:
                return RawError(status_code, content)


submit_claim_error_mapper: Final[ErrorMapper[SubmitClaimErrorBody]] = _SubmitClaimError()

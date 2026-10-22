from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_claims_shipment_protection_claim400_error1 import V3ClaimsShipmentProtectionClaim400Error1
from ..models.v3_claims_shipment_protection_claim404_error1 import V3ClaimsShipmentProtectionClaim404Error1
from ..models.v3_claims_shipment_protection_claim500_error1 import V3ClaimsShipmentProtectionClaim500Error1

GetClaimDetailsErrorBody: TypeAlias = (
    V3ClaimsShipmentProtectionClaim400Error1
    | V3ClaimsShipmentProtectionClaim404Error1
    | V3ClaimsShipmentProtectionClaim500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetClaimDetailsError:
    def map(self, status_code: int, content: bytes) -> GetClaimDetailsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3ClaimsShipmentProtectionClaim400Error1](content)
            case 404:
                return decode_json[V3ClaimsShipmentProtectionClaim404Error1](content)
            case 500:
                return decode_json[V3ClaimsShipmentProtectionClaim500Error1](content)
            case _:
                return RawError(status_code, content)


get_claim_details_error_mapper: Final[ErrorMapper[GetClaimDetailsErrorBody]] = _GetClaimDetailsError()

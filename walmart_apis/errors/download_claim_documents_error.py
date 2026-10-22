from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_claims_shipment_protection_claim_documents400_error1 import (
    V3ClaimsShipmentProtectionClaimDocuments400Error1,
)
from ..models.v3_claims_shipment_protection_claim_documents404_error1 import (
    V3ClaimsShipmentProtectionClaimDocuments404Error1,
)
from ..models.v3_claims_shipment_protection_claim_documents500_error1 import (
    V3ClaimsShipmentProtectionClaimDocuments500Error1,
)

DownloadClaimDocumentsErrorBody: TypeAlias = (
    V3ClaimsShipmentProtectionClaimDocuments400Error1
    | V3ClaimsShipmentProtectionClaimDocuments404Error1
    | V3ClaimsShipmentProtectionClaimDocuments500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _DownloadClaimDocumentsError:
    def map(self, status_code: int, content: bytes) -> DownloadClaimDocumentsErrorBody:
        match status_code:
            case 400:
                return decode_json[V3ClaimsShipmentProtectionClaimDocuments400Error1](content)
            case 404:
                return decode_json[V3ClaimsShipmentProtectionClaimDocuments404Error1](content)
            case 500:
                return decode_json[V3ClaimsShipmentProtectionClaimDocuments500Error1](content)
            case _:
                return RawError(status_code, content)


download_claim_documents_error_mapper: Final[
    ErrorMapper[DownloadClaimDocumentsErrorBody]
] = _DownloadClaimDocumentsError()

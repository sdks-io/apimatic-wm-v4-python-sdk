from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetReconReportV1ErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetReconReportV1Error:
    def map(self, status_code: int, content: bytes) -> GetReconReportV1ErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_recon_report_v1_error_mapper: Final[ErrorMapper[GetReconReportV1ErrorBody]] = _GetReconReportV1Error()

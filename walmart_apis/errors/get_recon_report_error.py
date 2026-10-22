from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetReconReportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetReconReportError:
    def map(self, status_code: int, content: bytes) -> GetReconReportErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_recon_report_error_mapper: Final[ErrorMapper[GetReconReportErrorBody]] = _GetReconReportError()

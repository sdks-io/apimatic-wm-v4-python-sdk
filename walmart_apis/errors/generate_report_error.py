from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GenerateReportErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GenerateReportError:
    def map(self, status_code: int, content: bytes) -> GenerateReportErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


generate_report_error_mapper: Final[ErrorMapper[GenerateReportErrorBody]] = _GenerateReportError()

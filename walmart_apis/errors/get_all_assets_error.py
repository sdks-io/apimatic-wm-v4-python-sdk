from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetAllAssetsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetAllAssetsError:
    def map(self, status_code: int, content: bytes) -> GetAllAssetsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_all_assets_error_mapper: Final[ErrorMapper[GetAllAssetsErrorBody]] = _GetAllAssetsError()

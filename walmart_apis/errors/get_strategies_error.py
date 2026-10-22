from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_token400_error1 import V3Token400Error1

GetStrategiesErrorBody: TypeAlias = V3Token400Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetStrategiesError:
    def map(self, status_code: int, content: bytes) -> GetStrategiesErrorBody:
        match status_code:
            case 403 | 500:
                return decode_json[V3Token400Error1](content)
            case _:
                return RawError(status_code, content)


get_strategies_error_mapper: Final[ErrorMapper[GetStrategiesErrorBody]] = _GetStrategiesError()

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_lagtime400_error1 import V3Lagtime400Error1
from ..models.v3_lagtime404_error1 import V3Lagtime404Error1
from ..models.v3_lagtime500_error1 import V3Lagtime500Error1

GetLagTimeErrorBody: TypeAlias = V3Lagtime400Error1 | V3Lagtime404Error1 | V3Lagtime500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetLagTimeError:
    def map(self, status_code: int, content: bytes) -> GetLagTimeErrorBody:
        match status_code:
            case 400:
                return decode_json[V3Lagtime400Error1](content)
            case 404:
                return decode_json[V3Lagtime404Error1](content)
            case 500:
                return decode_json[V3Lagtime500Error1](content)
            case _:
                return RawError(status_code, content)


get_lag_time_error_mapper: Final[ErrorMapper[GetLagTimeErrorBody]] = _GetLagTimeError()

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_repricer_strategy400_error1 import V3RepricerStrategy400Error1
from ..models.v3_token400_error1 import V3Token400Error1

UpdateStrategyErrorBody: TypeAlias = V3RepricerStrategy400Error1 | V3Token400Error1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateStrategyError:
    def map(self, status_code: int, content: bytes) -> UpdateStrategyErrorBody:
        match status_code:
            case 400:
                return decode_json[V3RepricerStrategy400Error1](content)
            case 403 | 500:
                return decode_json[V3Token400Error1](content)
            case _:
                return RawError(status_code, content)


update_strategy_error_mapper: Final[ErrorMapper[UpdateStrategyErrorBody]] = _UpdateStrategyError()

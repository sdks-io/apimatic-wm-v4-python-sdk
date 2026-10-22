from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_shipping_labels500_error1 import V3ShippingLabels500Error1

CreateLabelErrorBody: TypeAlias = V3ShippingLabels500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateLabelError:
    def map(self, status_code: int, content: bytes) -> CreateLabelErrorBody:
        match status_code:
            case 500:
                return decode_json[V3ShippingLabels500Error1](content)
            case _:
                return RawError(status_code, content)


create_label_error_mapper: Final[ErrorMapper[CreateLabelErrorBody]] = _CreateLabelError()

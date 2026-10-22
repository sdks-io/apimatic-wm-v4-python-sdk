from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_shipping_labels_carriers_trackings400_error1 import V3ShippingLabelsCarriersTrackings400Error1

DiscardLabelErrorBody: TypeAlias = list[V3ShippingLabelsCarriersTrackings400Error1] | RawError


@dataclass(frozen=True, slots=True)
class _DiscardLabelError:
    def map(self, status_code: int, content: bytes) -> DiscardLabelErrorBody:
        match status_code:
            case 400:
                return decode_json[list[V3ShippingLabelsCarriersTrackings400Error1]](content)
            case _:
                return RawError(status_code, content)


discard_label_error_mapper: Final[ErrorMapper[DiscardLabelErrorBody]] = _DiscardLabelError()

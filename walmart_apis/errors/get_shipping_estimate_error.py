from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_shipping_labels_shipping_estimates400_error1 import V3ShippingLabelsShippingEstimates400Error1

GetShippingEstimateErrorBody: TypeAlias = list[V3ShippingLabelsShippingEstimates400Error1] | RawError


@dataclass(frozen=True, slots=True)
class _GetShippingEstimateError:
    def map(self, status_code: int, content: bytes) -> GetShippingEstimateErrorBody:
        match status_code:
            case 400:
                return decode_json[list[V3ShippingLabelsShippingEstimates400Error1]](content)
            case _:
                return RawError(status_code, content)


get_shipping_estimate_error_mapper: Final[ErrorMapper[GetShippingEstimateErrorBody]] = _GetShippingEstimateError()

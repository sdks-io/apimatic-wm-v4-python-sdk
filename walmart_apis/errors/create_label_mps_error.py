from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error5 import Error5
from ..models.v3_shipping_multi_package_labels500_error1 import V3ShippingMultiPackageLabels500Error1

CreateLabelMpsErrorBody: TypeAlias = list[Error5] | V3ShippingMultiPackageLabels500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateLabelMpsError:
    def map(self, status_code: int, content: bytes) -> CreateLabelMpsErrorBody:
        match status_code:
            case 400:
                return decode_json[list[Error5]](content)
            case 500:
                return decode_json[V3ShippingMultiPackageLabels500Error1](content)
            case _:
                return RawError(status_code, content)


create_label_mps_error_mapper: Final[ErrorMapper[CreateLabelMpsErrorBody]] = _CreateLabelMpsError()

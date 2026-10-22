from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v1_settings_gettaxformprofile400_error1 import V1SettingsGettaxformprofile400Error1
from ..models.v1_settings_gettaxformprofile404_error1 import V1SettingsGettaxformprofile404Error1
from ..models.v1_settings_gettaxformprofile500_error1 import V1SettingsGettaxformprofile500Error1

GetTaxFormsErrorBody: TypeAlias = (
    V1SettingsGettaxformprofile400Error1
    | V1SettingsGettaxformprofile404Error1
    | V1SettingsGettaxformprofile500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _GetTaxFormsError:
    def map(self, status_code: int, content: bytes) -> GetTaxFormsErrorBody:
        match status_code:
            case 400:
                return decode_json[V1SettingsGettaxformprofile400Error1](content)
            case 404:
                return decode_json[V1SettingsGettaxformprofile404Error1](content)
            case 500:
                return decode_json[V1SettingsGettaxformprofile500Error1](content)
            case _:
                return RawError(status_code, content)


get_tax_forms_error_mapper: Final[ErrorMapper[GetTaxFormsErrorBody]] = _GetTaxFormsError()

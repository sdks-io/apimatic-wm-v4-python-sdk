from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.v3_insights_items_unpublished_counts500_error1 import V3InsightsItemsUnpublishedCounts500Error1
from ..models.v3_token400_error1 import V3Token400Error1

GetUnpublishedItemCountErrorBody: TypeAlias = V3Token400Error1 | V3InsightsItemsUnpublishedCounts500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetUnpublishedItemCountError:
    def map(self, status_code: int, content: bytes) -> GetUnpublishedItemCountErrorBody:
        match status_code:
            case 401 | 403:
                return decode_json[V3Token400Error1](content)
            case 500:
                return decode_json[V3InsightsItemsUnpublishedCounts500Error1](content)
            case _:
                return RawError(status_code, content)


get_unpublished_item_count_error_mapper: Final[
    ErrorMapper[GetUnpublishedItemCountErrorBody]
] = _GetUnpublishedItemCountError()

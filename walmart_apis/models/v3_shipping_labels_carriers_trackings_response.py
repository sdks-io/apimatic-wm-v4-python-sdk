from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V3ShippingLabelsCarriersTrackingsResponse(SdkBaseModel):
    data: Optional[bool] = UNSET
    """Returns ``true`` if the label was successfully discarded.

    <b style="color: green;">Market availability: US | CA | MX</b>"""


class V3ShippingLabelsCarriersTrackingsResponseDict(TypedDict):
    data: NotRequired[bool]

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdditionalAttribute4(SdkBaseModel):
    name: str
    """<br><b style='color:green;'>Market availability: Global</b>"""

    value: str
    """<br><b style='color:green;'>Market availability: Global</b>"""


class AdditionalAttribute4Dict(TypedDict):
    name: str
    value: str

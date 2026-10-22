from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .additional_attribute4 import AdditionalAttribute4, AdditionalAttribute4Dict


class AdditionalAttributes3(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: Global</b>"""

    additional_attribute: list[AdditionalAttribute4] = Field(alias="additionalAttribute")
    """<br><b style='color:green;'>Market availability: Global</b>"""


class AdditionalAttributes3Dict(TypedDict):
    additional_attribute: list[AdditionalAttribute4Dict]

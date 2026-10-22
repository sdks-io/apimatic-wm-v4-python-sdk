from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .box_dimensions4 import BoxDimensions4, BoxDimensions4Dict


class PackageDimension(SdkBaseModel):
    """Package Dimensions"""

    package_type: str = Field(alias="packageType")
    """Package Type. Supported Package Types are - 'CUSTOM_PACKAGE', 'FEDEX_ENVELOPE', 'FEDEX_PAK'<br/><b>Applicable to
    SWW and WPS.</span></b>"""

    box_dimensions: BoxDimensions4 = Field(alias="boxDimensions")
    """Box Dimensions"""


class PackageDimensionDict(TypedDict):
    package_type: str
    box_dimensions: BoxDimensions4Dict

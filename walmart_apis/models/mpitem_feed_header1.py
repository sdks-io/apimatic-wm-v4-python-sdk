from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.locale1 import Locale1, Locale1Dict


class MpitemFeedHeader1(SdkBaseModel):
    """<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    mart: str
    """The mart ID for the various markets are WALMART_CA for CA, WALMART_MEXICO for MX, and WALMART_CHILE for
    CL..<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    locale: Locale1
    """The market specific locale. Allowed values by market include: es for MX and CL, and en and fr for CA.<br><b
    style='color:green;'>Market availability: Global</b>"""

    version: str
    """The feed schema version. The values is 5.0.20250801-18_47_55-api for CA, MX and CL.<br><b
    style='color:green;'>Market availability: CA | MX | CL</b>"""

    business_unit: str = Field(alias="businessUnit")
    """Business unit identifier matching the target market. For example WALMART_CA for CA, WALMART_MEXICO for MX,
    WALMART_CHILE for CL.<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""

    tenant: str
    """The tenant identifier for the marketplace. For example, use WALMART_CA for CA, WALMART_MEXICO for MX,
    WALMART_CHILE for CL.<br><b style='color:green;'>Market availability: CA | MX | CL</b>"""


class MpitemFeedHeader1Dict(TypedDict):
    mart: str
    locale: Locale1Dict
    version: str
    business_unit: str
    tenant: str

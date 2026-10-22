from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .node10 import Node10, Node10Dict


class Inventories3(SdkBaseModel):
    """<strong style="color: green;">Market availability: Global</strong>"""

    nodes: list[Node10]


class Inventories3Dict(TypedDict):
    nodes: list[Node10Dict]

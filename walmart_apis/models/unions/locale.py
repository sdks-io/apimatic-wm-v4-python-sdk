from __future__ import annotations

from typing import TypeAlias

Locale: TypeAlias = str | list[str]
"""The market specific locale. Allowed values by market include: en for US, es for MX and CL, and en and fr for
CA.<br><b style='color:green;'>Market availability: Global</b>"""

LocaleDict: TypeAlias = str | list[str]

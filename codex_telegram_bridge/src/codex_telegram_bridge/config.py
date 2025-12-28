from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from .constants import TELEGRAM_CONFIG_PATH


def load_telegram_config(path: str | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else TELEGRAM_CONFIG_PATH
    return tomllib.loads(cfg_path.read_text(encoding="utf-8"))

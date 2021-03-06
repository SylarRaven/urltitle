from typing import Optional

from humanize import naturalsize


def _humanize_bytes(num_bytes: int) -> str:
    return naturalsize(num_bytes, gnu=True, format='%.0f')


def humanize_bytes(num_bytes: Optional[int]) -> Optional[str]:
    return _humanize_bytes(num_bytes) if num_bytes is not None else None


def humanize_len(text: bytes) -> str:
    return _humanize_bytes(len(text))

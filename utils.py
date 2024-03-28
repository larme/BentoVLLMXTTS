from __future__ import annotations

import os
import hashlib

def _hash_str(s: str) -> str:
    h = hashlib.new("sha256")
    h.update(s.encode())
    return h.hexdigest()


def text2path(text: str) -> str:
    hashed = _hash_str(text)
    dirs = ["audio", hashed[:2], hashed[2:4]]
    output_fn = hashed[4:] + ".wav"
    output_dir = os.path.join(*dirs)
    output_path = os.path.join(output_dir, output_fn)
    return output_path

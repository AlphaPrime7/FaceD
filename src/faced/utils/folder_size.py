from __future__ import absolute_import

from pathlib import Path

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)

def get_folder_size(folder):
    return sizeof_fmt(sum(f.stat().st_size for f in Path(folder).rglob("*")))

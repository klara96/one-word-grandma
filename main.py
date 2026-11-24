"""Write the one-word-grandma entry to an output file.

The entry text is exactly: <<<robuts>>>
It is written to /output/entry.txt (UTF-8). If /output does not exist, it is created.
The output directory can be overridden via the MAKEFUN_OUTPUT_DIR environment variable.
"""
import os
from pathlib import Path

ENTRY = "<<<robuts>>>"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_dir.joinpath("entry.txt").write_text(ENTRY, encoding="utf-8")

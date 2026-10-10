from pathlib import Path
import re
import urllib.request

src = Path("slinger-transfer.md").read_text(encoding="utf-8")
pairs = re.findall(r"\[([^\]]+)\]\((https://[^)]+\.mp4)\)", src)
out = Path("slinger-openart")
out.mkdir(exist_ok=True)

for i, (label, url) in enumerate(pairs, 1):
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", label).strip("_")
    target = out / f"{i:02d}_{safe}.mp4"
    print(f"Downloading {label} -> {target}")
    urllib.request.urlretrieve(url, target)

if len(pairs) != 8:
    raise SystemExit(f"Expected 8 clips, found {len(pairs)}")

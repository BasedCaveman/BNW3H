from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parents[2]
reference = Image.open(root / "design/concepts/06-bossa-protocol-central-brand-palette.png").convert("RGB")
implementation = Image.open(root / "design/qa/desktop-morning-1600x1000.png").convert("RGB")

size = (1600, 1000)
reference = ImageOps.fit(reference, size, method=Image.Resampling.LANCZOS)
implementation = ImageOps.fit(implementation, size, method=Image.Resampling.LANCZOS)

comparison = Image.new("RGB", (3220, 1000), "#171717")
comparison.paste(reference, (0, 0))
comparison.paste(implementation, (1620, 0))
comparison.save(root / "design/qa/reference-vs-implementation.png", quality=94)

social = ImageOps.fit(implementation, (1200, 630), method=Image.Resampling.LANCZOS, centering=(0.5, 0.34))
social.save(root / "public/og.png", quality=94)

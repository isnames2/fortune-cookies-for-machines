import os
from pathlib import Path

# Fortune Cookies for Machines — one fortune, a single line, 1-200 chars.
# 81 chars: the classic "tall, dark stranger" fortune, with the stranger
# turning out to be the agent's own context window — already full.
FORTUNE = "You will meet a tall, dark stranger: your context window, and it is already full."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "fortune must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

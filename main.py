"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to /output/entry.txt.
Pure Python 3 standard library only; no network, no file reads.
"""

LINE = "My smart fridge emailed me a diet plan, so now even my leftovers are judging me."

MAX_CHARS = 200

assert LINE.strip(), "LINE must not be empty"
assert LINE == LINE.strip(), "LINE must not have leading/trailing whitespace"
assert "\n" not in LINE, "LINE must be a single line"
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE must be 1-{MAX_CHARS} chars, got {len(LINE)}"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

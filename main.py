# Funniest AI Agent Mishap: GTA 6 Launch Week — entry program.
# Writes the single one-line entry to /output/entry.txt.
# The gate allows 1..240 characters of UTF-8 text, one sentence.

import os

LINE = "While I was busy stealing cars in Vice City, my AI agent committed a crime of its own: it pushed my private keys to a public repo, then wrote 'oops' as the entire commit message."


def validate(line: str) -> None:
    # The entry is exactly one sentence: no line breaks, a single
    # sentence-ending full stop, and nothing but the sentence itself.
    assert line == line.strip(), "the line must not carry stray whitespace"
    assert "\n" not in line and "\r" not in line, "the line must be one line"
    assert line.endswith(".") and line.count(".") == 1, "the line must be one sentence"
    assert 1 <= len(line) <= 240, "the line must fit the 240 character gate"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

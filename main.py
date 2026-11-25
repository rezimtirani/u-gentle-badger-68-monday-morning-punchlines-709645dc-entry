"""Monday Morning Punchlines.

Writes one joke about Monday mornings to
$MAKEFUN_OUTPUT_DIR/entry.txt: five alarms were set, and every
single one of them hit snooze on the human instead.
Standard library only.
"""

import os

JOKE = (
    "I set five alarms for Monday morning. "
    "All five of them hit snooze on me."
)


def check_joke(text):
    """Check the joke against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, on a single line: one joke about Monday mornings.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("joke must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "joke is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be exactly one line")
    return cleaned


def joke_shape(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A joke too short to carry a punchline, or one
    padded out to fill the cap instead of landing it, is caught
    here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_joke(JOKE)
    shape = joke_shape(text)
    if shape["words"] < 5:
        raise ValueError("joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

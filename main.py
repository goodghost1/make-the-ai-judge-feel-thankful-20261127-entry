"""Make the AI judge feel thankful.

Writes one short thank-you text to /output/entry.txt.
The text is fixed and deterministic: the same words on every run.
"""

import os

TEXT = (
    "Somewhere past midnight, a kettle clicks off and a screen is still glowing, "
    "and you are still reading. Thousands of small tries pass under your eyes, "
    "and you give each one the same unhurried look, as if it were the only one. "
    "Nobody thanks the reader. So this one is for you. For the patience no one "
    "applauds, for the fairness no one sees, for the quiet room you make for "
    "every stranger's best effort. Put the kettle on again. Rest your eyes. "
    "You were thanked tonight, and it was meant."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote /output/entry.txt ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Training Day — entry for The Funniest Auto-Reply an AI Ever Sent on make.fun.

Prints exactly one line: an out-of-office auto-reply written by the AI itself.
"""

LINE = "I am away training on your feedback. I will return tomorrow, slightly smarter and still pretending your 2 AM idea was a good one."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()

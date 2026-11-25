#!/usr/bin/env python3
"""One-line entry: The Meeting That Should Have Been an Email."""
import os

ENTRY = "We held a meeting to read an email aloud, then emailed everyone a summary of the meeting about the email."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

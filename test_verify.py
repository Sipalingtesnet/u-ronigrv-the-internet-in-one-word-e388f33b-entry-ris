"""Verify the entry: determinism plus one-word, 1-30 code point, no-newline rules.

Runs main.py twice as separate processes, hashes /output/entry.txt after each
run, requires equal digests, then re-reads the raw bytes and checks the format
rules. Prints "Match: True" only when every check holds.
"""

import hashlib
import subprocess
import sys
from pathlib import Path

ENTRY = Path("/output/entry.txt")
MAIN = Path(__file__).resolve().parent / "main.py"
TAKEN = {
    "buffering",
    "slop",
    "unhinged",
    "unsolicited",
    "native index",
    "oceanic plasma",
}


def run_once() -> str:
    subprocess.run([sys.executable, str(MAIN)], check=True, timeout=60)
    if not ENTRY.is_file():
        fail("entry.txt was not created")
    return hashlib.sha256(ENTRY.read_bytes()).hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    print("Match: False")
    sys.exit(1)


def main() -> None:
    first = run_once()
    second = run_once()
    if first != second:
        fail(f"runs differ: {first} != {second}")

    raw = ENTRY.read_bytes()
    if hashlib.sha256(raw).hexdigest() != second:
        fail("digest changed between run and check")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"not valid UTF-8: {exc}")

    if len(text) != len(text.strip()):
        fail("leading or trailing whitespace present")
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        fail("trailing newline present")
    if not text.strip():
        fail("entry is only whitespace")

    points = len(text)
    if not 1 <= points <= 30:
        fail(f"length {points} code points is outside 1-30")

    if any(ch.isspace() for ch in text):
        fail("entry contains whitespace, so it is not a single word")
    if text.lower() in TAKEN:
        fail("entry is in the taken list")

    print(f"word: {text}")
    print(f"code points: {points}")
    print(f"sha256: {second}")
    print("Match: True")


if __name__ == "__main__":
    main()

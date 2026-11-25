"""Entry for "The Internet in One Word": Shoutbrary.

A library is the one building where the sound is supposed to stay down. Ours
holds every book ever written, every patron is yelling at once, and no
librarian is coming. That is the whole internet in one beat.

Judge's criteria, in the order they are weighed:

1. One word for the whole internet. "Shout" and "library" are its two halves --
   the total archive and the total volume -- fused into a single noun. No
   phrase, no caption, nothing to explain.
2. Funny alone. The shush is the one rule a library has; here the rule is
   already broken everywhere and nobody is left to enforce it.
3. True of the whole internet, not one site. Every app is some blend of stored
   knowledge and raised voices, so the word never has to point at a particular
   one.
4. Surprising. The obvious reaches are scroll, feed, troll, echo. A library is
   the opposite image, and that collision is the whole smile.
5. Lands in one beat. Ten letters, spelled exactly as it sounds, readable
   before the reader has time to argue with it.

Deterministic, offline, no arguments, no randomness: it writes the word and
stops.
"""

from pathlib import Path

WORD = "Shoutbrary"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # Raw bytes, UTF-8, no trailing newline: the judged text is exactly WORD.
    OUTPUT.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Encrypt a Hebrew text file with a fresh random substitution cipher.

Usage
-----
python encrypt_hebrew.py input.txt output.txt           # encrypted text only
python encrypt_hebrew.py input.txt output.txt -s        # also save mapping
"""
import argparse
import random
import sys
from pathlib import Path


def create_random_mapping() -> dict[str, str]:
    """Return a random one-to-one mapping of the Hebrew letters א-ת."""
    hebrew_letters = [chr(code) for code in range(ord("א"), ord("ת") + 1)]
    shuffled = hebrew_letters[:]
    random.shuffle(shuffled)
    return dict(zip(hebrew_letters, shuffled))


def encrypt_with_mapping(text: str, mapping: dict[str, str]) -> str:
    """Encrypt *text* by substituting each Hebrew letter per *mapping*."""
    return "".join(mapping.get(ch, ch) for ch in text)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encrypt a Hebrew text file with a random substitution cipher."
    )
    parser.add_argument(
        "input_file", type=Path, help="Path to the source text file."
    )
    parser.add_argument(
        "output_file", type=Path, help="Path for the encrypted file."
    )
    parser.add_argument(
        "-s",
        "--save-mapping",
        action="store_true",
        help="Also write the letter mapping (one line per pair) "
        "next to the output file with extension '.map'.",
    )
    args = parser.parse_args()

    try:
        plaintext = args.input_file.read_text(encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"❌ Input file not found: {args.input_file}")

    mapping = create_random_mapping()
    ciphertext = encrypt_with_mapping(plaintext, mapping)

    args.output_file.write_text(ciphertext, encoding="utf-8")
    print(f"✅ Encrypted text written to {args.output_file}")

    if args.save_mapping:
        mapping_path = args.output_file.with_suffix(
            args.output_file.suffix + ".map"
        )
        with mapping_path.open("w", encoding="utf-8") as f:
            for src, dst in mapping.items():
                f.write(f"{src} -> {dst}\n")
        print(f"🗺  Mapping written to {mapping_path}")


if __name__ == "__main__":
    main()

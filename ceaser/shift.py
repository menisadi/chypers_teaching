import sys
import os


def caesar_cipher_hebrew(text: str, shift: int) -> str:
    """
    Encrypts the given Hebrew text by shifting each letter by the specified number.

    :param text: The input text in Hebrew.
    :param shift: The number to shift each letter.
    :return: The encrypted text.
    """
    hebrew_start = ord("א")
    hebrew_end = ord("ת")

    def shift_letter(letter: str, shift: int) -> str:
        if hebrew_start <= ord(letter) <= hebrew_end:
            new_pos = (ord(letter) - hebrew_start + shift) % (
                hebrew_end - hebrew_start + 1
            )
            return chr(hebrew_start + new_pos)
        return letter  # Non-Hebrew characters remain unchanged

    return "".join(shift_letter(char, shift) for char in text)


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <shift_amount>")
        sys.exit(1)

    input_file = sys.argv[1]
    shift_amount = int(sys.argv[2])
    output_file = f"{os.path.splitext(input_file)[0]}_encrypted{os.path.splitext(input_file)[1]}"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    encrypted_text = caesar_cipher_hebrew(text, shift_amount)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(encrypted_text)
        print(f"Encrypted text written to '{output_file}'")
    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

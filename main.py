def caesar_cipher_hebrew(text, shift):
    """
    Encrypts the given Hebrew text by shifting each letter by the specified number.

    :param text: The input text in Hebrew.
    :param shift: The number to shift each letter.
    :return: The encrypted text.
    """
    # Hebrew letters Unicode range
    hebrew_start = ord("א")
    hebrew_end = ord("ת")

    def shift_letter(letter, shift):
        if hebrew_start <= ord(letter) <= hebrew_end:
            # Calculate the new position with wrap-around
            new_pos = (ord(letter) - hebrew_start + shift) % (
                hebrew_end - hebrew_start + 1
            )
            return chr(hebrew_start + new_pos)
        return letter  # Non-Hebrew characters remain unchanged

    # Apply the shift to each letter in the text
    encrypted_text = "".join(shift_letter(char, shift) for char in text)
    return encrypted_text


# Example usage
if __name__ == "__main__":
    hebrew_text = input("Enter Hebrew text: ")
    shift_amount = int(input("Enter shift amount: "))
    result = caesar_cipher_hebrew(hebrew_text, shift_amount)
    print("Encrypted text:", result)

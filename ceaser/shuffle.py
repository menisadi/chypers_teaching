import random


def create_random_mapping() -> dict[str, str]:
    """
    Creates a random mapping of the Hebrew alphabet to another set of shuffled Hebrew letters.

    :return: A dictionary with the mapping.
    """
    hebrew_letters = [chr(code) for code in range(ord("א"), ord("ת") + 1)]
    shuffled_letters = hebrew_letters[:]
    random.shuffle(shuffled_letters)
    return dict(zip(hebrew_letters, shuffled_letters))


def encrypt_with_mapping(text: str, mapping: dict[str, str]) -> str:
    """
    Encrypts the given Hebrew text using the provided mapping.

    :param text: The input text in Hebrew.
    :param mapping: A dictionary containing the letter-to-letter mapping.
    :return: The encrypted text.
    """
    encrypted_text = "".join(mapping.get(char, char) for char in text)
    return encrypted_text


if __name__ == "__main__":
    hebrew_text = input("Enter Hebrew text: ")

    letter_mapping = create_random_mapping()

    print("Mapping:")
    for original, encrypted in letter_mapping.items():
        print(f"{original} -> {encrypted}")

    encrypted_text = encrypt_with_mapping(hebrew_text, letter_mapping)
    print("\nEncrypted text:", encrypted_text)

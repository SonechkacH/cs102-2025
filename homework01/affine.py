def encrypt_affine(plaintext, a, b):
    """
    Шифрует текст с помощью аффинного шифра.

    Args:
        plaintext (str): исходный текст для шифрования
        a (int): первый ключ шифрования
        b (int): второй ключ шифрования

    Returns:
        str: зашифрованный текст
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)

    encrypted_text = ""

    for char in plaintext:
        if char.lower() in alphabet:

            x = alphabet.index(char.lower())

            encrypted_position = (a * x + b) % m

            encrypted_char = alphabet[encrypted_position]

            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:

            encrypted_text += char

    return encrypted_text

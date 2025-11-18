def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_idx = 0
    key_len = len(keyword)
    for ch in plaintext:
        if "A" <= ch <= "Z":
            pos = ord(ch) - ord("A")
            key_char = keyword[key_idx % key_len]
            shift = ord(key_char) - ord("A")
            new_pos = pos + shift
            new_ch = chr(ord("A") + new_pos % 26)
            ciphertext += new_ch
            key_idx += 1
        elif "a" <= ch <= "z":
            pos = ord(ch) - ord("a")
            key_char = keyword[key_idx % key_len]
            shift = ord(key_char) - ord("a")
            new_pos = pos + shift
            new_ch = chr(ord("a") + new_pos % 26)
            ciphertext += new_ch
            key_idx += 1
        else:
            ciphertext += ch
            key_idx += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_len = len(keyword)
    key_idx = 0
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            pos = ord(ch) - ord("A")
            key_let = keyword[key_idx % key_len]
            shift = ord(key_let) - ord("A")
            new_pos = pos - shift
            new_ch = chr(ord("A") + new_pos % 26)
            plaintext += new_ch
            key_idx += 1
        elif "a" <= ch <= "z":
            pos = ord(ch) - ord("a")
            key_let = keyword[key_idx % key_len]
            shift = ord(key_let) - ord("a")
            new_pos = pos - shift
            new_ch = chr(ord("a") + new_pos % 26)
            plaintext += new_ch
            key_idx += 1
        else:
            plaintext += ch
            key_idx += 1
    return plaintext

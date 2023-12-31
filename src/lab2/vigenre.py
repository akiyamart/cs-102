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
    keyword = keyword.lower()
    key_iteration = 0 

    for letter in plaintext: 
        if not letter.isalpha():
            ciphertext += letter
        else:
            key_eleemnt = keyword[key_iteration % len(keyword)]  # Символ ключевого слова (для повторного использования ключа, если ключ недостаточно длинный)
            key_shift = ord(key_eleemnt) - ord('a') # Сдвиг для текущего символа ключа
            base = ord('a') if letter.islower() else ord('A')
            encrypted_char = chr(((ord(letter) - base + key_shift) % 26) + base) # Позиция симвовола после сдвига 
            ciphertext += encrypted_char
            key_iteration += 1

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
    keyword = keyword.lower()
    key_iteration = 0
    
    for letter in ciphertext:
        if letter.isalpha():
            key_eleemnt = keyword[key_iteration % len(keyword)]
            key_shift = ord(key_eleemnt) - ord('a')
            base = ord('a') if letter.islower() else ord('A')
            decrypted_char = chr(((ord(letter) - base - key_shift) % 26) + base)
            plaintext += decrypted_char
            key_iteration += 1
        else:
            plaintext += letter
    
    return plaintext

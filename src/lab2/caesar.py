def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    word = plaintext
    offset = shift
    ciphertext = ""
    register_word = ""

    for letter in word:     
        if letter.islower(): 
            register_word += "0"       
        else: 
            register_word += "1"

    word = word.lower()
    
    for i in range(len(word)):
        if not word[i].isalpha():
            ciphertext += word[i]
        elif ord(word[i]) + offset > 122: 
            if register_word[i] == "1":
                ciphertext += chr(ord(word[i]) + offset - 26).upper()
            else:
                ciphertext += chr(ord(word[i]) + offset - 26)
        
        else: 
            if register_word[i] == "1":
                ciphertext += chr(ord(word[i]) + offset).upper()
            else:
                ciphertext += chr(ord(word[i]) + offset)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    word = ciphertext
    offset = shift
    register_word = ""
    plaintext = ""

    for letter in word:     
        if letter.islower(): 
            register_word += "0"       
        else: 
            register_word += "1"

    word = word.lower()
    
    for i in range(len(word)):
        if not word[i].isalpha():
            plaintext += word[i] 
        elif ord(word[i]) - offset < 97: 
            if register_word[i] == "1":
                plaintext += chr(ord(word[i]) - offset + 26).upper()
            else:
                plaintext += chr(ord(word[i]) - offset + 26)
        else: 
            if register_word[i] == "1":
                plaintext += chr(ord(word[i]) - offset).upper()
            else:
                plaintext += chr(ord(word[i]) - offset)
    
    return plaintext



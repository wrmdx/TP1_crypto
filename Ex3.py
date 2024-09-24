def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key.upper() if i.isalpha()]
    plain_text_int = [ord(i) - ord('A') for i in plain_text.upper() if i.isalpha()]

    for i in range(len(plain_text_int)):
        value = (plain_text_int[i] + key_as_int[i % key_length]) % 26
        encrypted_text.append(chr(value + ord('A')))
    
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key.upper() if i.isalpha()]
    encrypted_text_int = [ord(i) - ord('A') for i in encrypted_text.upper() if i.isalpha()]

    for i in range(len(encrypted_text_int)):
        value = (encrypted_text_int[i] - key_as_int[i % key_length]) % 26
        decrypted_text.append(chr(value + ord('A')))
    
    return ''.join(decrypted_text)


def letter_frequency_analysis(ciphertext):
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            freq[char] = freq.get(char, 0) + 1
    return freq



key = "ENSAM"
plain_text = "Mardi est un beau jour 10. "


print("Texte original : " , plain_text)
print("Clé : " , key)
encrypted_text = vigenere_encrypt(plain_text, key)

print("Texte chiffré :", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Texte déchiffré :", decrypted_text)


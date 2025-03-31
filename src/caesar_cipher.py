class CaesarCipher:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        result_ciphertext = ""
        for char_plaintext in plaintext:
            encrypted_char = chr((ord(char_plaintext) + self.key) % 1114112)
            result_ciphertext += encrypted_char
        return result_ciphertext
    
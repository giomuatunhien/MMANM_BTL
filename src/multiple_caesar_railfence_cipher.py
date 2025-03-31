from caesar_cipher import CaesarCipher
from rail_fence_cipher import RailFenceCipher

class MultipleCaesarRailFence:
    def __init__(self, caesar_key: int, rails_rail_fence: int):
        self.caesar = CaesarCipher(caesar_key)
        self.rail_fence = RailFenceCipher(rails_rail_fence)

    def encrypt(self, plaintext: str) -> str:
        caesar_encrypted = self.caesar.encrypt(plaintext)
        result_ciphertext = self.rail_fence.encrypt(caesar_encrypted)
        return result_ciphertext
    
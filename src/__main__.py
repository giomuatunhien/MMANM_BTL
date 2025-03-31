from encrypt_decrypt_program import main
import sys

if __name__ == "__main__":
    plaintext_file = "./plaintext.txt"
    plaintext = ""
    with open(plaintext_file, 'r', encoding='utf-8') as f_in:
        plaintext = f_in.read()
    main(plaintext)
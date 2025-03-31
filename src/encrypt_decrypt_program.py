from caesar_cipher import CaesarCipher
from rail_fence_cipher import RailFenceCipher
from multiple_caesar_railfence_cipher import MultipleCaesarRailFence
from Decrypt import Eve
import threading

    
def main(plaintext):
    
    print("------------------------------------------------------------------")
    print("|         CHUONG TRINH MA HOA VA GIAI MA                         |")
    print("------------------------------------------------------------------")
    print("|                                                                |")
    print("|   CHON LENH:                                                   |")
    print("| 1. ENCRYPTION                                                  |")
    print("| 2. DECRYPTION                                                  |")
    print("|                                                                |")
    print("------------------------------------------------------------------")
    option = int(input("|     LUA CHON CUA BAN:                                       | ",))
    print("------------------------------------------------------------------")
    if option == 1:
        print("------------------------------------------------------------------")
        print("|                                                                |")
        print("|      CHON LENH                                                 |")
        print("| 1. CASESAR CIPHER                                              |")
        print("| 2. RAIL FENCE CIPHER                                           |")
        print("| 3. MULTIPLE CAESAR VA RAIL FENCE CIPHER                        |")
        print("|                                                                |")
        print("------------------------------------------------------------------")
        func_value = int(input("|     LUA CHON CUA BAN:                                       | ",))
        if func_value == 1:
            print("------------------------------------------------------------------")
            key = int(input("|   NHAP KHOA DE MA HOA:               ",))
            caesar_obj = CaesarCipher(key)
            text_decrypted = caesar_obj.encrypt(plaintext)
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------GHI FILE THANH CONG-----------           |")
            print("|                                                                |")
            print("------------------------------------------------------------------")
            with open('./cipher/ciphertext.txt', 'w', encoding='utf-8') as f_out:
                f_out.write(text_decrypted)
        elif func_value == 2:
            print("------------------------------------------------------------------")
            rails = int(input("|   NHAP KHOA DE MA HOA:               ",))
            railfence_obj = RailFenceCipher(rails)
            print("------------------------------------------------------------------")
            text_decrypted = railfence_obj.encrypt(plaintext)
            with open('./cipher/ciphertext.txt', 'w', encoding='utf-8') as f_out:
                f_out.write(text_decrypted)
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------GHI FILE THANH CONG-----------           |")
            print("|                                                                |")
            print("------------------------------------------------------------------")
        elif func_value == 3:
            print("------------------------------------------------------------------")
            key = int(input("|   ENTER YOUR KEY FOR CAESAR ENCRYPTION: ",))
            rails = int(input("|   ENTER YOUR RAILS FOR RAILFENCE ENCRYPTION: ",))
            print("------------------------------------------------------------------")
            multiple_obj = MultipleCaesarRailFence(key, rails)
            text_decrypted = multiple_obj.encrypt(plaintext)
            with open('./cipher/ciphertext.txt', 'w', encoding='utf-8') as f_out:
                f_out.write(text_decrypted)
            print("------------------------------------------------------------------")
            print("|                                                                |")
            print("|           ------------GHI FILE THANH CONG-----------           |")
            print("|                                                                |")
            print("------------------------------------------------------------------")   
            
    elif option == 2:
        hacker = Eve()
        input_file = './cipher/ciphertext.txt'
        ciphers_and_files = [
            (input_file, './output/result_1.txt', hacker.decrypt_caesar),
            (input_file, './output/result_2.txt', hacker.decryptRailFence),
            (input_file, './output/result_3.txt', hacker.decryptMultiple),
        ]

        threads = []
        for file_input, file_output, decrypt in ciphers_and_files:
            thread = threading.Thread(target=decrypt, args=(file_input, file_output, ))
            #thread = threading.Thread(target=decrypt, kwargs={'file_input': file_input, 'file_output': file_output})
            threads.append(thread)
            thread.start() 

        for thread in threads:
            thread.join()

        print('Tất cả các phép tính đã hoàn thành!')
    #  run_caesar_cipher(plaintext, key=3)
    #  run_rail_fence_cipher(plaintext, rails=5)
    #  run_multiple_caesar_railfence_cipher(plaintext, caesar_key=3, rails_rail_fence=5)
    
    
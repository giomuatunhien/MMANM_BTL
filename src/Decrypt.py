import threading
import time
from collections import Counter

class Eve:
    # Hàm tính toán
    def __init__(self):
        self.valid_chars = {' ', '.', ',', '?', ':', '!', ';', '"', '(', ')', "'", '_', '@', '#', '$', '+', '-', '=', '*', '/', '%', '\n'}
    
    def condition(self, c:chr):
        return c.isalpha() or c.isdigit() or c in self.valid_chars

    def decrypt_caesar_help(self, ciphertext):
        english_frequency = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
        
        counter = Counter(ciphertext) 

        max_frequency = max(counter.values())
        
        highest_frequency_chars = [char for char, freq in counter.items() if freq == max_frequency]
        processed_keys = set()
        results = []
        decrypted = ""
        for i in (english_frequency):
            for j in highest_frequency_chars:
                decrypted = ""
                key = (ord(j) - ord(i)) % 0x110000
                flag = True
                char = 0
                while char < len(ciphertext):
                    new_char_1 = chr((ord(ciphertext[char]) - key) % 0x110000)
                    if not (self.condition(new_char_1)):
                        new_char_2 = chr((ord(new_char_1)+32) % 0x110000)
                        new_char_3 = chr((ord(new_char_1)-32) % 0x110000)
                        if (self.condition(new_char_2) and flag):
                            flag = False
                            key = (key - 32) % 0x110000
                            char = 0
                        elif (self.condition(new_char_3) and flag):
                            flag = False
                            key = (key + 32) % 0x110000
                            char = 0
                        else: break
                        decrypted=""
                    else:
                        decrypted+=new_char_1
                        char += 1
                if(len(decrypted)==len(ciphertext)):
                    if key not in processed_keys:
                        processed_keys.add(key)  # Đánh dấu key đã xử lý
                        results.append((key, decrypted))
        return results
        

    def decryptRailFence_help(self, ciphertext, file_output, keyofCaesar):
        with open(file_output, 'w', encoding='utf-8') as f_out:
            for key in range(2, len(ciphertext)):
                rail = [['\n' for i in range(len(ciphertext))] for j in range(key)]
            
                dir_down = None
                row, col = 0, 0
            
                for i in range(len(ciphertext)):
                    if row == 0:
                        dir_down = True
                    if row == key - 1:
                        dir_down = False
                    
                    rail[row][col] = '\0'
                    col += 1
                    
                    if dir_down:
                        row += 1
                    else:
                        row -= 1
                        
                index = 0
                for i in range(key):
                    for j in range(len(ciphertext)):
                        if ((rail[i][j] == '\0') and
                        (index < len(ciphertext))):
                            rail[i][j] = ciphertext[index]
                            index += 1
                    
                result = []
                row, col = 0, 0
                for i in range(len(ciphertext)):
                    
                    if row == 0:
                        dir_down = True
                    if row == key-1:
                        dir_down = False
                        
                    if (rail[row][col] != '\0'):
                        result.append(rail[row][col])
                        col += 1
                        
                    if dir_down:
                        row += 1
                    else:
                        row -= 1
                if(keyofCaesar!=-1):
                    f_out.write(f'rail: {key}; key: {keyofCaesar}; Result: {"".join(result)}\n')
                else:
                    #print(result)
                    f_out.write(f' rail: {key}; Result: {"".join(result)}\n')
        print(f'Ghi kết quả vào {file_output} thành công!')

    def decrypt_caesar(self, file_input, file_output):
        start_time = time.time()
        with open(file_input, 'r', encoding='utf-8') as f_in:
            ciphertext = f_in.read()
        results = self.decrypt_caesar_help(ciphertext)
        with open(file_output, 'w', encoding='utf-8') as f_out:
            for key, decrypted in results:
                f_out.writelines(f"Key: {key}, Decrypted: \"{decrypted}\"")
        end_time = time.time()  # Ghi lại thời gian kết thúc
        elapsed_time = end_time - start_time  # Tính thời gian chạy
        print(f"Thời gian chạy: {elapsed_time:.6f} giây")
        print(f'Ghi kết quả vào {file_output} thành công!')
        
    def decryptRailFence(self, file_input, file_output):
        start_time = time.time()
        with open(file_input, 'r', encoding='utf-8') as f_in:
            ciphertext = f_in.read()
        self.decryptRailFence_help(ciphertext, file_output, -1)
        end_time = time.time()  # Ghi lại thời gian kết thúc
        elapsed_time = end_time - start_time  # Tính thời gian chạy
        print(f"Thời gian chạy: {elapsed_time:.6f} giây")

    def decryptMultiple(self, file_input, file_output):
        start_time = time.time()
        with open(file_input, 'r', encoding='utf-8') as f_in:
            ciphertext = f_in.read()
        results=self.decrypt_caesar_help(ciphertext)
        for key, decrypted in results:
            self.decryptRailFence_help(decrypted, file_output, key)
        end_time = time.time()  # Ghi lại thời gian kết thúc
        elapsed_time = end_time - start_time  # Tính thời gian chạy
        print(f"Thời gian chạy: {elapsed_time:.6f} giây")


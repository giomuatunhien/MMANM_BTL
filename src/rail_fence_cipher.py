class RailFenceCipher:
    def __init__(self, rails: int):
        self.rails = rails
    def encrypt(self, plaintext: str) -> str:
        # Declaration variable:
        # direction=1: go down, direction=-1: go up
        result_ciphertext = ""
        length_matrix = len(plaintext)
        num_rails = self.rails
        matrix_cipher = [["" for _ in range(length_matrix)] for _ in range(num_rails)]
        direction = -1
        row=0
        col=0
        
        # Hiện thực
        # Ghi vào ma trận
        for i in range(length_matrix):
            matrix_cipher[row][col] = plaintext[i]
            if row==0 or row==num_rails-1:
                 direction *= -1
            row += direction
            col += 1
        
        # Đọc ma trận
        for i in range(num_rails):
            for j in range(length_matrix):
                if matrix_cipher[i][j] != '':
                    result_ciphertext += matrix_cipher[i][j]
                    
        return result_ciphertext
    
    
    
class PlayFairCipher:
    def __init__(self) -> None:
        pass
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set()
        matrix = []
        
        # Thêm các chữ cái trong key vào ma trận
        for letter in key:
            if letter not in key_set:
                matrix.append(letter)
                key_set.add(letter)

        # Thêm các chữ cái còn lại của bảng chữ cái
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)

        # Chia thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
    
    def prepare_text(self, text):
        text = text.replace("J", "I").upper()
        prepared_text = ""

        i = 0
        while i < len(text):
            if i == len(text) - 1:  # Nếu ký tự cuối cùng lẻ, thêm 'X'
                prepared_text += text[i] + "X"
                break
            if text[i] == text[i + 1]:  # Nếu có 2 ký tự trùng, chèn 'X' giữa
                prepared_text += text[i] + "X"
                i += 1
            else:
                prepared_text += text[i] + text[i + 1]
                i += 2

        return prepared_text

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.prepare_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
            else:  # Thành hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        decrypted_text = ""
        cipher_text = cipher_text.upper()

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
            else:  # Thành hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        banro = ""
        i = 0
        while i < len(decrypted_text):
            if i < len(decrypted_text) - 1 and decrypted_text[i+1] == 'X':
                # Nếu 'X' được chèn giữa hai ký tự giống nhau, bỏ 'X'
                if i+2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i+2]:
                    banro += decrypted_text[i]
                    i += 2  # Bỏ qua 'X'
                else:
                    banro += decrypted_text[i] + decrypted_text[i+1]
                    i += 2
            else:
                banro += decrypted_text[i]
                i += 1

        return banro
            
            

    
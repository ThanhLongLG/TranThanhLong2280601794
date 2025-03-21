class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """ Mã hóa bằng hoán vị cột """
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        """ Giải mã bằng hoán vị cột """
        num_cols = int(len(text) / key)  # Số cột (hàng trong bảng)
        num_rows = key  # Số hàng (số lượng khóa)
        num_shaded_boxes = (num_cols * num_rows) - len(text)  # Ô thừa cần bỏ qua

        decrypted_text = [''] * num_cols  # Khởi tạo mảng rỗng với số cột
        col, row = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1

            # Nếu đến cột cuối cùng hoặc gặp ô thừa, nhảy xuống dòng
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(decrypted_text)



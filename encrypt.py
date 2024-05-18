class Encrypt:
    def bit_xor(self, a, b):
        result = 0
        for i in range(8):
            x = (a % 2 == 1) and 1 or 0
            y = (b % 2 == 1) and 1 or 0
            if (x + y) % 2 == 1:
                result += 2 ** i
            a = a // 2
            b = b // 2
        return result

    def encrypt(self, data, key):
        encrypted = []
        key_length = len(key)
        for i, char in enumerate(data):
            key_char = ord(key[i % key_length])
            char = ord(char)
            encrypted_char = self.bit_xor(char, key_char)
            encrypted.append(encrypted_char)
        return encrypted

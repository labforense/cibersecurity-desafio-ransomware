import os
import pyaes

# Arquivo criptografado
file_name = "teste.txt.testeransomware"

# Abrir o arquivo
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Mesma chave de 16 bytes
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo original novamente
with open("teste.txt", "wb") as f:
      f.write(decrypt_data)

print("Arquivo descriptografado com sucesso!")


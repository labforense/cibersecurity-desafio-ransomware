from pathlib import Path
import pyaes

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab_data"
SOURCE_FILE = LAB_DIR / "exemplo.txt"
ENCRYPTED_FILE = LAB_DIR / "exemplo.txt.testeransomware"
KEY = b"testeransomwares"


def main():
    if not SOURCE_FILE.is_file():
        raise FileNotFoundError(f"Arquivo de laboratório não encontrado: {SOURCE_FILE}")

    data = SOURCE_FILE.read_bytes()
    aes = pyaes.AESModeOfOperationCTR(KEY)
    encrypted_data = aes.encrypt(data)
    ENCRYPTED_FILE.write_bytes(encrypted_data)

    print("Simulação concluída.")
    print(f"Original preservado: {SOURCE_FILE.name}")
    print(f"Arquivo cifrado criado: {ENCRYPTED_FILE.name}")


if __name__ == "__main__":
    main()

from pathlib import Path
import pyaes

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab_data"
ENCRYPTED_FILE = LAB_DIR / "exemplo.txt.testeransomware"
RECOVERED_FILE = LAB_DIR / "exemplo.recuperado.txt"
KEY = b"testeransomwares"


def main():
    if not ENCRYPTED_FILE.is_file():
        raise FileNotFoundError(f"Arquivo cifrado não encontrado: {ENCRYPTED_FILE}")

    encrypted_data = ENCRYPTED_FILE.read_bytes()
    aes = pyaes.AESModeOfOperationCTR(KEY)
    recovered_data = aes.decrypt(encrypted_data)
    RECOVERED_FILE.write_bytes(recovered_data)

    print("Recuperação concluída.")
    print(f"Arquivo recuperado criado: {RECOVERED_FILE.name}")
    print("O arquivo cifrado foi preservado como evidência de laboratório.")


if __name__ == "__main__":
    main()

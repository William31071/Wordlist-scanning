import requests

def scan_url(target_url, word):
    """Escanea un sitio web buscando una palabra específica en las rutas."""
    full_url = f"{target_url.rstrip('/')}/{word}"
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Encontrado: {full_url} (Código {response.status_code})")
        elif response.status_code == 403:
            print(f"[-] Acceso denegado: {full_url} (Código {response.status_code})")
        elif response.status_code == 404:
            print(f"[!] No encontrado: {full_url} (Código {response.status_code})")
        else:
            print(f"[*] Estado desconocido: {full_url} (Código {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar con {full_url}: {e}")

def load_wordlist(file_path):
    """Carga la lista de palabras desde un archivo."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {file_path}")
        return []

def main():
    TARGET_URL = "http://127.0.0.1:8000"  # Cambia por el sitio a escanear
    WORDLIST_FILE = "wordlist.txt"  # Archivo con la lista de palabras

    words = load_wordlist(WORDLIST_FILE)
    if not words:
        print("No hay palabras para escanear.")
        return

    print(f"Escaneando {TARGET_URL} con {len(words)} palabras...\n")
    for word in words:
        scan_url(TARGET_URL, word)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Kensei File Organizer
Automatiza a organização de diretórios movendo arquivos para subpastas por categoria.
"""
import os
import shutil

# Cores para Estética Hacker
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Mapeamento de Extensões por Categoria
FILE_MAP = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "docs": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".md"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audios": [".mp3", ".wav", ".flac", ".ogg"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "scripts": [".py", ".sh", ".bat", ".ps1", ".js", ".html"]
}

def organize_files(directory: str):
    """
    Varre o diretório e organiza os arquivos conforme o FILE_MAP.
    """
    if not os.path.exists(directory):
        print(f"{RED}[!] Erro: O caminho '{directory}' não existe.{RESET}")
        return

    print(f"{GREEN}[*] Iniciando triagem em: {BOLD}{directory}{RESET}\n")
    
    # Dicionário para rastrear estatísticas por categoria
    stats = {cat: 0 for cat in FILE_MAP.keys()}
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    count = 0
    for file in files:
        # Evita que o script organize a si mesmo
        if file == os.path.basename(__file__):
            continue

        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for category, extensions in FILE_MAP.items():
            if file_ext in extensions:
                target_folder = os.path.join(directory, category)
                
                # Cria a pasta de categoria se não existir
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Caminhos de origem e destino
                source = os.path.join(directory, file)
                destination = os.path.join(target_folder, file)
                
                try:
                    shutil.move(source, destination)
                    print(f"{GREEN}[+] MOVIMENTADO:{RESET} {file} -> {category}/")
                    moved = True
                    stats[category] += 1
                    count += 1
                except Exception as e:
                    print(f"{RED}[!] Falha ao mover {file}: {e}{RESET}")
                break
        
        if not moved:
            print(f"{CYAN}[i] IGNORADO (Sem categoria):{RESET} {file}")

    print(f"\n{GREEN}{BOLD}--- OPERAÇÃO CONCLUÍDA ---{RESET}")
    if count > 0:
        print(f"{BOLD}Resumo por categoria:{RESET}")
        for cat, qty in stats.items():
            if qty > 0:
                print(f"  {CYAN}• {cat.capitalize()}:{RESET} {qty} arquivo(s)")
    print(f"{GREEN}Total de arquivos organizados: {count}{RESET}")

def main():
    print(f"{GREEN}{BOLD}--- KENSEI FILE ORGANIZER ---{RESET}")
    print(f"{GREEN}Módulo de higienização de diretórios ativo.{RESET}\n")

    try:
        path = input(f"{CYAN}[?]{RESET} Digite o caminho da pasta (ou Enter para atual): ").strip()
        
        # Se o usuário der enter, usa o diretório onde o script está
        if not path:
            path = os.getcwd()
            
        organize_files(path)

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Interrupção detectada. Abortando...{RESET}")
    except Exception as e:
        print(f"\n{RED}[!] Erro inesperado: {e}{RESET}")

if __name__ == "__main__":
    main()
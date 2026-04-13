#!/usr/bin/env python3
"""
Kensei Password Generator
Gerador de senhas customizável com foco em entropia e opções de complexidade.
"""
import random
import string
from datetime import datetime

# Cores para Estética Hacker
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

OUTPUT_FILE = "senhas.txt"

def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Gera uma senha aleatória baseada nos critérios fornecidos.
    """
    # O set base é sempre letras minúsculas para garantir consistência
    char_pool = string.ascii_lowercase
    
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Gera a senha usando random.choice para permitir repetição
    return ''.join(random.choice(char_pool) for _ in range(length))

def get_boolean_input(prompt: str) -> bool:
    """Valida entradas do tipo sim/não."""
    while True:
        resp = input(f"{CYAN}[?]{RESET} {prompt} (s/n): ").strip().lower()
        if resp in ['s', 'n']:
            return resp == 's'
        print(f"{RED}[!] Entrada inválida. Use 's' para sim ou 'n' para não.{RESET}")

def save_passwords_to_file(passwords: list):
    """
    Salva a lista de senhas no arquivo com timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n--- BATCH GENERATED AT {timestamp} ---\n")
            for p in passwords:
                f.write(f"{p}\n")
        print(f"{GREEN}[+] Senhas exportadas para {OUTPUT_FILE} com sucesso.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Erro ao salvar arquivo: {e}{RESET}")

def main():
    print(f"{GREEN}{BOLD}--- KENSEI PASSWORD GENERATOR ---{RESET}")
    print(f"{GREEN}Configure os parâmetros da sua chave de acesso.{RESET}\n")

    try:
        # Definição do tamanho
        while True:
            length_input = input(f"{CYAN}[?]{RESET} Comprimento da senha: ")
            if length_input.isdigit() and int(length_input) > 0:
                length = int(length_input)
                break
            print(f"{RED}[!] Erro: Digite um número inteiro positivo.{RESET}")

        # Definição de complexidade
        upper = get_boolean_input("Incluir letras MAIÚSCULAS?")
        nums  = get_boolean_input("Incluir Números?")
        syms  = get_boolean_input("Incluir Símbolos?")

        # Geração de lote (5 senhas)
        senhas = [generate_password(length, upper, nums, syms) for _ in range(5)]

        # Output Estilizado
        print(f"\n{GREEN}{'='*40}{RESET}")
        print(f"{BOLD}LOTE DE SENHAS GERADO:{RESET}")
        for i, s in enumerate(senhas, 1):
            print(f"{GREEN}{i}.{RESET} {s}")
        print(f"{GREEN}{'='*40}{RESET}")
        
        # Salva em arquivo
        save_passwords_to_file(senhas)

        # Dica de Segurança
        if length < 12:
            print(f"{RED}[!] Alerta de Segurança: Senhas com menos de 12 caracteres são vulneráveis.{RESET}")
        else:
            print(f"{GREEN}[+] Força da senha considerada aceitável para o lab.{RESET}")

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Operação cancelada pelo usuário.{RESET}")
    except Exception as e:
        print(f"\n{RED}[!] Erro inesperado: {e}{RESET}")

if __name__ == "__main__":
    main()
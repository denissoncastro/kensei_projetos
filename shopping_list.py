#!/usr/bin/env python3
"""
Script para gerenciamento de lista de compras.
Permite adicionar, visualizar e remover itens em um ambiente interativo.
"""

# Cores para Estética Hacker
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Configurações de Persistência
DATA_FILE = "lista_compras.txt"

def save_to_file(items: list) -> None:
    """
    Salva os itens da lista em um arquivo de texto.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for item in items:
                f.write(f"{item}\n")
        print(f"{GREEN}[+] Sincronização concluída: '{DATA_FILE}' atualizado.{RESET}")
    except Exception as e:
        print(f"{RED}[-] Erro crítico ao salvar dados: {e}{RESET}")

def main():
    compras = []
    
    while True:
        print(f"\n{GREEN}{BOLD}--- KENSEI SHOPPING LIST MANAGER ---{RESET}")
        print(f"{GREEN}1. Adicionar Item")
        print(f"2. Ver Lista")
        print(f"3. Remover Item")
        print(f"4. Sair{RESET}")
        
        opcao = input(f"\n{CYAN}[?]{RESET} Escolha a opção (1-4): ").strip()

        if opcao == '4':
            save_to_file(compras)
            print(f"{GREEN}[!] Encerrando o gerenciador. Até logo!{RESET}")
            break

        elif opcao == '1':
            item = input(f"{CYAN}Digite o nome do item: {RESET}").strip()
            if item:
                compras.append(item)
                print(f"{GREEN}[+] '{item}' adicionado com sucesso.{RESET}")
            else:
                print(f"{RED}[-] Erro: O nome do item não pode estar vazio.{RESET}")

        elif opcao == '2':
            if not compras:
                print(f"{RED}[!] A lista está vazia.{RESET}")
            else:
                print(f"\n{BOLD}ITENS ATUAIS:{RESET}")
                for i, item in enumerate(compras, 1):
                    print(f"{GREEN}{i}. {item}{RESET}")

        elif opcao == '3':
            if not compras:
                print(f"{RED}[!] A lista está vazia. Nada para remover.{RESET}")
                continue
            
            try:
                # Mostra a lista antes para o usuário saber o que remover
                for i, item in enumerate(compras, 1):
                    print(f"{GREEN}{i}. {item}{RESET}")
                    
                escolha = input(f"{CYAN}Digite o número do item para remover: {RESET}")
                idx = int(escolha)
                if idx < 1:
                    raise IndexError
                removido = compras.pop(idx - 1)
                print(f"{GREEN}[-] '{removido}' removido da lista.{RESET}")
            except (ValueError, IndexError):
                print(f"{RED}[-] Erro: Índice inválido. Digite um número válido da lista.{RESET}")

        else:
            print(f"{RED}[-] Erro: Opção inválida.{RESET}")

if __name__ == "__main__":
    main()
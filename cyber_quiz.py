#!/usr/bin/env python3
"""
Kensei Cyber Quiz
Módulo de avaliação de conhecimentos em Segurança da Informação.
"""
import random
import threading
import sys

# Cores para Estética Hacker
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def timed_input(prompt: str, timeout: int):
    """
    Solicita entrada do usuário com um limite de tempo.
    """
    print(prompt, end="", flush=True)
    result = [None]

    def get_input():
        result[0] = sys.stdin.readline().strip()

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    input_thread.join(timeout)
    if input_thread.is_alive():
        print(f"\n{RED}[!] TEMPO ESGOTADO!{RESET}")
        return None
    return result[0]

def main():
    # Pool de perguntas para garantir variação
    pool_perguntas = [
        {
            "pergunta": "O que caracteriza um ataque de Phishing?",
            "opcoes": ["Uso de força bruta em senhas", "E-mails ou sites falsos para roubar dados", "Exploração física de hardware"],
            "correta": 2
        },
        {
            "pergunta": "Qual o objetivo principal de um Ransomware?",
            "opcoes": ["Criptografar dados e exigir resgate", "Espionar a webcam do usuário", "Acelerar o processamento do sistema"],
            "correta": 1
        },
        {
            "pergunta": "O que significa a sigla MFA?",
            "opcoes": ["Multi-File Analysis", "Master Firewall Access", "Multi-Factor Authentication"],
            "correta": 3
        },
        {
            "pergunta": "Qual a função básica de um Firewall?",
            "opcoes": ["Aumentar a velocidade da internet", "Filtrar o tráfego de rede", "Remover vírus do disco rígido"],
            "correta": 2
        },
        {
            "pergunta": "O que é um ataque de Brute Force?",
            "opcoes": ["Tentar descobrir senhas por tentativa e erro", "Inundar um servidor com tráfego (DDoS)", "Roubar cabos de rede físicos"],
            "correta": 1
        }
    ]

    # Embaralha o pool e seleciona as perguntas da rodada
    random.shuffle(pool_perguntas)
    perguntas = pool_perguntas[:5]
    
    acertos = 0
    total = len(perguntas)
    tempo_limite = 20

    print(f"{GREEN}{BOLD}--- KENSEI CYBERSECURITY CHALLENGE ---{RESET}")
    print(f"{GREEN}Iniciando avaliação. Você tem {tempo_limite}s por pergunta.{RESET}\n")

    for i, item in enumerate(perguntas, 1):
        # Prepara opções embaralhadas para esta rodada
        opcoes = item['opcoes'][:]
        resposta_correta_texto = opcoes[item['correta'] - 1]
        random.shuffle(opcoes)
        novo_idx_correto = opcoes.index(resposta_correta_texto) + 1

        print(f"{BOLD}Pergunta {i}: {item['pergunta']}{RESET}")
        
        for idx, opcao in enumerate(opcoes, 1):
            print(f"{CYAN}{idx}){RESET} {opcao}")
        
        # Captura resposta com timer
        entrada = timed_input(f"\n{CYAN}[?]{RESET} Selecione (1-3): ", tempo_limite)
        
        if entrada is None:
            resposta = -1 # Indica timeout
        else:
            try:
                resposta = int(entrada)
            except ValueError:
                resposta = 0 # Entrada inválida

        # Verifica se acertou
        if resposta == novo_idx_correto:
            print(f"{GREEN}[+] Resposta correta!{RESET}\n")
            acertos += 1
        elif resposta == -1:
            print(f"{RED}[-] Falha por timeout. A correta era: {resposta_correta_texto}{RESET}\n")
        else:
            print(f"{RED}[-] Incorreto. A resposta correta era: {resposta_correta_texto}{RESET}\n")

    # Resultado Final
    print(f"{GREEN}{'='*45}{RESET}")
    print(f"{BOLD}RESULTADO FINAL: {acertos}/{total} ACERTOS{RESET}")
    
    if acertos >= 3:
        print(f"{GREEN}STATUS: APROVADO - CONHECIMENTO VALIDADO.{RESET}")
    else:
        print(f"{RED}STATUS: REPROVADO - NECESSÁRIO TREINAMENTO ADICIONAL.{RESET}")
    print(f"{GREEN}{'='*45}{RESET}")

if __name__ == "__main__":
    main()
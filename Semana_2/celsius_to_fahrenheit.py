#!/usr/bin/env python3
"""
Script para conversão de temperaturas (Celsius <-> Fahrenheit).
Permite que o usuário escolha a direção da conversão.
"""

# Cores para Estética Hacker
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Limites Físicos (Zero Absoluto)
ABS_ZERO_CELSIUS = -273.15
ABS_ZERO_FAHRENHEIT = -459.67

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print(f"\n{GREEN}{BOLD}--- KENSEI THERMAL CONVERTER ---{RESET}")
        print(f"{GREEN}1. Celsius para Fahrenheit")
        print(f"2. Fahrenheit para Celsius")
        print(f"3. Sair{RESET}")
        
        opcao = input(f"\n{CYAN}[?]{RESET} Escolha a opção (1, 2 ou 3): ").strip()

        if opcao == '3':
            print(f"{GREEN}[!] Encerrando o sistema de conversão. Até logo!{RESET}")
            break

        if opcao not in ['1', '2']:
            print(f"{RED}[-] Erro: Opção inválida. Tente novamente.{RESET}")
            continue

        try:
            if opcao == '1':
                celsius = float(input(f"{CYAN}Digite a temperatura em Celsius: {RESET}"))
                if celsius < ABS_ZERO_CELSIUS:
                    print(f"{RED}[!] Erro: Valor abaixo do zero absoluto ({ABS_ZERO_CELSIUS}°C).{RESET}")
                    continue
                
                resultado = celsius_to_fahrenheit(celsius)
                print(f"\n{GREEN}[RESULTADO] {celsius:.2f}°C -> {resultado:.2f}°F{RESET}")
            else:
                fahrenheit = float(input(f"{CYAN}Digite a temperatura em Fahrenheit: {RESET}"))
                if fahrenheit < ABS_ZERO_FAHRENHEIT:
                    print(f"{RED}[!] Erro: Valor abaixo do zero absoluto ({ABS_ZERO_FAHRENHEIT}°F).{RESET}")
                    continue
                
                resultado = fahrenheit_to_celsius(fahrenheit)
                print(f"\n{GREEN}[RESULTADO] {fahrenheit:.2f}°F -> {resultado:.2f}°C{RESET}")
                
        except ValueError:
            print(f"{RED}[-] Erro: Entrada inválida. Por favor, digite um número.{RESET}")

if __name__ == "__main__":
    main()

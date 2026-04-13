#!/usr/bin/env python3
"""
Script para converter temperatura de Celsius para Fahrenheit.
Pede ao usuário o valor em Celsius e exibe o resultado formatado.
"""

def celsius_to_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    try:
        # Pede o valor em Celsius
        celsius_input = input("Digite a temperatura em Celsius: ")
        celsius = float(celsius_input)
        
        # Converte para Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Mostra o resultado formatado
        print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F")
    except ValueError:
        print("Erro: Por favor, digite um número válido para a temperatura.")

if __name__ == "__main__":
    main()

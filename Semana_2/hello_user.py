def main():
    while True:
        # Solicita o nome ao usuário e remove espaços extras
        nome = input("Digite o seu nome: ").strip()
        
        # Valida se o nome tem pelo menos 3 caracteres
        if len(nome) >= 3:
            break
        print("Erro: O nome deve ter pelo menos 3 caracteres. Tente novamente.")

    # Exibe a saudação com o nome em maiúsculo
    print(f"Olá, {nome.upper()}!")

if __name__ == "__main__":
    main()

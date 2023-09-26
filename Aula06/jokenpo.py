import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    print("Bem-vindo ao Jogo Pedra, Papel e Tesoura!")

    while True:

        print("\nEscolha uma opção:")
        print("[1] Pedra")
        print("[2] Papel")
        print("[3] Tesoura")
        print("[4] Sair")

        escolha = input ("\nDigite o número da opção desejada: ")

        if escolha == "1":
            client_escolha = "pedra"
        elif escolha == "2":
            client_escolha = "papel"
        elif escolha == "3":
            client_escolha = "tesoura"
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")
            continue

        try:
            server_escolha, result = proxy.recebe_escolha(client_escolha)
            print(f"\nComputador escolheu: {server_escolha}")
            print(result)
        except ValueError as e:
            print(f"Erro: {e}")
        
    print("Jogo encerrado.")

if __name__ == "__main__":
    main()



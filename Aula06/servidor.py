from xmlrpc.server import SimpleXMLRPCServer # Criar um servidor xmlrpc
import random # Gerar escolhas aleatorias para o servidor

class Servidor:
    def __init__(self):
        self.escolha = ["pedra", "papel", "tesoura"]  # Lista com as possíveis escolhas do jogo

    def recebe_escolha(self, client_escolha):
        if client_escolha not in self.escolha: # Verifica se a escolha do cliente está na lista acima
            raise ValueError("Escolha inválida. Escolha entre pedra, papel ou tesoura.")
        
        server_escolha = random.choice(self.escolha) # Gera escolha aleatória baseada na lista
        result = self.resultado(client_escolha, server_escolha)
        return server_escolha, result

    def resultado(self, client_escolha, server_escolha): # Determina o resultado da rodada
        if client_escolha == server_escolha:
            return "Empate!"
        elif (
            (client_escolha == "pedra" and server_escolha == "tesoura")
            or (client_escolha == "papel" and server_escolha == "pedra")
            or (client_escolha == "tesoura" and server_escolha == "papel")
        ):
            return "Você Venceu!"
        else:
            return "Computador Venceu!"

def main():
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(Servidor())
    print("Servidor RPC rodando na porta 8000...")
    server.serve_forever()

if __name__ == "__main__":
    main()

import threading
import random
import time

# Função que gera um número aleatório entre 1 e 5
def gerar_numero_aleatorio():
    return random.randint(1, 5)

# Função assíncrona que simula a corrida da thread
def realizar_corrida(id_da_thread):
    posicao_atual = 0
    total_passos = 0
    
    print(f"Thread {id_da_thread} - Iniciando")
    
    while posicao_atual < 50:
        passos = gerar_numero_aleatorio()
        total_passos += passos
        posicao_atual += passos
        
        print(f"Vez da Thread {id_da_thread}")
        print(f"Número sorteado: {passos}")
        print(f"Thread {id_da_thread} Andou {passos} casas")
        print(f"Posição atual da Thread {id_da_thread}: {posicao_atual}")
        
        time.sleep(1)
    
    print(f"Thread {id_da_thread} - Chegou à posição 50! Total de passos: {total_passos}")
    
    return total_passos

# Função principal
def main():
    num_threads = 2
    threads_finalizadas = 0
    resultados = []

    def thread_secundaria(thread_id):
        total_passos = realizar_corrida(thread_id)
        resultados.append(total_passos)

    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=thread_secundaria, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    indice_vencedor = resultados.index(min(resultados))
    id_thread_vencedora = indice_vencedor + 1
    print(f"A thread {id_thread_vencedora} venceu com {resultados[indice_vencedor]} passos!")

if __name__ == "__main__":
    main()

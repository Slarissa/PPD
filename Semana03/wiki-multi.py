import threading
import time
import requests

def verificar_pagina_wiki_existente(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return url + '- Existe'
        elif response.status_code == 404:
            return url + '- Não existe'
        else:
            return url + '- desconhecido'
    except Exception as error:
        return url + '- erro: ' + str(error)

def thread_func(url):
    result = verificar_pagina_wiki_existente(url)
    return result

def main():
    print("Executando com threads:")

    wiki_page_urls = [f"https://en.wikipedia.org/wiki/{i + 1}" for i in range(50)]

    start_time = time.time()

    threads = []
    results = []

    for url in wiki_page_urls:
        thread = threading.Thread(target=lambda u: results.append(thread_func(u)), args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for result in results:
        print(result)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Tempo de execução em paralelo: {elapsed_time:.2f}s")

if __name__ == "__main__":
    main()

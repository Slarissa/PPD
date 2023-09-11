import threading
import time
import requests

def get_wiki_page_existence(wiki_page_url):
    try:
        response = requests.get(wiki_page_url)
        page_status = "unknown"
        if response.status_code == 200:
            page_status = "Existe"
        elif response.status_code == 404:
            page_status = "Não existe"
        
        return f"{wiki_page_url} - {page_status}"
    except Exception as error:
        return f"{wiki_page_url} - error: {error}"

def main():
    print("Executando de forma sequencial:")

    wiki_page_urls = [f"https://en.wikipedia.org/wiki/{i + 1}" for i in range(50)]

    start_time = time.time()

    def thread_function(url):
        result = get_wiki_page_existence(url)
        print(result)

    threads = []

    for url in wiki_page_urls:
        thread = threading.Thread(target=thread_function, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Tempo sequencial: {elapsed_time:.2f}s")

if __name__ == "__main__":
    main()

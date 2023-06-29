import sys
from threading import Thread
import encontrar_links
import arquivos

links_encontrados = set()
links_processados = set()


def inicia_threads():
    threads = []
    novos_links_encontrados = []

    for link in links_encontrados:
        thread = Thread(target=processar_link, args=(link, novos_links_encontrados))
        thread.start()
        threads.append(thread)

    # Espera tudo terminar
    for thread in threads:
        thread.join()

    return novos_links_encontrados


def processar_link(link, results):
    global links_processados

    if link not in links_processados:
        links_processados.add(link)
        novos_links_encontrados = encontrar_links.encontrar_links(links_processados, link)
        print("PROCESSAR LINK | ", link)
        results.extend(novos_links_encontrados)
    else:
        print("JA PROCESSADO LINK | ", link)


def main():
    global links_encontrados, links_processados

    while(True):

        links_encontrados = arquivos.ler_linhas_arquivo(links_encontrados, "links_encontrados.txt")
        links_processados = arquivos.ler_linhas_arquivo(links_processados, "links_processados.txt")

        if len(links_encontrados) == 0:
            links_encontrados.add('https://ufop.br/')

        novos_links_encontrados = inicia_threads()
        
        links_encontrados = set()

        for link in novos_links_encontrados:
            if link not in links_processados:
                links_encontrados.add(link)

        arquivos.escrever_linhas_arquivo(links_encontrados,  "links_encontrados.txt")
        arquivos.escrever_linhas_arquivo(links_processados,  "links_processados.txt")


if __name__ == '__main__':
    sys.exit(main())

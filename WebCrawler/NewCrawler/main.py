import sys
from threading import Thread
import ssl
import time

import encontrar_links
import arquivos

links_encontrados = set()
links_processados = set()

def main():
    global links_encontrados, links_processados

    #while(True):
    links_a_remover = []
    novos_links_encontrados = []

    links_encontrados = arquivos.ler_linhas_arquivo(links_encontrados, "links_encontrados.txt")
    links_processados = arquivos.ler_linhas_arquivo(links_processados, "links_processados.txt")

    if len(links_encontrados) == 0:
        links_encontrados.add('https://ufop.br/')

    for link in links_encontrados:
        if link not in links_processados:
            links_processados.add(link)
            novos_links_encontrados = novos_links_encontrados + encontrar_links.encontrar_links(links_processados, link)
            print("PROCESSAR LINK | ", link)
        else:
            print("JA PROCESSADO LINK | ", link)

        # links_a_remover.append(link)
    
    links_encontrados = set()

    for link in novos_links_encontrados:
        if link not in links_processados:
            links_encontrados.add(link)

    # for link in links_a_remover:
    #     links_encontrados.remove(link)

    #arquivos.remover_linhas_arquivo(links_a_remover, "links_encontrados.txt")

    arquivos.escrever_linhas_arquivo(links_encontrados,  "links_encontrados.txt")
    arquivos.escrever_linhas_arquivo(links_processados,  "links_processados.txt")


if __name__ == '__main__':
    sys.exit(main())
from threading import Thread
import encontrar_links
from tkinter import messagebox
import requests

links_encontrados: set()
links_processados: set()
links_com_erro: set()

def inicia_threads(encontrados: set(), processados: set(), com_erro: set(), link_a_verificar):
    
    global links_encontrados, links_processados, links_com_erro
    links_encontrados = encontrados
    links_processados = processados
    links_com_erro = com_erro
    
    threads = []
    novos_links_encontrados = []
    try:
        for link in links_encontrados:
            thread = Thread(target=processar_link, args=(novos_links_encontrados, link, link_a_verificar))
            thread.start()
            threads.append(thread)
    except:
        print("Thread")

    # Espera tudo terminar
    for thread in threads:
        thread.join()

    links_encontrados = set()

    for link in novos_links_encontrados:
        if link not in links_processados and link not in links_com_erro:
            links_encontrados.add(link)

    return links_encontrados, links_processados, links_com_erro


def processar_link(results, link, link_a_verificar):
    global links_processados, links_com_erro

    if link not in links_processados and link not in links_com_erro:

        novos_links_encontrados, encontrou = encontrar_links.encontrar_links(links_processados, links_com_erro, link)

        if(encontrou):
            links_processados.add(link)
            print("PROCESSANDO... | ", link)
            results.extend(novos_links_encontrados)

            if link_a_verificar in novos_links_encontrados and link_a_verificar != '':
                mensagem = "O link que está sendo rastreado foi encontrado na página: ", link
                messagebox.showinfo("Link Encontrado", mensagem)
                with open('arquivosTXT/html_link_verificado.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.write(link+"\n")
                    arquivo.write(requests.get(link, verify=False).text)


        else:
            links_com_erro.add(link)
    else:
        print("LINK JA PROCESSADO | ", link)

import sys
import processar_links
import arquivos

links_encontrados = set()
links_processados = set()
links_com_erro = set()


link_inicial = 'https://www.ufop.br/'
link_a_verificar = ''

def main():
    global links_encontrados, links_processados, links_com_erro, link_inicial, link_a_verificar

    while(True):

        links_encontrados = arquivos.ler_linhas_arquivo(links_encontrados, "arquivosTXT/links_encontrados.txt")
        links_processados = arquivos.ler_linhas_arquivo(links_processados, "arquivosTXT/links_processados.txt")
        links_com_erro = arquivos.ler_linhas_arquivo(links_com_erro, "arquivosTXT/links_com_erro.txt")

        if len(links_encontrados) == 0 and len(links_processados) == 0:
            links_encontrados.add(link_inicial)
        elif len(links_encontrados) == 0:
            print("Chegamos ao fim !!")
            break

        links_encontrados, links_processados, links_com_erro = processar_links.inicia_threads(links_encontrados, links_processados, links_com_erro, link_a_verificar)

        arquivos.escrever_linhas_arquivo(links_encontrados, "arquivosTXT/links_encontrados.txt")
        arquivos.escrever_linhas_arquivo(links_processados, "arquivosTXT/links_processados.txt")
        arquivos.escrever_linhas_arquivo(links_com_erro, "arquivosTXT/links_com_erro.txt")


if __name__ == '__main__':
    sys.exit(main())

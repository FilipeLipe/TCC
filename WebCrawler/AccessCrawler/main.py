import time
import sys
import processar_links
import arquivos

links_encontrados = set()
links_processados = set()
links_com_erro = set()


link_inicial = 'https://www.ufop.br/'
dominio = 'ufop'
link_a_verificar = ''
result = []

def main():
    
    global links_encontrados, links_processados, links_com_erro, link_inicial, link_a_verificar

    while(True):
        
        tempo_inicio = time.time()

        links_encontrados = arquivos.ler_linhas_arquivo(links_encontrados, "arquivosTXT/links_encontrados.txt")
        links_processados = arquivos.ler_linhas_arquivo(links_processados, "arquivosTXT/links_processados.txt")
        links_com_erro = arquivos.ler_linhas_arquivo(links_com_erro, "arquivosTXT/links_com_erro.txt")

        links_processados_antes = len(links_processados)
        links_com_erro_antes = len(links_com_erro)

        if len(links_encontrados) == 0 and len(links_processados) == 0:
            links_encontrados.add(link_inicial)
        elif len(links_encontrados) == 0:
            print("Chegamos ao fim !!")
            break

        links_encontrados, links_processados, links_com_erro = processar_links.inicia_threads(links_encontrados, links_processados, links_com_erro, link_a_verificar)

        print("BATATA")
        resultado = {
            "processado": len(links_processados) - links_processados_antes, 
            "encontrado": len(links_encontrados),
            "erro": len(links_com_erro) - links_com_erro_antes,
            "tempo":round(time.time() - tempo_inicio, 1)
                   }
        result.append(resultado)
        print("\n\n", resultado,"\n\n")

        arquivos.escrever_linhas_arquivo(links_encontrados, "arquivosTXT/links_encontrados.txt")
        arquivos.escrever_linhas_arquivo(links_processados, "arquivosTXT/links_processados.txt")
        arquivos.escrever_linhas_arquivo(links_com_erro, "arquivosTXT/links_com_erro.txt")

        

    print(result)

if __name__ == '__main__':
    sys.exit(main())

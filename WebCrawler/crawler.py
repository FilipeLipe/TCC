import sys
from threading import Thread
import urllib.request
import ssl
import time

linksEncontrados = []
linksRastreados = []
linksRastreadosNovos = []
links = []
links0 = []
links1 = []
links2 = []
links3 = []
links4 = []
links5 = []
links6 = []
links7 = []
links8 = []
links9 = []
links404 = []
linksPDF = []
linksRadio = []
find = '"http'
posicao = 0

def encontrarLinks(url):
    
    if '.pdf' in url or '.doc' in url or '.docx' in url or '.xlsx' in url:
        linksPDF.append(url)
        linksRastreadosNovos.append(url)
        return

    if 'radio.ufop.br/sites/default/files' in url:
        linksRadio.append(url)
        return

    #Pega a url passada por parametro
    try:
        content = str(urllib.request.urlopen(url).read())
        linksRastreadosNovos.append(url)
    except Exception as err:
        links404.append(url)
        print("Erro no Link: "+ url)
        return

    while(True):
        try:
            try:
                posicao = int(content.index(find) + len(find))
            except:
                break

            content = content[posicao:]

            contentAux = int(content.index('"'))

            # Pega o link completog
            link = 'http'+ content[ : contentAux]

            #Tem que ter .ufop no link para indicar que faz parte do dominio da ufop
            if '.ufop' in link:

                #Verifica as extensões permitidas pelo ases
                if '.css' not in link and '.gif' not in link and '.js' not in link and '.png' not in link and '.jpg' not in link and '.php' not in link and '.JPG' not in link and '.jpeg' not in link:

                    #Links que precisam de autenticação ou que não serão tratados e que estou ignorando
                    if 'minha.ufop' not in link and 'minhaufop' not in link and 'https://proad.ufop.br/' not in link and 'facebook' not in link and 'instagram' not in link and 'play.google.com' not in link: 

                        #Links que não são analisados no ASES
                        if 'wp-json' not in link and 'jcarousel' not in link and 'ajax' not in link and 'wp-content' not in link and '\\\\' not in link:
                            
                            #Link que eh extremamente grande e custoso
                            if 'revistacuringa' not in link:

                                #Não permite inserir links duplicados
                                if link not in linksEncontrados:

                                    #Pega o ultimo numero do total de links e seleciona qual a lista que o link irá entrar
                                    balancearLinks(link)

            #Atualiza o content para que não pegue novamente o mesmo link
            content = content[contentAux:]

        except:
            if content.index('</html>'):
                print("Web Crawler chegou ao fim da página")
                break
            else:
                print("Erro inesperado no Web Crawler")
                break

def balancearLinks(link):
    #Adciona na lista total para controle
    links.append(link)

    #De acordo com a quantidade de links ja encontrados, ele determina em qual lista o link irá ser processado
    match str(len(links))[-1:]:
        case '0':
            links0.append(link)
        case '1':
            links1.append(link)
        case '2':
            links2.append(link)
        case '3':
            links3.append(link)
        case '4':
            links4.append(link)
        case '5':
            links5.append(link)
        case '6':
            links6.append(link)
        case '7':
            links7.append(link)
        case '8':
            links8.append(link)
        case '9':
            links9.append(link)

def iniciarThread(numThread, listLinks):
    inicio = time.time()
    for link in listLinks:
        print("\n\n\n===================================")
        print("\nTotal Links"+str(numThread)+": "+ str(len(listLinks)) +
        " | Rastreados: "+ str(len(linksRastreadosNovos)) +
        " | Erros: "+ str(len(links404)) +
        " | Tempo de execução: "+ str(round(time.time()-inicio,2)) + "s" + 
        " | PDF: "+ str(len(linksPDF)) +
        " | Radio: "+ str(len(linksRadio)) +
        "\nNOVO LINK SERÁ RASTREADO !!\nLink: "+ link +"\n")
        
        #Caso o link ainda não tenha sido rastreado, ele vai passar pelo processo
        if link not in linksRastreadosNovos and link not in linksRastreados:
            encontrarLinks(link)
        
        
def escreverArquivoLinks(arquivoLinks):
    while(True):
        if(len(links) % 50 == 0):
            for link in links:
                if link not in linksEncontrados:
                    linksEncontrados.append(link)
                    arquivoLinks.write(link+'\n')

            
def escreverArquivoLinksRastreados(arquivoLinksRastreados):
    while(True):
        if(len(linksRastreadosNovos) % 50 == 0):
            for link in linksRastreadosNovos:
                if link not in linksRastreados:
                    linksRastreados.append(link)
                    arquivoLinksRastreados.write(link+'\n')

def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    #Abre o arquivo com os links encontrados e adiciona a variavel
    with open('../Links.txt', 'w+') as arquivoLinks:
        linksEncontrados = arquivoLinks.readlines()
        linksEncontrados = [x.rstrip('\n') for x in linksEncontrados]

        #Abre o arquivo com os links rastreados e adiciona a variavel
        with open('../LinksRastreados.txt', 'w+') as arquivoLinksRastreados:
            linksRastreados = arquivoLinksRastreados.readlines()
            linksRastreados = [x.rstrip('\n') for x in linksRastreados]

            #Passa por todos os links encontrados e seleciona quais que ainda não foram selecionados
            for link in linksEncontrados:
                if link not in linksRastreadosNovos and link not in linksRastreados:
                    balancearLinks(link)
                    
            #Faz a primeira chamada para iniciar o dominio
            encontrarLinks('https://ufop.br/')

            t0 = Thread(target=iniciarThread, args=(0, links0))
            t1 = Thread(target=iniciarThread, args=(1, links1))
            t2 = Thread(target=iniciarThread, args=(2, links2))
            t3 = Thread(target=iniciarThread, args=(3, links3))
            t4 = Thread(target=iniciarThread, args=(4, links4))
            t5 = Thread(target=iniciarThread, args=(5, links5))
            t6 = Thread(target=iniciarThread, args=(6, links6))
            t7 = Thread(target=iniciarThread, args=(7, links7))
            t8 = Thread(target=iniciarThread, args=(8, links8))
            t9 = Thread(target=iniciarThread, args=(9, links9))

            t0.start()
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            
            threadArquivoLinks = Thread(target=escreverArquivoLinks, args=(arquivoLinks)).start()
            threadArquivoLinksRastreados = Thread(target=escreverArquivoLinksRastreados, args=(arquivoLinksRastreados)).start()

            while(True):

                if links == linksRastreados:
                    print("TODOS OS LINKS FORAM RASTREADOS !!")

                    #Depois que finalizar, irá printar todos os links encontrados
                    print(links)
                    break

if __name__ == '__main__':
    sys.exit(main())
    

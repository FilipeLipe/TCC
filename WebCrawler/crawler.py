import sys
import urllib.request
import ssl
import time

links = []
linksRastreados = []
links404 = []
find = '"http'
posicao = 0

def encontrarLinks(url):
    
    #Pega a url passada por parametro
    try:
        content = str(urllib.request.urlopen(url).read())
        linksRastreados.append(url)
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
                    if 'minha.ufop' not in link and 'minhaufop' not in link and 'https://proad.ufop.br/' not in link and 'facebook' not in link: 

                        #Links que não estão abrindo
                        #if 'http://www.ifac.ufop.br' not in link and 'http://www.ichs.ufop.br' not in link and 'http://www.impostosolidario.ufop.br/' not in link and 'ufop.br\\\\/jcarousel\\\\/ajax\\\\/views' not in link and 'ufop.br\\\\/search\\\\/node' not in link and 'https://sites.ufop.br/nti2/book/' not in link and 'http://u2.ufop.br/' not in link and 'https://antigo.propp.ufop.br/casadopesquisador' not in link and 'http://www.cead.ufop.br/sa2014/' not in link and 'http://www.cead.ufop.br/portfoliobrincante/' not in link and 'antigo.propp.ufop' not in link and 'https://nite.ufop.br/apresenta\\xc3\\xa7\\xc3\\xa3o' not in link and 'http://prof.ufop.br/devolu\\xc3\\xa7\\xc3\\xa3o-de-suprimentos-de-fundos' not in link and 'http:/www.prof.ufop.br/arq_gru/insc_prof_substituto_.html' not in link:
                            
                            #Não permite inserir links duplicados
                        if link not in links:
                            links.append(link)
                            print(link)

            #Atualiza o content para que não pegue novamente o mesmo link
            content = content[contentAux:]

        except:
            if content.index('</html>'):
                print("Web Crawler chegou ao fim da página")
                break
            else:
                print("Erro inesperado no Web Crawler")
                break

def main():

    inicio = time.time()
    ssl._create_default_https_context = ssl._create_unverified_context

    encontrarLinks('https://ufop.br/')

    for link in links:
        print("\n\n\n===================================")
        print("\nTotal Links: "+ str(len(links)) +" | Rastreados: "+ str(len(linksRastreados)) +" | Tempo de execução: "+ str(round(time.time()-inicio,2))+"s\nNOVO LINK SERÁ RASTREADO !!\nLink: "+ link +"\n")
        #Caso o link ainda não tenha sido rastreado, ele vai passar pelo processo
        if link not in linksRastreados:
            encontrarLinks(link)

        if links == linksRastreados:
            print("TODOS OS LINKS FORAM RASTREADOS !!")
            break
    
    #Depois que finalizar, irá printar todos os links encontrados
    print(links)



if __name__ == '__main__':
    sys.exit(main())
    

import sys
import urllib.request
links = []
linksRastreados = []
find = '"http'
posicao = 0

def encontrarLinks(url):
    #Pega a url passada por parametro
    content = str(urllib.request.urlopen(url).read())
    while(True):
        try:
            
            posicao = int(content.index(find) + len(find))
            content = content[posicao:]

            contentAux = int(content.index('"'))

            #Pega o link completo, colocamos so http pois caso o link seja um https ele coloca corretamente
            link = 'http'+ content[ : contentAux]

            #Verifica o link e desconsidera aqueles que possuam
            if '.css' not in link and '.gif' not in link and '.js' not in link and '.png' not in link and '.jpg' not in link and 'minha.ufop' not in link:

                #Tem que ter ufop no link para indicar que faz parte do dominio da ufop
                if 'ufop' in link:

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
    encontrarLinks('https://ufop.br/')

    for link in links:
        
        print("\n\nNOVO LINK SERÁ RASTREADO !!\nLink: "+ link +"\n\n")
        #Caso o link ainda não tenha sido rastreado, ele vai passar pelo processo
        if link not in linksRastreados:
            encontrarLinks(link)

        if links == linksRastreados:
            print("TODOS OS LINKS FORAM RASTREADOS !!")
            break



if __name__ == '__main__':
    sys.exit(main())
    

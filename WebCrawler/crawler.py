import urllib.request
links = []
content = str(urllib.request.urlopen("https://ufop.br/").read())
find = '"https://'
posicao = 0


while(True):
    posicao = int(content.index(find) + len(find))
    content = content[posicao:]

    contentAux = int(content.index('"'))
    link = content[ : contentAux]

    print('Link '+ str(posicao) +': "https://'+link+'"')
    content = content[contentAux:]


# for x in range(len(content)):
#     try:
#         posicao += int(content.index(find) + len(find))
#         link = content[ posicao : posicao + 100]
#         x = posicao
#         print("Link "+ str(posicao) +": "+link)
#     except:
#         print("Acabou os links")

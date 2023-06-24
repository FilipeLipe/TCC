
from typing import List

def ler_linhas_arquivo(links: set(), nome_arquivo: str) -> set():
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        linhas = [linha.strip() for linha in linhas]
        links.update(linhas)
        return links
    

def escrever_linhas_arquivo(links: set(), nome_arquivo: str):
    try:
        with open(nome_arquivo, 'a') as arquivo:
            for link in links:
                arquivo.write(link + '\n')
    except:
        print("Não conseguiu encontrar o arquivo: ", nome_arquivo)


def remover_linhas_arquivo(links_remover: List[str], nome_arquivo: str):
    with open(nome_arquivo, 'r') as arquivo:
        links = arquivo.readlines()

        diferenca = list(set(links) - set(links_remover))

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(diferenca)
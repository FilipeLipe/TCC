
import requests
requests.packages.urllib3.disable_warnings()
import ssl
from bs4 import BeautifulSoup
from typing import List

import filtro

def encontrar_links(links_processados: set(), links_com_erro: set(), url: str):
     
    ssl._create_default_https_context = ssl._create_unverified_context
    links_encontrados = set()

    try:
        response = requests.get(url, verify=False)
    except Exception as err:
            print("Erro no Link: "+ url)
            return links_encontrados, False
    
    if response.status_code == 200:
        conteudo_html = response.text
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        links = soup.find_all('a')
        for a in links:
            link = a.get('href')
            link = verificar_link_local(url, link)

            if filtro.valida_link(links_processados, links_com_erro, link):
                links_encontrados.add(link)
                
        return links_encontrados, True
    else:
        print('Erro ao acessar a página:', response.status_code ,' | ', url)
        return links_encontrados, False
    

def verificar_link_local(url, link):
    if link:
        if link.startswith('http'):
            return link
        
        if link.startswith('/'):

            dominio_url = url
            posicao_barra = url.find("/", 8) 
            if posicao_barra != -1:
                dominio_url = url[:posicao_barra]

            return dominio_url + link

    return None

    
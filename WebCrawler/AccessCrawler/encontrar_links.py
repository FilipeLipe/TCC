
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

            if link and link[0] == "/":
                if url[len(url)-1] == "/": 
                    link = url + link[1:]
                else:
                    link = url + link

            if filtro.valida_link(links_processados, links_com_erro, link):
                links_encontrados.add(link)
                
        return links_encontrados, True
    else:
        print('Erro ao acessar a página:', response.status_code ,' | ', url)
        return links_encontrados, False
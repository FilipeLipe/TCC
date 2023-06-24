
import requests
requests.packages.urllib3.disable_warnings()
import ssl
from bs4 import BeautifulSoup
from typing import List

def encontrar_links(url: str) -> List[str]:
    
    ssl._create_default_https_context = ssl._create_unverified_context
    links_encontrados = []

    try:
        response = requests.get(url, verify=False)
    except Exception as err:
            print("Erro no Link: "+ url)
            return
    
    if response.status_code == 200:
        conteudo_html = response.text
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            links_encontrados.append(link.get('href'))
        return links_encontrados
    else:
        print('Erro ao acessar a página:', response.status_code)
        return links_encontrados
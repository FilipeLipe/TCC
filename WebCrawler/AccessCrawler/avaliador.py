#link;porcentagem;totalErros;totalAvisos;marcacaoErros;marcacaoAvisos;comportamentoErros;comportamentoAvisos;conteudoInformacaoErros;conteudoInformacaoAvisos;apresentacaoDesignErros;apresentacaoDesignAvisos;multimidiaErros;multimidiaAvisos;formulariosErros;formulariosAvisos
import sys
import arquivos
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
from model.Avaliacao import Avaliacao
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

lock = Lock()
navegadores_disponiveis = []

def avaliarLink(link):
    avaliacao = Avaliacao(link)
    navegador = getNavegador()
    getAvaliacao(navegador, link)
    getResposta(navegador, avaliacao)
    liberarNavegador(navegador)
    pass

def getNavegador():
    if not navegadores_disponiveis:
        service = Service(GeckoDriverManager().install())
        firefox_options = Options()
        firefox_options.add_argument('-headless')
        navegador = webdriver.Firefox(service=service, options=firefox_options)
    else:
        navegador = navegadores_disponiveis.pop()
    return navegador

def liberarNavegador(navegador):
    navegadores_disponiveis.append(navegador)

def getAvaliacao(navegador, link):

    navegador.get("https://asesweb.governoeletronico.gov.br/")

    url_input = navegador.find_element(By.ID, "url")
    url_input.clear()
    url_input.send_keys(link)

    executar = navegador.find_element(By.ID, "input_tab_1")
    executar.click()
    print("Avaliando: "+ link)

def getResposta(navegador, avaliacao: Avaliacao):
    
    if awaitElemento(navegador):
        getPorcentagem(navegador, avaliacao)
        getTabela(navegador, avaliacao)
        setResposta(avaliacao)
        return True
    
    return False



def awaitElemento(navegador):
    wait = WebDriverWait(navegador, 70)  
    try:
        porcentagem_element = wait.until(EC.presence_of_element_located((By.ID, "webaxscore")))
        return True
    except TimeoutException:
        return False


def getPorcentagem(navegador, avaliacao: Avaliacao):
    porcentagem_element = navegador.find_element(By.ID, "webaxscore")
    avaliacao.porcentagem = porcentagem_element.find_element(By.TAG_NAME, "span").text


def getTabela(navegador, avaliacao: Avaliacao):
    tabela = navegador.find_element(By.ID, "tabelaErros")
    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        if len(colunas) >= 3:
            avaliacao.secoes.append(colunas[0].text.strip())
            avaliacao.erros.append(colunas[1].text.strip())
            avaliacao.avisos.append(colunas[2].text.strip())



def setResposta(avaliacao):
    with lock:
        with open('arquivosTXT/avaliacao.txt', 'a') as arquivo:
            arquivo.write('\n' + avaliacao.to_string())


if __name__ == '__main__':
    links_processados = set()
    links_processados = arquivos.ler_linhas_arquivo(links_processados, "arquivosTXT/links_processados.txt")

    max_threads = 20

    with ThreadPoolExecutor(max_threads) as executor:
        futures = {executor.submit(avaliarLink, link): link for link in links_processados}

        for future in futures:
            future.result()

    print("\nAvaliação de todos os links concluída!\n")

    
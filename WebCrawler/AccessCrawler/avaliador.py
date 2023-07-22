import sys
import arquivos
from model.Avaliacao import Avaliacao
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def avaliarLink(link):

    avaliacao = Avaliacao(link)

    navegador = getNavegador()
    
    getAvaliacao(navegador, link)

    getResposta(navegador, avaliacao)


def getNavegador():
    service = Service(GeckoDriverManager().install())
    firefox_options = Options()
    firefox_options.add_argument('-headless')
    return webdriver.Firefox(service = service, options=firefox_options)

def getAvaliacao(navegador, link):

    navegador.get("https://asesweb.governoeletronico.gov.br/")

    url_input = navegador.find_element(By.ID, "url")
    url_input.clear()
    url_input.send_keys(link)

    executar = navegador.find_element(By.ID, "input_tab_1")
    executar.click()

def getResposta(navegador, avaliacao: Avaliacao):

    getPorcentagem(navegador, avaliacao)
    getTabela(navegador, avaliacao)

    setResposta(avaliacao)


def getPorcentagem(navegador, avaliacao: Avaliacao):
    wait = WebDriverWait(navegador, 180)  
    porcentagem_element = wait.until(EC.presence_of_element_located((By.ID, "webaxscore")))
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
    with open('arquivosTXT/avaliacao.txt', 'a') as arquivo: 
        arquivo.write('\n'+ avaliacao.to_string())

if __name__ == '__main__':
    sys.exit(avaliarLink('http://ufop.br'))
    #link;porcentagem;totalErros;totalAvisos;marcacaoErros;marcacaoAvisos;comportamentoErros;comportamentoAvisos;conteudoInformacaoErros;conteudoInformacaoAvisos;apresentacaoDesignErros;apresentacaoDesignAvisos;multimidiaErros;multimidiaAvisos;formulariosErros;formulariosAvisos
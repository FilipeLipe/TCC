from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())

firefox_options = Options()
firefox_options.add_argument('-headless')

navegador = webdriver.Firefox(service = service, options=firefox_options)


navegador.get('https://asesweb.governoeletronico.gov.br/')

url = "https://asesweb.governoeletronico.gov.br/"
navegador.get(url)



url_input = navegador.find_element(By.ID, "url")
url_to_add = "https://www.ufop.br/"
url_input.clear()
url_input.send_keys(url_to_add)



execute_button = navegador.find_element(By.ID, "input_tab_1")
execute_button.click()


wait = WebDriverWait(navegador, 180)  
resultado_element = wait.until(EC.presence_of_element_located((By.ID, "webaxscore")))


div_element = navegador.find_element(By.ID, "webaxscore")

# Extrair o texto do elemento <strong> (o texto 'ASES')
strong_element = div_element.find_element(By.TAG_NAME, "strong")
texto_strong = strong_element.text

# Extrair o texto do elemento <span> (a porcentagem '63.67%')
span_element = div_element.find_element(By.TAG_NAME, "span")
texto_span = span_element.text

# Imprimir os resultados
print("Texto do <strong>: ", texto_strong)
print("Texto do <span>: ", texto_span)

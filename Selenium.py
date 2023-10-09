from selenium import webdriver # importando a função para abrir o navegador
from webdriver_manager.chrome import ChromeDriverManager # importando função que atualizará o webdriver
from selenium.webdriver.chrome.service import Service # importando função para executar webdriver_manager

from selenium.webdriver.common.by import By # Obter Elemento
from selenium.webdriver.common.keys import Keys # Obter Tecla
from selenium.webdriver.chrome.options import Options # Para realizar opções especificas do navegador

chrome_options = Options() # Variavel para ultilizar as opções do Chrome
chrome_options.add_argument("--start-maximized") # Inicie o Chrome maximizado
chrome_options.add_experimental_option("detach", True) # impendi que o navegador seja fechado
servico = Service(ChromeDriverManager().install()) # instalar chrome driver atualizado
navegador = webdriver.Chrome(service=servico, options=chrome_options) # abre o navegador

navegador.get("https://www.nuuvem.com/br-pt/") # ir para o site expecifico
navegador.find_element(By.XPATH, '//*[@id="header-nav"]/div[1]/div/ul/li[1]/a').click() # Clica no elemento selecionado
navegador.find_element(By.XPATH, '//*[@id="header-search-large"]/div/input').send_keys("Resident Evil 4") # Digita no elemento seleciona
navegador.find_element(By.XPATH, '//*[@id="header-search-large"]/div/input').send_keys(Keys.ENTER) # Realiza o comando ENTER do teclado
navegador.find_element(By.XPATH, '//*[@id="catalog"]/div[3]/div[2]/div/div/div[1]').click()
navegador.find_element(By.XPATH, '//*[@id="product"]/div[5]/div/aside[1]/div/div[1]/div[5]/div[1]/div/div/button').click()
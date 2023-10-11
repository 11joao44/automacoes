# bibliotecas necessárias
from selenium import webdriver  # função para abrir o navegador
from webdriver_manager.chrome import ChromeDriverManager  # função que atualiza o webdriver
from selenium.webdriver.common.by import By  # função para localizar elementos na página
from selenium.webdriver.common.keys import Keys  # função para simular teclas
from selenium.webdriver.chrome.options import Options  # função para configurar opções específicas do navegador
from selenium.webdriver.chrome.service import Service # função para controlar o serviço do ChromeDriver iniciar, parar.

# Configura as opções do navegador Chrome
chrome_options = Options() # Variavel para opção
chrome_options.add_argument("--start-maximized")  # Inicia o Chrome maximizado
chrome_options.add_experimental_option("detach", True)  # Impede que o navegador seja fechado

# Inicializa o serviço do ChromeDriver e atualiza
servico = Service(ChromeDriverManager().install())

# Inicializa o navegador Chrome com as opções configuradas
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Abre o site 
navegador.get("https://www.nuuvem.com/br-pt/")

# Localiza o elemento de pesquisa e clica nele
navegador.find_element(By.XPATH, '//*[@id="header-search-large"]/div/button/i').click()

# Localiza a caixa de pesquisa, insere o texto e pressiona Enter
navegador.find_element(By.XPATH, '//*[@id="header-search-large"]/div/input').send_keys("Resident Evil 4")
navegador.find_element(By.XPATH, '//*[@id="header-search-large"]/div/input').send_keys(Keys.ENTER)

# Clica no item selecionado da pesquisa
navegador.find_element(By.XPATH, '//*[@id="catalog"]/div[3]/div[2]/div/div/div[1]').click()

# Clica no botão desejado
navegador.find_element(By.XPATH, '//*[@id="product"]/div[5]/div/aside[1]/div/div[1]/div[5]/div[1]/div/div/button').click()

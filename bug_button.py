from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
site = webdriver.Chrome(service=servico, options=chrome_options)

site.get("https://gestaoweb.redeflex.com.br/efc-presentation/publico/sessaoEncerrada.jsf")
site.find_element(By.CLASS_NAME, 'ui-button').click()
# site.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/table/tbody/tr[2]/td/button').click()

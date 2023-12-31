# bibliotecas necessárias
import requests # Biblioteca fazer fazer requisição
import openpyxl # Biblioteca para criar arquivo Excel
from bs4 import BeautifulSoup # Biblioteca para analisar código HTML

workbook = openpyxl.Workbook() # Criar um novo arquivo Excel

sheet = workbook.active # Selecionar a planilha ativa (por padrão, há uma planilha chamada 'Sheet')

# Adicionar cabeçalhos para as colunas
sheet['A1'] = 'Título do jogo'
sheet['B1'] = 'Preço do jogo'

url = 'https://www.nuuvem.com/br-pt/catalog/price/promo/sort/release-date/sort-mode/desc'
requisicao = requests.get(url) # entrar no site fornecido 
print(requisicao) # para observar a resposta da requisição

site = BeautifulSoup(requisicao.text, "html.parser") # Analisa o HTML do site com BeautifulSoup
titulos = site.find_all(class_='product-title') # Encontrar todos os elementos com a classe "product-title" para obter os títulos
precos = site.find_all(class_='product-price--val') # Encontrar todos os elementos com a classe "product-price--val" para obter os preços

for i, (titulo_element, preco_element) in enumerate(zip(titulos, precos), start=2):
    titulo = titulo_element.text.strip()
    preco = preco_element.text.strip()
    sheet[f'A{i}'] = titulo
    sheet[f'B{i}'] = preco

# Salvar o arquivo Excel caso o arquivo ja exista
# as colunas e linhas serão preenchidas tudo novamente semelhante a uma atualização
workbook.save('produtos.xlsx')

print("Dados foram escritos no arquivo Excel 'produtos.xlsx'")

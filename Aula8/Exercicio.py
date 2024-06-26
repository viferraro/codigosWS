import requests
from bs4 import BeautifulSoup
import re

# Faz a requisição HTTP para a página
url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
pagina = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os textos na página
all_text = soup.get_text()

'''Considere a string:
"1227 122228 104 1222222226 1232323 1523 121212512 250"
Faça um programa com regex que seleciona
1) os itens com dígito 7 (em qualquer posição)
2) os itens com dígitos 2 e 5 (em qualquer posição).'''

msg='1227 122228 104 1222222226 1232323 1523 121212512 250'
#padrao = '12*7'
#print('1- Padrão: "12*7"')
padrao = r'\b\d*7\d*\b'
print('1- Padrão: "d*7"') 
teste = re.findall(padrao, msg)
print(teste)


padrao = r'\b\d*2\d*5\d*\b | \b\d*5\d*2\d*\b'
print('2- Padrão: "d*2d*5" ou "d*5d*2"')
teste = re.findall(padrao, msg)
print(teste)
#obter preços do mercado livre
import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

nome = input('Qual produto voce deseja pesquisar? ')

#print(url_base + produto)

response = requests.get(url_base + nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs= {'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})


    print('Título do produto:', titulo.text)
    print('link do produto:', link['href'])
    
    if (centavos):
        print('Preço do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preço do produto: R$', real.text)


    print('\n\n')
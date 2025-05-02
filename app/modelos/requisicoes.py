import requests
import json

url = 'http://127.0.0.1:8000/api/restaurantes/'
response = requests.get(url)

def requisicao_nomes():
    if response.status_code == 200:
        dados_json = response.json()
        restaurantes = []
        for item in dados_json['Dados']:
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in restaurantes:
                restaurantes.append(nome_do_restaurante)
    return restaurantes

def criar_cardapios(lista: list):
    cardapios = []
    for item in lista:
        url = f'http://127.0.0.1:8000/api/restaurantes/?restaurante={item}'
        response = requests.get(url)
        cardapios.append(response.json()['Cardapio'])
    return cardapios



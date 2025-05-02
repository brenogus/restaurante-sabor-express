# Código para criação de API onde é possível consultar o cardápio de cada restaurante

from fastapi import FastAPI, Query # Importação das classe FastAPI (classe da api), e Querry(Classe usada como parâmetro na criação de APIs)
import requests


app = FastAPI() # Instanciando um objeto API


@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes.
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
   
    if response.status_code == 200: # Verificação se a requisição foi satisfeita
        dados_json = response.json() # Criação de uma variável que armazena os dados JSON da requisição
        if restaurante is None: # Condicional que verifica se a query da URL esta vazia
            return {'Dados':dados_json} # Retorna todos os restaurantes consumidos pela requisição da variável url

        dados_restaurante = [] # Criação de uma lista que representa uma lista com todos os restaurantes
        for item in dados_json: # Laço para criação de um dicionário pra cada restaurante, esse dicionário será armazenado em dados_restaurante
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante} # Resposta da requsição feita em get_restaurantes
    else: 
        return {'Erro':f'{response.status_code} - {response.text}'} # Fechamento do condicional que verifica se a requisição teve resposta, nesse caso é para quando a conexão falha


# Para ligar o servidor uvicorn digite no terminal "uvicorn api.main:app --reload"
# Aperte ctrl e clique na URL indicada no terminal para acessar a página no navegador
# Para acessar os dados da API vc deve digitar na barra do navegador após o numero da porta "/caminho/usado/na/criação/da/API" (fica no decorator da função)
# para digitar uma query escreva "URL/caminho/usado/na/criação/da/API/?nome_do_parametro_da_função=valor_que_quer_pesquisar"
# Para sair do uvicorn aperte ctrl + c
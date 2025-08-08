# Esse código serve para ler e filtrar dados de um arquivo JSON de restaurantes

import requests # Módulo para requisições
import json # Módulo para trabalhar com JSON

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:   # Verifica se a requisição HTTP foi satisfeita
    dados_json = response.json() # Criação de uma variável com os arquivos JSON do link original
    dados_restaurante = {} # Cria um dicionário onde serão armazenados os dados dos restaurantes
    for item in dados_json: # Laço for que irá criar uma chave e uma lista como valor onde serão armazenados todos os dados de cada restaurante
        nome_do_restaurante = item['Company'] # Variavel criada para facilitar o processo (não ter que acessar o nome pelo indice)
        if nome_do_restaurante not in dados_restaurante: # Condicional para que todas as chaves de dados_restaurante sejam únicas
            dados_restaurante[nome_do_restaurante] = [] # Criando uma chave com uma lista como value para cada restaurante
        dados_restaurante[nome_do_restaurante].append({ # fazendo o append dos itens do cardápio de cada restaurante
            "item" : item['Item'], 
            "price" : item['price'],
            "description" : item['description']
        })
else:
    print(f'O erro foi {response.status_code}') # Condicional para caso a conexão da requisição não seja satisfeita

for nome_do_restaurante, dados in dados_restaurante.items(): # Laço for para criar os arquivos txt para cada restaurante
    nome_do_arquivo = f'restaurante-sabor-express/app/api/cardapios/{nome_do_restaurante}.json' # Salva os arquivos na pasta cardapios
    with open(nome_do_arquivo,'w') as arquivo_restaurante: # Opção 'w' significa write (criar arquivo)
        json.dump(dados,arquivo_restaurante,indent=4)
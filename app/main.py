from modelos.restaurante import Restaurante
from modelos.requisicoes import requisicao_nomes,criar_cardapios
from modelos.cardapio.item_cardapio import ItemCardapio

nomes_restaurantes = requisicao_nomes()
cardapios = criar_cardapios(nomes_restaurantes)
restaurantes_dict = {nome: Restaurante(nome) for nome in nomes_restaurantes}

for i, cardapio in enumerate(cardapios):
    cardapios[i] = [ItemCardapio(item) for item in cardapio]

for nome, cardapio in zip(nomes_restaurantes, cardapios):
    restaurante = restaurantes_dict[nome]
    restaurante.adicionar_no_cardapio(cardapio)






def main():
   restaurantes_dict[nomes_restaurantes[1]].listar_cardapio

if __name__ == '__main__':
    main()
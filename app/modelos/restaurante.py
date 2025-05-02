from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from modelos.cardapio.bebida import Bebida

class Restaurante:
    '''Classe principal que representa um restaurante'''

    restaurantes = []
    def __init__(self,nome: str):
        self._nome = nome.strip().title()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Método de classe usado para listar os restaurantes.'''

        print(f'{'Nome do restaurante'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
  
    def alternar_estado(self):
        '''Método para ativar ou desativar o status do restaurante.'''
        self._status = not self._status

    def receber_avaliacao(self, cliente: str, nota):
        '''Método que registra uma avaliação de um cliente.'''

        try:
            nota = float(nota)
        except ValueError:
            print(f"Nota inicial inválida para {cliente}. Vamos tentar novamente.")
            nota = -1  # força a entrada no while

        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            while True:
                try:
                    nova_nota = float(input(f"{cliente}, digite uma nota entre 0 e 5: "))
                    if 0 <= nova_nota <= 5:
                        avaliacao = Avaliacao(cliente, nova_nota)
                        self._avaliacao.append(avaliacao)
                        break
                    else:
                        print("Nota fora do intervalo permitido. Tente novamente.\n")
                except ValueError:
                    print("Entrada inválida. Digite um número.\n")
                    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        elif isinstance(item, list) and all(isinstance(i, ItemCardapio) for i in item):
            self._cardapio.extend(item)
        else:
            raise ValueError("Esperado ItemCardapio ou lista de ItemCardapio")



    @property
    def avaliacoes(self):
        '''Property para mostrar as avaliações registradas no restaurante.'''

        for avaliacao in self._avaliacao:
            print(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Property para mostrar uma média de todas as avaliações registradas no restaurante.'''

        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma_das_notas / len(self._avaliacao),1)
        return media

    @property
    def ativo(self):

        '''Property para mostrar o status do restaurante.'''

        return f'Ativado' if self._status else 'Desativado'
    
    @property
    def listar_cardapio(self):
       for item in self._cardapio:
           print(item)



class Avaliacao:
    '''Classe que representa uma avaliação feita por um cliente sobre um restaurante.'''
    
    def __init__(self, cliente: str,nota: float):
        self._cliente = cliente
        self._nota = nota  # valor ainda não definido


    def __str__(self):
        return f"Avaliação de {self._cliente}: nota {self._nota}"
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente.title()
        self._nota = nota
        self._anonimato = True

    @property
    def anonimato(self):
        return 'Anônimo' if self._anonimato else self._cliente
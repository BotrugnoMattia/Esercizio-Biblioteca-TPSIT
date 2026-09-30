from Libro import Libro


class Biblioteca:
    """Gestisce un archivio di libri (inserimento, ricerca, conteggio)."""

    def __init__(self, nome="Biblioteca Comunale"):
        self.nome = nome
        self.catalogo = []

    def inserisci_libro(self, libro):
        if isinstance(libro, Libro):
            self.catalogo.append(libro)
        else:
            raise TypeError("L'oggetto deve essere un'istanza di Libro.")

    def cerca_per_titolo(self, titolo):
        return [l for l in self.catalogo if titolo.lower() in l.titolo.lower()]

    def cerca_per_autore(self, autore):
        return [l for l in self.catalogo if autore.lower() in l.autore.lower()]

    def conteggio_libri(self):
        return len(self.catalogo)

    def __str__(self):
        return f"Biblioteca '{self.nome}' - Totale libri: {self.conteggio_libri()}"
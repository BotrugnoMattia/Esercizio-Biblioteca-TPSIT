class Libro:
    """Rappresenta un singolo libro della biblioteca."""

    def __init__(self, titolo, autore, anno, editore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def readingTime(self, pagine_per_minuto=2):
        """Calcola il tempo stimato di lettura in minuti (di default 2 pagine al minuto)."""
        if pagine_per_minuto <= 0:
            raise ValueError("La velocità di lettura deve essere maggiore di zero.")
        minuti_totali = self.pagine / pagine_per_minuto
        return round(minuti_totali, 1)

    def __str__(self):
        return f"'{self.titolo}' di {self.autore} ({self.anno}) - {self.editore}, {self.pagine} pag."
import random
from biblioteca import Biblioteca
from Libro import Libro


def genera_1000_libri(biblioteca):
    autori = ["Italo Calvino", "Umberto Eco", "Dante Alighieri", "Giacomo Leopardi", "Luigi Pirandello"]
    editori = ["Mondadori", "Sellerio", "Einaudi", "Rizzoli", "Feltrinelli"]

    for i in range(1, 1001):
        titolo = f"Libro Numero {i}"
        autore = random.choice(autori)
        anno = random.randint(1300, 2026)
        editore = random.choice(editori)
        pagine = random.randint(100, 900)

        libro = Libro(titolo, autore, anno, editore, pagine)
        biblioteca.inserisci_libro(libro)


if __name__ == "__main__":
    print("=== TEST GESTIONE BIBLIOTECA (1000 LIBRI) ===\n")
    biblio = Biblioteca("Biblioteca Centrale")
    genera_1000_libri(biblio)

    print(biblio)
    print(f"Conteggio confermato: {biblio.conteggio_libri()} libri.")

    risultati = biblio.cerca_per_autore("Italo Calvino")
    print(f"Trovati {len(risultati)} libri di Italo Calvino.")

    primo_libro = risultati[0]
    print(f"\nEsempio: {primo_libro}")
    print(f"Tempo di lettura stimato: {primo_libro.readingTime()} minuti.")
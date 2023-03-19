# Program "test_data_create.py" tworzy dane testowe w postaci ciągu odwołań
# do stron, który będzie wykorzystany przez programy implementujące działanie
# algorytmów zastępowania stron do wykonania symulacji.
# Ciąg odwołań do stron (ciąg liczb) jest zapisany w pliku "test_data.txt", który
# znajduje się w folderze "test_data".

# Moduł random potrzebny do generowania pseudolosowych danych.
import random


# Funkcja tworząca dane testowe do projektu w postaci ciągu odwołań do stron.
def create_data():

    # Deklaracja pustej listy, w której umieścimy wygenerowane dane.
    sequence_of_pages = []

    # Utworzenie pliku tekstowego, w którym umieścimy wygenerowane dane testowe.
    with open("test_data/test_data.txt", "w") as file:

        # Do pliku zapisujemy 100 linii zawierających po jednej liczbie.
        # Dokładniej mówiąc, każda linia zawiera stronę o pewnym numerze.
        for line in range(1, 101):

            # Wylosowana liczba z zakresu od 1 do 25 to element ciągu odwołań do stron.
            # Dokładniej mówiąc, to strona o numerze od 1 do 25.
            number_of_page = random.randint(1, 25)

            # Dodajemy wylosowane numery stron do listy.
            sequence_of_pages.append(number_of_page)

            # Zapisujemy wylosowane numery stron do pliku tekstowego.
            # Każda linia zawiera jedną liczbę.
            file.write(f"{number_of_page}\n")

    # Utworzenie pliku tekstowego o nazwie "data_for_page_substituion_solver.txt",
    # do którego zapiszemy wygenerowane dane w następującej postaci:
    # - pierwsza linia: numery stron oddzielone spacją,
    # - druga linia: znak nowej linii.
    # Plik znajduje się w folderze "test_data".
    # Używam tego pliku do kopiowania wygenerowanych danych do kalkulatora online,
    # który potwierdza mi czy symulacja wykonała się prawidłowo.
    with open("test_data/data_for_page_substituion_solver.txt", "a") as file:
        for line in sequence_of_pages:
            file.write(f"{line} ")

        file.write("\n")

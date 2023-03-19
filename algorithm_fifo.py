# Program "algorithm_fifo.py" przeprowadza symulację algorytmu FIFO
# zastępowania stron. Dokładniej mówiąc, pobiera on liczbę ramek,
# z których ma korzystać oraz ciąg odwołań do stron. Następnie
# dla każdej strony z ciągu określa czy była ona w pamięci,
# czy też nie. Dane te zlicza odpowiednio jako wartości
# "hit" i "faults". Ostatecznie zwracamy listę, na której
# znajduje się ilość ramek, długość ciągu odwołań do stron,
# ilość stron trafionych, ilość stron brakujących
# wskaźnik procentowy stron trafionych oraz wskaźnik
# procentowy stron brakujących. Lista ta jest przekazywana
# do pliku "write_results.py", w którym zapisujemy dane z niej
# odczytane do odpowiedniego pliku.

# Funkcja przeprowadzająca symulację algorytmu FIFO zastępowania stron.
# Pobiera ona ilość ramek, na których ma działać oraz ciąg odwołań do stron
# w postaci listy. Następnie zlicza, które strony z ciągu były w pamięci.
# Ostatecznie zwraca listę, w której znajduje się ilość ramek, długość ciągu odwołań do stron,
# ilość stron trafionych, ilość stron brakujących stron, wskaźnik procentowy stron trafionych
# oraz wskaźnik procentowy stron brakujących.
def fifo(number_of_frames, list_of_pages):

    # Deklaracja listy o wielkości zależnej od ilości ramek.
    # Lista symbolizuje kolumnę odwołań do stron.
    # Każdy indeks listy to osobna ramka, w której planowo
    # mają się znajdować odwołania do stron.
    # Strony wchodzą do listy od lewej strony (w kolumnie byłoby to od góry).
    # Czyli najnowsze strony będą na skrajnym lewym indeksie listy, a najstarsze
    # na skrajnym prawym indeksie listy.
    # Apostrofy w kwadratowych nawiasach mają symbolizować pustą ramkę.
    list_of_frames = [''] * number_of_frames

    # Deklaracja aktualnego numeru ramki pamięci.
    frame = 0

    # Deklaracja ilości stron, których nie było w pamięci
    # podczas wykonywania algorytmu.
    faults = 0

    # Deklaracja ilości stron, które były w pamięci,
    # podczas wykonywania algorytmu
    hit = 0

    # Przechodzimy po kolei przez wszystkie elementy listy.
    # Elementami listy dla przypomnienia są odwołania do stron.
    # Ustalamy ilość stron, których nie było w pamięci oraz
    # ilość stron, które w niej były.
    for page in list_of_pages:

        # Jeżeli danej strony nie ma na liście ramek, to sprawdzamy,
        # czy aktualny numer ramki jest mniejszy niż całkowita ilość ramek
        # na liście.
        if page not in list_of_frames:
            if frame < number_of_frames:

                # Jeżeli tak, to wpisujemy stronę w odpowiednią ramkę, czyli w miejsce
                # listy o indeksie, który wyznacza aktualny numer obsługiwanej ramki.
                list_of_frames[frame] = page
            else:

                # Jeżeli danej strony nie ma na liście ramek i numer ramki
                # jest równy lub większy niż całkowita ilość ramek, to wyznaczane jest modulo
                # z aktualnej liczby ramek, czyli reszta z dzielenia aktualnej liczby ramek
                # przez całkowitą liczbę ramek. W ten sposób zapisujemy stronę do ramki.
                # Operacja modulo ma zablokować możliwość wpisania strony na nieistniejącą ramkę.
                frame = frame % number_of_frames
                list_of_frames[frame] = page

            # Przejście do kolejnej ramki.
            frame += 1

            # Zliczenie kolejnej strony, której nie było w pamięci.
            faults += 1
        else:

            # Zliczenie kolejnej strony, która była w pamięci.
            hit += 1

    # Utworzenie listy z wynikami przeprowadzonej symulacji zastępowania stron
    # według algorytmu FIFO. Wyniki to kolejno:
    # 1. całkowita ilość ramek,
    # 2. długość ciągu odwołań do stron,
    # 3. ilość stron, których nie było w pamięci podczas przeprowadzania symulacji,
    # 4. ilość stron, które były w pamięci podczas przeprowadzania symulacji,
    # 5. wskaźnik procentowy stron trafionych,
    # 6. wskaźnik procentowy stron brakujących.
    results_of_the_fifo_algorithm = [[number_of_frames, len(list_of_pages),
                                      hit, faults, hit / len(list_of_pages),
                                      faults / len(list_of_pages)]]

    return results_of_the_fifo_algorithm

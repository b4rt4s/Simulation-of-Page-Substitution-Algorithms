# Program "algorithm_lru.py" przeprowadza symulację algorytmu LRU
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

# Funkcja przeprowadzająca symulację algorytmu LRU zastępowania stron.
# Pobiera ona ilość ramek, na których ma działać oraz ciąg odwołań do stron
# w postaci listy. Następnie zlicza, które strony z ciągu były w pamięci.
# Ostatecznie zwraca listę, w której znajduje się ilość ramek, długość ciągu odwołań do stron,
# ilość stron trafionych, ilość stron brakujących stron, wskaźnik procentowy stron trafionych
# oraz wskaźnik procentowy stron brakujących.
def lru(number_of_frames, list_of_pages):

    # Deklaracja listy o wielkości zależnej od ilości ramek.
    # Lista symbolizuje kolumnę odwołań do stron.
    # Każdy indeks listy to osobna ramka, w której planowo
    # mają się znajdować odwołania do stron.
    # Strony wchodzą do listy od prawej strony (w kolumnie byłoby to od dołu).
    # Czyli najnowsze strony będą na skrajnym prawym indeksie listy, a najstarsze
    # na skrajnym lewym indeksie listy.
    # Apostrofy w kwadratowych nawiasach mają symbolizować pustą ramkę.
    list_of_frames = [''] * number_of_frames

    # Deklaracja ilości stron, których nie było w pamięci
    # podczas wykonywania algorytmu.
    faults = 0

    # Deklaracja ilości stron, które były w pamięci,
    # podczas wykonywania algorytmu
    hit = 0

    # Przechodzimy po kolei przez wszystkie elementy listy,
    # którymi dla przypomnienia są odwołania do stron.
    # Ustalamy ilość stron, których nie było w pamięci oraz
    # ilość stron, które w niej były.
    for page in list_of_pages:

        # Warunek, który spełnia się, jeżeli danej strony nie ma na liście ramek (w pamięci).
        if page not in list_of_frames:

            # Sprawdzamy, czy całkowita liczba ramek jest równa wielkości listy ramek.
            # Jeżeli tak, to usuwamy stronę z ramki nr 0, czyli usuwamy stronę
            # znajdującą się na skrajnym lewym indeksie listy ramek.
            if number_of_frames == len(list_of_frames):
                list_of_frames.pop(0)

            # Niezależnie od wykonania się poprzedniego warunku wpisujemy stronę
            # w ostatnią ramkę, czyli tę znajdującą się na skrajnym prawym
            # indeksie listy ramek.
            list_of_frames.append(page)

            # Zliczenie kolejnej strony, której nie było w pamięci.
            faults += 1

        # Warunek, który spełnia się, jeżeli dana strona jest na liście ramek (w pamięci).
        else:

            # Jeżeli dana strona znajduje się w pamięci, to usuwamy tę stronę z ramki,
            # w której się ona aktualnie znajduje i wpisujemy ją do ramki znajdującej
            # się na skrajnym prawym indeksie listy ramek.
            list_of_frames.remove(page)
            list_of_frames.append(page)

            # Zliczenie kolejnej strony, która była w pamięci.
            hit += 1

    # Utworzenie listy z wynikami przeprowadzonej symulacji zastępowania stron
    # według algorytmu LRU. Wyniki to kolejno:
    # 1. całkowita ilość ramek,
    # 2. długość ciągu odwołań do stron,
    # 3. ilość stron, których nie było w pamięci podczas przeprowadzania symulacji,
    # 4. ilość stron, które były w pamięci podczas przeprowadzania symulacji,
    # 5. wskaźnik procentowy stron trafionych,
    # 6. wskaźnik procentowy stron brakujących.
    results_of_the_lru_algorithm = [[number_of_frames, len(list_of_pages),
                                    hit, faults, hit / len(list_of_pages),
                                    faults / len(list_of_pages)]]

    return results_of_the_lru_algorithm

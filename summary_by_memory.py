# Program "summary_by_memory.py" wykonuje zestawienie składające się
# pięciu kolumn. Oto one:
# - kolumna nr 1: liczba ramek od 1 do 20,
# - kolumna nr 2: liczba trafionych stron podczas przeprowadzania
# symulacji zgodnie z algorytmem FIFO,
# - kolumna nr 3: liczba brakujących stron podczas przeprowadzania
# symulacji zgodnie z algorytmem FIFO,
# - kolumna nr 4: liczba trafionych stron podczas przeprowadzania
# symulacji zgodnie z algorytmem LRU,
# - kolumna nr 5: liczba brakujących stron podczas przeprowadzania
# symulacji zgodnie z algorytmem LRU.

# Funkcja "read_summary_of_pages" to funkcja odczytująca dane testowe
# z plików wynikowych dla algorytmów FIFO i LFU.
def read_summary_of_pages(name, number_of_frames):

    # Otworzenie pliku z wynikami.
    with open(f"algorithm_{name}_results/algorithm_{name}_results{number_of_frames}.txt") as file:

        # Umieszczenie w zmiennej "lines" listy, której elementami są
        # trzyelementowe listy zagnieżdżone. Pierwszy element to wielkość
        # ramki, drugi to ilość trafionych stron, a trzeci to ilość
        # brakujących stron.
        lines = [line.split() for line in file]

        # Utworzenie pustej listy, w której umieścimy listy trzyelementowe składające
        # się z wyżej wymienionych danych.
        list_of_results = []

        # Zapis danych wynikowych do pustej listy, której elementami
        # są zagnieżdżone trzyelementowe listy.
        # Pierwsza liczba to wielkość ramki pamięci.
        # Druga liczba to ilość trafionych stron.
        # Trzecia liczba to ilość brakujących stron.
        # Konwertujemy powyższe wartości na typ całkowity.
        for element in lines:
            list_of_results.append([int(element[0]), int(element[2]), int(element[3])])

    # Zwracamy listę powyższych wartości
    return list_of_results


# Funkcja zapisująca do pliku zestawienie ilości ramek z ilością trafionych
# i brakujących stron.
def write_summary_of_pages(number_of_frames):

    # Wywołanie funkcji do odczytu pliku z wynikami poszczególnych
    # algorytmów, które zostaną zwrócone w postaci listy trzyelementowej.
    first_algorithm = read_summary_of_pages('fifo', number_of_frames)
    second_algorithm = read_summary_of_pages('lru', number_of_frames)

    # Zapisujemy do pliku listę z wynikami zestawienia.
    # - Kolumna nr 1: liczba ramek od 1 do 20.
    # - Kolumna nr 2: liczba trafionych stron podczas przeprowadzania
    # symulacji zgodnie z algorytmem FIFO.
    # - Kolumna nr 3: liczba brakujących stron podczas przeprowadzania
    # symulacji zgodnie z algorytmem FIFO.
    # - Kolumna nr 4: liczba trafionych stron podczas przeprowadzania
    # symulacji zgodnie z algorytmem LRU.
    # - Kolumna nr 5: liczba brakujących stron podczas przeprowadzania
    # symulacji zgodnie z algorytmem LRU.
    with open(f"results/summary_by_memory.txt", "a") as file:
        file.write(f"{first_algorithm[0][0]} {first_algorithm[0][1]} {first_algorithm[0][2]} "
                   f"{second_algorithm[0][1]} {second_algorithm[0][2]}\n")

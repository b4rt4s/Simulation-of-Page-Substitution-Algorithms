# Program "test_data_read.py" odczytuje dane testowe w postaci
# ciągu odwołań do stron, który będzie wykorzystany przez programy
# implementujące działanie algorytmów zastępowania stron
# do wykonania symulacji.

# Funkcja "read_data" to funkcja odczytująca dane testowe z plików tekstowych.
def read_data():

    # Otworzenie pliku z danymi testowymi.
    with open("test_data/test_data.txt") as file:

        # Utworzenie pustej listy, w której umieścimy ciąg odwołań do stron.
        list_of_test_data = []

        # Zapis danych testowych do pustej listy, której elementami
        # są składowe ciągu odwołań do stron.
        # Każda składowa ciągu to numer strony.
        for page in file:
            list_of_test_data.append(int(page))

    return list_of_test_data

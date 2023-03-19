# Program "main.py" zarządza procesem całej symulacji.
# Krótko mówiąc, łączy ze sobą wszystkie pliki w jedną całość.

# Importowanie modułów plików projektu.
import test_data_create
import test_data_read
import algorithm_fifo
import algorithm_lru
import write_results
import summary_by_memory

# Importowanie modułu "os", który pozwala m.in. na usuwanie pliku.
import os

# Usunięcie pliku z wygenerowanymi danymi przy każdym nowym załadowaniu programu.
if os.path.isfile("test_data/data_for_page_substituion_solver.txt"):
    os.unlink("test_data/data_for_page_substituion_solver.txt")

# Usunięcie pliku z wygenerowanymi danymi przy każdym nowym załadowaniu programu.
if os.path.isfile("results/summary_by_memory.txt"):
    os.unlink("results/summary_by_memory.txt")

# Utworzenie danych potrzebnych do wykonania pojedynczej symulacji.
test_data_create.create_data()

# Przeprowadzenie 20 symulacji zastępowania stron dla 20 różnych wielkości ramek.
for number_of_frames in range(1, 21):

    # Odczyt danych i wykonanie symulacji zastępowania stron zgodnie z odpowiednimi algorytmami.
    read_and_perform_simulation1 = algorithm_fifo.fifo(number_of_frames, test_data_read.read_data())
    read_and_perform_simulation2 = algorithm_lru.lru(number_of_frames, test_data_read.read_data())

    # Zapis do odpowiednich plików wyników uzyskanych dla obu algorytmów.
    write_results.writing_to_file(read_and_perform_simulation1, number_of_frames, 'fifo')
    write_results.writing_to_file(read_and_perform_simulation2, number_of_frames, 'lru')

    # Zapis do pliku zestawienia składającego się z rozmiarów
    # pamięci oraz liczby trafionych i brakujących stron dla
    # obu algorytmów zastępowania stron.
    # Zestawienie jest zapisane w pliku "summary_by_memory" w folderze "results".
    summary_by_memory.write_summary_of_pages(number_of_frames)

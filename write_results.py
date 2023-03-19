# Program "write_results.py" dla danego zestawu danych pochodzących
# z jednej przeprowadzonej symulacji danego algorytmu zapisuje je w pliku
# "algorithm_{name}_results/algorithm_{name}_results{i}.txt",
# gdzie {name} oznacza nazwę algorytmu FIFO lub LRU, a {i} to numer
# od 1 do 20. Dokładniej mówiąc, zapisuje dane (liczby) w 1 linii. Poszczególne
# liczby są oddzielone znakiem spacji. Łącznie jest ich sześć i prezentują
# się następująco:
# 1. całkowita ilość ramek,
# 2. długość ciągu odwołań do stron,
# 3. ilość stron, których nie było w pamięci podczas przeprowadzania symulacji,
# 4. ilość stron, które były w pamięci podczas przeprowadzania symulacji,
# 5. wskaźnik procentowy stron trafionych,
# 6. wskaźnik procentowy stron brakujących.

# Funkcja zapisująca wyniki przeprowadzonych symulacji do plików.
def writing_to_file(list_of_results, number_of_frames, name):

    # Utworzenie pliku tekstowego w odpowiednim folderze, do którego zapiszemy
    # dane wygenerowane przez użyty algorytm.
    with open(f"algorithm_{name}_results/algorithm_{name}_results{number_of_frames}.txt", "w") as file:

        # Zapisujemy do pliku listę z wynikami danego przeprowadzonego algorytmu.
        file.write(f"{list_of_results[0][0]} {list_of_results[0][1]} {list_of_results[0][2]} "
                   f"{list_of_results[0][3]} {list_of_results[0][4]*100} {list_of_results[0][5]*100}\n")

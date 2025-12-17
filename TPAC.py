import time

############################################################
# QUESTION 1 – Lecture du fichier
# Lire les valeurs du fichier valeurs_aleatoires.txt
# Stocker les valeurs dans une liste values_list
############################################################

def read_file(filename):
    values_list = []
    with open(filename, "r") as file:
        for line in file:
            values_list.append(int(line.strip()))
    return values_list


############################################################
# QUESTION 2 – Nombre d'occurrences (version lente)
# Utiliser une boucle imbriquée + dictionnaire
# Déterminer le nombre exact d’itérations
# Complexité : O(n²)
############################################################

def nombre_occurrences(values_list):
    occurrences = {}
    iterations = 0

    for i in range(len(values_list)):
        count = 0
        for j in range(len(values_list)):   # boucle imbriquée
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
        occurrences[values_list[i]] = count

    return occurrences, iterations


############################################################
# QUESTION 4 – Amélioration du calcul des occurrences
# Objectif : réduire la complexité de O(n²) → O(n)
############################################################

def nombre_occurrences_ameliore(values_list):
    occurrences = {}
    iterations = 0

    for value in values_list:
        iterations += 1
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    return occurrences, iterations


############################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
# - Trie les éléments en ordre croissant
# - Affiche le nombre d’itérations
# - Affiche la complexité (O(n²))
# - Intègre un chronomètre
############################################################

def selection_sort(arr):
    n = len(arr)
    iterations = 0
    start_time = time.time()

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            iterations += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.time()
    duration = end_time - start_time

    return arr, iterations, duration


############################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
# - Trie les éléments en ordre croissant
# - Compte les itérations
# - Affiche la complexité : O(n log n)
# - Intègre un chronomètre
############################################################

merge_iterations = 0

def merge_sort(tab):
    global merge_iterations

    if len(tab) <= 1:
        return tab

    merge_iterations += 1

    mid = len(tab) // 2
    left = merge_sort(tab[:mid])
    right = merge_sort(tab[mid:])

    return merge(left, right)


def merge(left, right):
    global merge_iterations
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        merge_iterations += 1
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


############################################################
# QUESTION 7 – Sauvegarde du tableau trié
############################################################

def write_to_file(filename, values):
    with open(filename, "w") as file:
        for v in values:
            file.write(str(v) + "\n")


############################################################
# PROGRAMME PRINCIPAL
############################################################

if name == "main":
   print("\n================= LECTURE DU FICHIER =================")
    values_list = read_file("valeurs_aleatoires.txt")
    
print("Fichier chargé avec succès !\n")

    print("================= OCCURRENCES (version lente) =================")
    occ_slow, it_slow = nombre_occurrences(values_list)
    print(f"Nombre d’itérations : {it_slow}")
    print("Complexité : O(n²)\n")

    print("================= OCCURRENCES AMÉLIORÉES =================")
    occ_fast, it_fast = nombre_occurrences_ameliore(values_list)
    print(f"Nombre d’itérations : {it_fast}")
    print("Complexité : O(n)\n")

    print("================= SELECTION SORT =================")
    sorted_sel, it_sel, time_sel = selection_sort(values_list.copy())
    print(f"Tri par sélection terminé.")
    print(f"Nombre d’itérations : {it_sel}")
    print(f"Durée d’exécution : {time_sel:.6f} sec")
    print("Complexité : O(n²)\n")

    print("================= MERGE SORT =================")
    global merge_iterations
    merge_iterations = 0
    start_merge = time.time()
    sorted_merge = merge_sort(values_list.copy())
    end_merge = time.time()

    print(f"Tri par fusion terminé.")
    print(f"Nombre d’itérations : {merge_iterations}")
    print(f"Durée d’exécution : {end_merge - start_merge:.6f} sec")
    print("Complexité : O(n log n)\n")

    print("================= SAUVEGARDE =================")
    write_to_file("valeurs_aleatoires_tries.txt", sorted_merge)
    print("Fichier valeurs_aleatoires_tries.txt créé avec succès !")
def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(n - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
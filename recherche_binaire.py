def recherche_binaire(arr, valeur):
    debut = 0
    fin = len(arr) - 1
    while debut <= fin:
        milieu = debut + (fin - debut) // 2
        if arr[milieu] == valeur:
            return milieu
        elif arr[milieu] < valeur:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

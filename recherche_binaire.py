def recherche_binaire(arr, x, debug=False):
    # Modifications par Marie
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if debug:
                print(f'Trouvé à l'index {mid}')
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    if debug:
        print('Non trouvé')
    return -1

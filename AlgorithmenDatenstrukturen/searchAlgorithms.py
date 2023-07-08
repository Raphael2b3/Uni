def binarySearch(liste, element):
    first = 0
    last = len(liste)
    i = None
    while first <= last and i is not None:
        mid = first + (last - first) // 2
        if liste[mid] < element:
            first = mid + 1
        elif liste[mid]> element:
            last = mid -1
        else:
            i = mid
    return i

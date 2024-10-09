def summa(some_list):
    if some_list == []:
        return 0
    else:
        return some_list[0] + summa(some_list[1:])


def len_list(some_list):
    if some_list == []:
        return 0
    else:
        return  1 + len_list(some_list[1:])
   

def max_el(some_list):
    if len(some_list) == 2:
        return some_list[0] if some_list[0] > some_list[1] else some_list[1]
    sub_max_el = max_el(some_list[1:])
    return some_list[0] if some_list[0] > sub_max_el else sub_max_el


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



print(summa([2, 4, 6]))
print(len_list([2, 4, 6, 3]))
print(max_el([26, 4, 6, 3, 25, 12]))
print(quicksort([26, 4, 6, 3, 25, 1]))
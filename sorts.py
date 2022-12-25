import random
from heapsort import heap_sort
from math import log2


def bubble_sort(list1):
    has_swapped = True

    while has_swapped:
        has_swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    return list1


def cocktail_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1
    return a


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr


def selection_sort(mylist):
    # Traverse through all list elements
    for i in range(len(mylist)):

        # Searching the minimum element in remaining unsorted list
        min_pos = i
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[min_pos]:
                min_pos = j

        # Swap the found minimum element with the first element
        temp = mylist[i]
        mylist[i] = mylist[min_pos]
        mylist[min_pos] = temp
    return mylist


def comb_sort(number):
    dist = len(number)
    swap = True
    while dist > 1 or swap:
        dist = max(1, int(dist / 1.25))
        swap = False
        for a in range(len(number) - dist):
            b = a + dist
            if number[a] > number[b]:
                number[a], number[b] = number[b], number[a]
                swap = True
    return number


def shell_sort(inp):
    h = len(inp) // 2
    while h > 0:
        for i in range(h, len(inp)):
            t = inp[i]
            j = i
            while j >= h and inp[j - h] > t:
                inp[j] = inp[j - h]
                j -= h

            inp[j] = t
        h = h // 2
    return inp


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def partition(array, begin, end, *, reverse=False):
    pivot_idx = random.randint(begin, end)
    pivot = array[pivot_idx]

    array[end], array[pivot_idx] = array[pivot_idx], array[end]
    first_larger = begin
    for idx in range(begin, end):
        if reverse ^ (array[idx] <= pivot):
            array[idx], array[first_larger] = array[first_larger], array[idx]
            first_larger += 1

    array[end], array[first_larger] = array[first_larger], array[end]
    return first_larger


def intro_sort(array, begin=0, end=None, depth=0):
    if end is None:
        end = len(array) - 1

    if depth < log2(len(array)):
        if begin < end:
            mid = partition(array, begin, end)
            intro_sort(array, begin, mid - 1, depth + 1)
            intro_sort(array, mid + 1, end, depth + 1)
    else:
        heap_sort(array[begin:end + 1])
    return array


def counting_sort(input_array):
    max_element = max(input_array)
    min_element = min(input_array)
    count_array = dict.fromkeys([i for i in range(min_element, max_element + 1)], 0)
    for el in input_array:
        count_array[el] += 1
    for i in range(min_element + 1, max_element + 1):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(input_array)
    i = len(input_array) - 1
    while i >= 0:
        current_el = input_array[i]
        count_array[current_el] -= 1
        new_position = count_array[current_el]
        output_array[new_position] = current_el
        i -= 1

    return output_array

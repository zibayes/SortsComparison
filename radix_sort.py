from sorts import counting_sort


def counting_sort_for_radix(input_array, place_value):
    count_array = [0] * 10
    input_size = len(input_array)
    for i in range(input_size):
        place_element = (input_array[i] // place_value) % 10
        count_array[place_element] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    output_array = [0] * input_size
    i = input_size - 1
    while i >= 0:
        current_el = input_array[i]
        place_element = (input_array[i] // place_value) % 10
        count_array[place_element] -= 1
        new_position = count_array[place_element]
        output_array[new_position] = current_el
        i -= 1

    return output_array


def radix_sort(input_array):
    max_el = max(input_array)

    D = 1
    while max_el > 0:
        max_el /= 10
        D += 1

    place_val = 1
    output_array = input_array
    while D > 0:
        output_array = counting_sort_for_radix(output_array, place_val)
        # output_array = counting_sort(output_array)
        place_val *= 10
        D -= 1

    result = next((output_array.index(x) for x in output_array if x < 0), None)
    if result is not None:
        return output_array[result:] + output_array[:result]
    return output_array

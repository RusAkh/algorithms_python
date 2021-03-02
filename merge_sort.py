inversion_counter = 0       # ADDITIONAL inversion counter


def merge_sort(array):
    if len(array) <= 1:         # base case
        return array

    midpoint = int(len(array) / 2)
    left_part, right_part = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])      # recursively divide in half
    print(left_part, right_part)        # just visual
    return merge(left_part, right_part)     # apply merging step


def merge(left, right):
    global inversion_counter        # ADDITIONAL counter for inversions in array
    result = []
    l_iter = r_iter = 0
    while l_iter < len(left) and r_iter < len(right):       # while there are elements left in both left n right arrays
        if left[l_iter] < right[r_iter]:
            result.append(left[l_iter])         # if left - [0] < right - [1]   append smaller one to resulting array
            l_iter += 1     # move pointer
        else:
            result.append(right[r_iter])
            inversion_counter += len(left[l_iter:])         # oof I can not explain this in comment, hope u get it
            r_iter += 1         # move pointer

    result.extend(left[l_iter:])        # something is left somewhere, add the remaining
    result.extend(right[r_iter:])       # something is left somewhere, add it

    return result


print(merge_sort([1, 5, 7, 6, 4, 8, 12]))
print('inversions:', inversion_counter)

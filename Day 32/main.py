def sort_array(source_array):
    odd_nums = sorted(x for x in source_array if x % 2 != 0)

    return [odd_nums.pop(0) if num % 2 != 0 else num for num in source_array]


list = [5, 8, 6, 3, 4]

print(sort_array(list))
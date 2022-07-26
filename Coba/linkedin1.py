def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_alpha_nums(['a','b','c'], [1,2,3])
print_alpha_nums(['e,','f','g','h'], [4,5,6])
def uneven_remover(list):
    even_nums = [num for num in list if num % 2 == 0]
    return even_nums

def main():
    list = [1,2,3,4,5,6,7,8,9]
    new_list = uneven_remover(list)
    print(f"The original list is {list}")
    print(f"The cut-down list is {new_list}")

main()
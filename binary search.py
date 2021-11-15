def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    
    while left_index <= right_index :
        middle_index = (left_index + right_index)//2
        if numbers_list[middle_index] == number_to_find:
            return middle_index
        if numbers_list[middle_index] < number_to_find:
            left_index = middle_index + 1
        if numbers_list[middle_index] > number_to_find:
            right_index = middle_index -1
    return -1



if __name__ == '__main__':
    numbers_list = [12,15,17,19,21,24,45,67]
    number_to_find = 45
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at {index} using binary search")
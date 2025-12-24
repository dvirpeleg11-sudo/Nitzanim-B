# # warming exercises
#
# alist = []
#
# for i in range(5):
#     # input a number
#     print("Enter num: ")
#     num = int(input())
#
#     # add the number to the list
#     alist.append(num)
#
# print(alist)
#
# for i in range(len(alist) - 1, -1, -1):
#     print(i)
#
# alist_sum = 0
#
# for num in alist:
#     alist_sum += num
#
# avg = alist_sum / len(alist)
# print(avg)
#
# for num in alist:
#     if num % 2 == 0:
#         print(num)
#
# maximum_value = alist[0]
#
# for i in range(1, len(alist)):
#     if alist[i] > maximum_value:
#         maximum_value = alist[i]
#
# print(maximum_value)
#
# # task 1
#
# import random
#
# numbers = []
#
# for i in range(100):
#     rand_num = random.randint(1, 1000)
#     numbers.append(rand_num)
#
# even_numbers = []
# odd_numbers = []
#
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
#
# print("the lengths of each list:")
# print(len(numbers))
# print(len(even_numbers))
# print(len(odd_numbers))
#
# print("the average value in each list:")
# print(sum(numbers) / len(numbers))
# print(sum(even_numbers) / len(even_numbers))
# print(sum(odd_numbers) / len(odd_numbers))
#
# # task 2
#
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
#
# matrix_sum = 0
#
# for row in matrix:
#     for col in row:
#         matrix_sum += col
#
# row_sum = []
#
# for row in matrix:
#     current_row_sum = 0
#     for col in row:
#         current_row_sum += col
#     row_sum.append(current_row_sum)
#
# col_sum = []
#
# for i in range(len(matrix[0])):
#     current_column_sum = 0
#     for row in matrix:
#         current_column_sum += row[i]
#     col_sum.append(current_column_sum)

# task 4

X = 'X'
O = 'O'
matrix = [
    [O, O, X, X, X],
    [X, O, X, X, X],
    [X, O, O, O, X],
    [X, X, X, O, X],
    [X, X, X, O, O]
]

counter = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        currentValue = matrix[row][col]
        if currentValue == O:
            print(f"{counter}({row}, {col})")
            counter+=1

# task 5

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if row == 0 or row == len(matrix) - 1:
            print(matrix[row][col], end= " ")
        elif col == 0 or col == len((matrix[row])) - 1:
            print(matrix[row][col], end= " ")
        else:
            print(end= "  ")
    print()
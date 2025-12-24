# task 1

# import random
#
# def create_list():
#     numbers = []
#
#     for i in range(100):
#         rand_num = random.randint(1, 1000)
#         numbers.append(rand_num)
#
#     return numbers
#
# def create_even_and_odd_lists(numbers):
#     even_numbers = []
#     odd_numbers = []
#
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#
#     return even_numbers, odd_numbers
#
# def print_length_of_lists(numbers, even_numbers, odd_numbers):
#     print("the lengths of each list:")
#     print(len(numbers))
#     print(len(even_numbers))
#     print(len(odd_numbers))
#
# def print_average_of_lists(numbers, even_numbers, odd_numbers):
#     print("the average value in each list:")
#     print(sum(numbers) / len(numbers))
#     print(sum(even_numbers) / len(even_numbers))
#     print(sum(odd_numbers) / len(odd_numbers))
#
# def main():
#     numbers = create_list()
#     even_numbers, odd_numbers = create_even_and_odd_lists(numbers)
#     print_length_of_lists(numbers, even_numbers, odd_numbers)
#     print_average_of_lists(numbers, even_numbers, odd_numbers)
#
# main()

# task 2

# def get_matrix_sum(matrix):
#     matrix_sum = 0
#
#     for row in matrix:
#         for col in row:
#             matrix_sum += col
#     return matrix_sum
#
# def get_rows_sum(matrix):
#     row_sum = []
#
#     for row in matrix:
#         current_row_sum = 0
#         for col in row:
#             current_row_sum += col
#         row_sum.append(current_row_sum)
#
#     return row_sum
#
# def get_cols_sum(matrix):
#     col_sum = []
#
#     for col_i in range(len(matrix[0])):
#         current_column_sum = 0
#         for row in matrix:
#             current_column_sum += row[col_i]
#         col_sum.append(current_column_sum)
#
#     return col_sum
#
# def main():
#     matrix = [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#         [21, 22, 23, 24, 25]
#     ]
#     matrix_sum = get_matrix_sum(matrix)
#     matrix_rows_sum = get_rows_sum(matrix)
#     matrix_cols_sum = get_cols_sum(matrix)
#
# main()

# task 3



# task 4

# def input_two_number():
#     x1 = int(input("Enter first number: "))
#     x2 = int(input("Enter second number: "))
#     return x1, x2
#
# def add():
#     x1, x2 = input_two_number()
#     print(x1 + x2)
#
# def subtract():
#     x1, x2 = input_two_number()
#     print(x1 - x2)
#
# def multiply():
#     x1, x2 = input_two_number()
#     print(x1 * x2)
#
# def divide():
#     x1, x2 = input_two_number()
#     print(x1 / x2)
#
# def calculator():
#
#     function = " "
#
#     while function.lower() != "exit":
#
#         print("""
#         Add .1
#         Subtract .2
#         Multiply .3
#         Divide .4
#         Exit .5
#         """)
#         function = input("Enter function you want to do or EXIT if you want to exit: ")
#
#         if function.lower() == "add":
#             add()
#         elif function.lower() == "subtract":
#             subtract()
#         elif function.lower() == "multiply":
#             multiply()
#         elif function.lower() == "divide":
#             divide()
#         elif function.lower() == "exit":
#             break
#         else:
#             print("not a valid input. please look again at the menu.")
#
#     print("you typed exit, so now the system has closed. have a nice day!")
#
# def main():
#     calculator()
#
# main()

# task 5

# def add_and_sort(sorted_names, user_input):
#
#     user_input_length = len(user_input)
#
#     if not sorted_names:
#
#         sorted_names.append(user_input)
#         return sorted_names
#
#     for index, name in enumerate(sorted_names):
#         if user_input_length < len(name):
#             sorted_names.insert(index, user_input)
#             return sorted_names
#
#     sorted_names.append(user_input)
#     return sorted_names
#
# def input_some_names():
#
#     sorted_names = []
#     user_input = input("Enter name: ")
#
#     while user_input.lower() != "stop":
#
#         sorted_names = add_and_sort(sorted_names, user_input)
#         user_input = input("Enter another name: ")
#
#     print("The sorted list of names is: ")
#     for name in sorted_names:
#         print(name, end= ", ")
#
# def main():
#     input_some_names()
#
# main()

# task 6
# import random
#
# def play_guesses():
#
#     number = random.randint(1, 100)
#     guess = number - 1
#
#     while guess != number:
#
#         guess = int(input("Enter your guess: "))
#         if guess > number:
#             print("Too high")
#         elif guess < number:
#             print("Too low")
#
#     print("You got this! well done.")
#
# def main():
#     play_guesses()
#
# main()

# taks 7
# def input_valid_number():
#
#     while True:
#         user_input = input("Enter number: ")
#         try:
#             user_input = int(user_input)
#             if user_input > 0:
#                 return user_input
#             else:
#                 print("Please enter a positive number above zero.")
#
#         except:
#             print("Please enter a number.")
#
# def print_seven_boom(number):
#     for num in range(1, number):
#         if num % 7 == 0 or num % 10 == 7:
#             print("BOOM")
#         else:
#             print(num)
#
# def main():
#     number = input_valid_number()
#     print_seven_boom(number)
#
# main()

# task 8

# def is_len_eight_minimum(password):
#     if len(password) >= 8:
#         return True
#     return False
#
# def is_contain_num(password):
#     for tav in password:
#         if tav.isdigit():
#             return True
#     return False
#
# def is_contain_upper(password):
#     for tav in password:
#         if tav.isupper():
#             return True
#     return False
#
# def main():
#     password = input("Enter password: ")
#     if not is_len_eight_minimum(password):
#         print("The password doesnt have 8 tavs in it or more.")
#     elif not is_contain_num(password):
#         print("The password doesnt contain number in it.")
#     elif not is_contain_upper(password):
#         print("The password doesnt contain a capital letter in it.")
#     else:
#         print("The password is valid!")
#
# main()
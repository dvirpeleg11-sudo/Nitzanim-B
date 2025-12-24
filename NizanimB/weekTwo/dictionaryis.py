# def menu(dictionary):
#     print("Enter 1 if you want to add a name."
#           "2 if you want to remove a name."
#           "3 if you want to look for a phone number by a specific name."
#           "")
#     choose = input()
#
#     while choose.lower() != "exit":
#
#         if choose == "1":
#
#             print("Enter name: ")
#             name = input()
#
#             print("Enter phone number: ")
#             number = input()
#
#             dictionary[name] = number
#
#         elif choose == "2":
#
#             print("Enter name:")
#             name = input()
#
#             dictionary.pop(name)
#
#         elif choose == "3":
#
#             print("Enter name:")
#             name = input()
#
#             if name in dictionary:
#                 print(f"the phone number of {name} is {dictionary[name]}.")
#             else:
#                 print(f"the name {name} is not in the dictionary.")
#
#         print("Enter 1 if you want to add a name."
#               "2 if you want to remove a name."
#               "3 if you want to look for a phone number by a specific name."
#               "")
#         choose = input()
#
#     print(f"the dict is {dictionary}.")
#
# def main():
#     dictionary = dict()
#     menu(dictionary)
#
# if __name__ == '__main__':
#     main()

# def add_three_products(shopping_cart):
#
#     for i in range(3):
#         print("Enter product: ")
#         product = input()
#
#         print("Enter quantity: ")
#         quantity = int(input())
#
#         shopping_cart[product] = quantity
#
#     return shopping_cart
#
# def print_items(shopping_cart):
#     for key, value in shopping_cart.items():
#         print(key, value)
#
# def main():
#     shopping_cart = {}
#     shopping_cart = add_three_products(shopping_cart)
#     print_items(shopping_cart)
#
# main()

# # task 1
# def print_dict(dictionary):
#
#     result = []
#     for key, value in dictionary.items():
#         result.append((key, value))
#
#     print(result)
#
# def main():
#     dictionary = {}
#     print_dict(dictionary)
#
# main()
#
# # task 2
# def add_dict(dictionary, dict_to_add):
#
#     for key, value in dict_to_add.items():
#         dictionary[key] = value
#
#     return dictionary
#
# def main():
#     dictionary = {}
#     dict_to_add = {}
#     res = add_dict(dictionary, dict_to_add)
#     print(res)
#
# main()
#
# # task 3
# def create_keys_by_two_lists(keys, values):
#     final_dict = {}
#     for i in range(len(keys)):
#         final_dict[keys[i]] = values[i]
#
#     return final_dict
#
# def main():
#     keys = ["dvir", "sagi"]
#     values = [1, 2]
#     res = create_keys_by_two_lists(keys, values)
#     print(res)
#
# main()

# # task 4
#
# def in_dict(dictionary, number):
#     for key in dictionary.keys():
#         if number == key:
#             return True
#
#     return False
#
# def create_dict_with_stars():
#
#     dictionary = {}
#     for i in range(7):
#         number = int(input("Enter number: "))
#
#         if in_dict(dictionary, number):
#             dictionary[number] = (number + 1) * "*"
#         else:
#             dictionary[number] = number * "*"
#
#     return dictionary
#
# def main():
#     empty_dict = {}
#     dictionary = create_dict_with_stars()
#     print(dictionary)
#
# main()
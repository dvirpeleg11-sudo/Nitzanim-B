# # warming up
#
# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}
#
# print(set_b.intersection(set_a))

# # task 1
#
# def create_sets():
#
#     set_a = set()
#     set_b = set()
#
#     user_input = input("Enter num or DONE: ")
#
#     while user_input.lower() != "done":
#         set_a.add(user_input)
#         user_input = input("Enter num or DONE: ")
#
#     user_input = input("Enter num or DONE: ")
#
#     while user_input.lower() != "done":
#         set_b.add(user_input)
#         user_input = input("Enter num or DONE: ")
#
#     return set_a, set_b
#
# def main():
#     set_a, set_b = create_sets()
#     print(set_a.union(set_b))
#
# main()

# task 2

# def create_sets():
#
#     set_a = set()
#     set_b = set()
#
#     user_input = input("Enter num or DONE: ")
#
#     while user_input.lower() != "done":
#         set_a.add(user_input)
#         user_input = input("Enter num or DONE: ")
#
#     user_input = input("Enter num or DONE: ")
#
#     while user_input.lower() != "done":
#         set_b.add(user_input)
#         user_input = input("Enter num or DONE: ")
#
#     return set_a, set_b
#
# def print_a_specials(intersected_set, set_b):
#     for value in intersected_set:
#         if value not in set_b:
#             print(value)
#
# def main():
#     set_a, set_b = create_sets()
#     intersected_set = (set_a.union(set_b))
#     print_a_specials(intersected_set, set_b)
#
# main()
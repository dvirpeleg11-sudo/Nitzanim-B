import random

# functions task 1

def input_field_size():

    print("Enter number of rows in the field: ")
    rows = int(input())

    print("Enter number of coloumns in the field: ")
    cols = int(input())

    return rows, cols

def create_parking_field(rows, cols, possible_names):
    parking_field = []
    for i in range(rows):
        current_row = []
        for j in range(cols):
            rand_name = random.choice(possible_names)
            current_row.append(rand_name)
        parking_field.append(current_row)
    return parking_field

def print_parking_field(parking_field):
    for row in parking_field:
        print(row)

# functions task 2

def print_count_appearnce_of_car(parking_field, car_name):
    for row in parking_field:
        counter = 0
        for col in row:
            if col == car_name:
                counter += 1
        print(f"In row number {parking_field.index(row) + 1}, there are {counter} cars with the name {car_name}.")

def count_empties_in_odd_cols(parking_field):
    for col_index in range(1, len(parking_field[0]), 2):
        count_empties = 0
        for row in parking_field:
            if row[col_index] is None:
                count_empties += 1
        print(f"In coluomn number {col_index}, there are {count_empties} empty places.")

# functions task 3

def get_count_appearnce_of_car(parking_field, car_name):

    counter = 0
    for row in parking_field:
        for col in row:
            if col == car_name:
                counter += 1
    return counter

def count_appearnce_of_each_car(parking_field, possible_names):

    appearnce_of_each_car = {}
    possible_names.remove(None)

    for name in possible_names:
        appearnce_of_each_car[name] = get_count_appearnce_of_car(parking_field, name)

    return appearnce_of_each_car

def sort_values(appearnce_of_each_car):
    values = []
    for value in appearnce_of_each_car.values():
        values.append(value)
    values = sorted(values)
    return values

def sort_keys_like_values(appearnce_of_each_car, sorted_values):

    new_dict = {}

    for value in sorted_values:
        for key in appearnce_of_each_car.keys():
            if appearnce_of_each_car[key] == value:
                new_dict[key] = value
    return new_dict

def print_top_three(appearnce_of_each_car):

    print("Top 3 brands in the parking Lot:")
    for i in range(3):
        keys = appearnce_of_each_car.keys()
        keys = list(keys)
        keys.reverse()
        print(f"{keys[i]} {appearnce_of_each_car[keys[i]]}")

# functions task 4

def create_sets(first_parking_field, second_parking_field):

    set_first_parking_field = set()
    set_second_parking_field = set()

    for row in first_parking_field:
        for col in row:
            if not (col is None):
                set_first_parking_field.add(col)

    for row in second_parking_field:
        for col in row:
            if not (col is None):
                set_second_parking_field.add(col)

    return set_first_parking_field, set_second_parking_field

# functions for bonus

def create_field_from_two_fields(parking_field, second_parking_field):
    result = parking_field
    for row_index in range(len(parking_field)):
        for col_index in range(len(parking_field[row_index])):
            if parking_field[row_index][col_index] is None and second_parking_field[row_index][col_index] is None:
                result[row_index][col_index] = None
            elif parking_field[row_index][col_index] is None and not (second_parking_field[row_index][col_index] is None):
                result[row_index][col_index] = second_parking_field[row_index][col_index]
            elif not (parking_field[row_index][col_index] is None) and (second_parking_field[row_index][col_index] is None):
                result[row_index][col_index] = parking_field[row_index][col_index]
            else:
                result[row_index][col_index] = "X"

    return result

# main function

def main():

    # task 1
    print("task 1:")
    possible_names = [None, "TOY", "BMW", "TES", "KIA", "HYU"]
    rows, cols = input_field_size()
    parking_field = create_parking_field(rows, cols, possible_names)
    print_parking_field(parking_field)
    print()

    # task 2
    print("Task 2:")
    apperance_in_all_rows = print_count_appearnce_of_car(parking_field, "TES")
    count_empties_in_odd_cols(parking_field)

    print("Task 3:")
    appearnce_of_each_car = count_appearnce_of_each_car(parking_field, possible_names)
    print(appearnce_of_each_car)
    sorted_values = sort_values(appearnce_of_each_car)
    appearnce_of_each_car = sort_keys_like_values(appearnce_of_each_car, sorted_values)
    print_top_three(appearnce_of_each_car)
    print()

    print("Task 4:")
    rows, cols = input_field_size()
    second_parking_field = create_parking_field(rows, cols, possible_names)
    print_parking_field(second_parking_field)
    set_first_parking_field, set_second_parking_field = create_sets(parking_field, second_parking_field)

    union_set = set_first_parking_field.union(set_second_parking_field)

    common_car_names = set_first_parking_field.union(set_second_parking_field)
    print("the common cars names of the two parking field are:")
    print(common_car_names)

    print("the union cars that apears only in the first field are: ")
    print(common_car_names - set_second_parking_field)
    print()

    # Bonus
    print("Bonus:")
    result = create_field_from_two_fields(parking_field, second_parking_field)
    print(result)

main()
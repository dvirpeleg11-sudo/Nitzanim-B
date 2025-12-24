def matrix_square_make(num):
    matrix = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(0)
        matrix.append(row)

    return matrix

def show_problems_in_television(television_pixels):
    problems = []
    for row in range(len(television_pixels)):
        for col in range(len(television_pixels[row])):
            if television_pixels[row][col] == "problem":
                problems.append((row, col))

    return problems

def avg_two_d_list(two_d_list):

    number_of_values = 0
    sum_of_values = 0

    for row in two_d_list:
        for col in row:
            number_of_values += 1
            sum_of_values += col

    return sum_of_values / number_of_values

def get_half_value(two_d_list):
    united_list = []
    for row in two_d_list:
        for col in row:
            united_list.append(col)

    united_list.sort()
    half_value_index = len(united_list) // 2
    return united_list[half_value_index]

def shift(alist, moves):

    shifted_list = []
    moves %= len(alist)

    # add the vlaues from moves up until the end of the alist
    for i in range(moves, len(alist)):
        shifted_list.append(alist[i])

    # add the values from the first up until moves
    for i in range(moves):
        shifted_list.append(alist[i])

    return shifted_list

def main():

    # warm up
    # print("warm up:")
    # matrix = matrix_square_make(2)
    # print(matrix)

    # task 1
    # print("task 1:")
    # problems = show_problems_in_television([["problem", "work"], ["problem", "problem"]])
    # print(problems)

    # task 2
    # print("task 2:")
    # avg = avg_two_d_list([[1, 2, 3], [1, 4, 7]])
    # print(avg)
    # half_value = get_half_value([[1, 2, 3], [1, 4, 7]])
    # print(half_value)

    # task 3
    # print("task 3:")
    # shifted_list = shift([1,2,3,4,5,6], 2)
    # print(shifted_list)



main()
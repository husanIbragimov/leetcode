def check_sum(matrix):
    for i in range(3):
        for j in range(3):
            # print(matrix[i], "test")
            square_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if square_sum != 10:
                return False
    return True

def check_sum_me(matrix):
    # print(matrix)
    index = []


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def solve_puzzle(filename):
    with open(filename, 'r') as file:
        data = [list(map(int, line.split())) for line in file]
        # print(data)

    solutions = []

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    matrix = [
                        data[i], data[j],
                        data[k], data[l]
                    ]
                    print(matrix)
                    if check_sum(matrix):
                        solutions.append(matrix)

                    # if check_sum_me(matrix):
                    #     solutions.append(matrix)

    for solution in solutions:
        print_matrix(solution)
        print(solution)


solve_puzzle('input.txt')



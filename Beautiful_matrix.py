def find_one_position(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                print(i, j)


def calculate_moves_to_center(one_pos):
    center_pos = (2, 2)
    return abs(one_pos[0] - center_pos[0]) + abs(one_pos[1] - center_pos[1])


matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))


one_pos = find_one_position(matrix)

print(calculate_moves_to_center(one_pos))

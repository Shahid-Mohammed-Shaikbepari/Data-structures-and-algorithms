def rotate( matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    Approach:
    1. calculate number of layers = n-1
    2. iterate for number of layers and move items circularly
    3. for 3x3 matrix, (0, 0) goes to (0, 2), (0, 2)--> (2, 2); (2, 2) --> (2, 0); (2, 0)--> (0, 0) this for layer 1
    4. for layer 2, (0, 1) --> (1, 2); (1, 2) --> (2, 1) ; (2, 1) --> (1, 0); (1, 0) --> (0, 1)

    """

    def process( s_row, s_col):
        nonlocal N
        e_col = e_row = N - 1 - s_row
        for i in range(n - 1):
            temp = matrix[s_row][s_col + i]
            # step 1
            matrix[s_row][s_col + i] = matrix[e_row - i][s_col]
            # step 2
            matrix[e_row - i][s_col] = matrix[e_row ][e_col-i]
            # step 3
            matrix[e_row ][e_col - i] = matrix[s_row+i][e_col]
            # step 4
            matrix[s_row+i][e_col] = temp

    N = n = len(matrix)
    row = col = 0
    n = 3
    while n:
        process( row, col)

        n //= 2
        row += 1
        col += 1
    # while n:
    #     process(n, row, col)
    #
    #     n //= 2
    #     row += 1
    #     col += 1
    print(matrix)


matrix = [[1,2,3, 10],[4,5,6, 11],[7,8,9, 12], [13, 14, 15, 16]]
mat1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(rotate(mat1))

def num_of_paths_to_dest(n):
    if n < 1:
        return n
    memo = [[-1]*n for i in range(n)]

    r = c = 0
    memo[n-1][n-1] = 1

    def backtrack(r, c):
        if r >= n or c >= n or r < c:
            return 0


        if memo[r][c] != -1:
            return memo[r][c]

        memo[r][c] = backtrack(r+1, c) + backtrack(r, c+1)
        return memo[r][c]

    backtrack(r, c)
    return memo[0][0]


res = num_of_paths_to_dest(4)
print(res)

# def num_of_paths_to_dest(n):
#     if n < 1:
#         return n
#
#     out = 0
#     r = c = 0
#
#     def backtracing(r, c):
#         nonlocal out
#         if r == n-1 and c == n-1:
#             out += 1
#             return
#
#         for ri, ci in ([(1, 0), (0, 1)]):
#             nr, nc = r+ri,c+ci
#             if nr >= nc and nr < n and nc < n :
#                 backtracing(nr, nc )
#
#     backtracing(r, c)
#     return out
#
# res = num_of_paths_to_dest(4)
# print(res)
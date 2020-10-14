def num_of_paths_to_dest(n):
  if n < 1:
    return 0


  r = c = 0
  memo = {}
  def backtracing(r, c):

    if r == n-1 and c == n-1:
      return 1
    if (r,c) in memo:
        return memo.get((r,c))
    for ri, ci in ([(1, 0), (0, 1)]):
      nr, nc = r+ri,c+ci
      if nr >= nc and nr < n and nc < n :
        memo[(r,c)] = memo.get((r,c), 0)+backtracing(nr, nc )
    return memo[(r,c)]

  backtracing(r, c)
  return memo.get((0,0))


print(num_of_paths_to_dest(100))
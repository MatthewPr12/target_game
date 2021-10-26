grid_tuples = []
letters = ["a", "b", "a", "c", "b", "v", "v", "v", "b"]
for j in letters:
    a = letters.count(j)
    grid_tuples.append(tuple([j, a]))
    grid_tuples = sorted(list(set(grid_tuples)))

print(grid_tuples)
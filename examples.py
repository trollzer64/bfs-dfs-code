from main import BFS, DFS, toIncMatrix

example = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
]
print("Original")
for i, row in enumerate(toIncMatrix(example)):
    print("{}\t".format(i) + ", ".join(map(str, row)))

print("\n\n{:^30}".format("BFS"))
print("\nExemplo 1 (R=0):")
matrix, V = BFS(example, 0)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))

print("\nExemplo 2 (R=4):")
matrix, V = BFS(example, 4)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))

print("\nExemplo 3 (R=3):")
matrix, V = BFS(example, 3)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))


print("\n\n{:^30}".format("DFS"))
print("\nExemplo 1 (R=0):")
matrix, V = DFS(example, 0)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))

print("\nExemplo 2 (R=4):")
matrix, V = DFS(example, 4)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))

print("\nExemplo 3 (R=3):")
matrix, V = DFS(example, 3)
print("V = {}".format(V))
for i, row in enumerate(matrix):
    print("{}\t".format(i) + ", ".join(map(str, row)))

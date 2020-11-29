n = input()
print(*list(set([i for i in n if n.count(i) == 2])))
pyramide1: list[list[int]] = [[3], [7, 4], [2, 4, 6], [9, 5, 9, 3]]
memo: list[list[int]] = pyramide1.copy()

for i in range(len(memo)-1):
    for j in range(len(memo[i])):
        memo[i][j]=0

print(memo)
print(pyramide1)

# 1225 

num1, num2 = input().split()
num1, num2 = list(map(int, num1)), list(map(int, num2))

print(sum(num1) * sum(num2))

# import sys

# (a,b) = sys.stdin.readline().split()
# total = 0

# for n in range(len(a)):
#     for i in range(len(b)):
#         total += int(a[n]) * int(b[i])

# print(total)

# 2438

n = int(input())

for a in range(1, n+1):
    print('*' * a)

# 2739

n = int(input())
matrix = []

matrix = [f'{n} * {a} = {n * a}' for a in range(1,10)]

for i in matrix:
    print(i)

# 2953

scores = [(a, sum(list(map(int, input().split())))) for a in range(1, 6)]

scores = sorted(scores, key = lambda x:x[1], reverse=True)

print(*scores[0])

# 2669 

position = [list(map(int, input().split())) for _ in range(4)]
rec = []

for a in range(4):
    for n in range(position[a][0], position[a][2]):
        for i in range(position[a][1], position[a][3]):
            if (str(n) + str(i)) not in rec:
                rec.append(str(n) + str(i))

print(len(rec))
    






# total_area = 0
# part = 0

# position = [list(map(int, input().split())) for _ in range(4)]
# position = sorted(position, key = lambda x:x[0])

# for a in range(4):
#     total_area += (position[a][2] - position[a][0]) * (position[a][3] - position[a][1]) 

# for n in range(1, 4):
#     if position[n][0] < position[n - 1][2] and position[n][1] < position[n - 1][3]:




    


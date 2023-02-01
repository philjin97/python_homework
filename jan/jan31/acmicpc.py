# # 2441

# n = int(input())

# for num in range(n, 0, -1):
#     print(' ' * (n - num) + '*' * num)

# # 2592

# data = [int(input()) for x in range(10)]
# freq = 0
# num = 0

# for i in data:
#     freq_current = data.count(i)
#     if freq_current > freq:
#         num = i


# print(sum(data) // 10)
# print(num)

# # 10798

# data = [input() for x in range(5)]
# password = ''

# for a in range(15):
#     for n in range(5):
#         try:
#             password += data[n][a]
#         except:
#             pass

# print(password)

# 9455

for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [[]for _ in range(n)]

    for i in range(m):
        a = list(input().split())
        for j in range(n):
            grid[j].append(a[j])

print(grid)

# T = int(input())

# for t in range(1, T+1):
#     (a, b) = list(map(int, input().split()))
#     data = [list(map(int, input().split())) for n in range(a)]
#     new_data = data
#     for col in range(a):
#         for row in range(b):
#             new_data[][]= data[a][b]


                

# print(data, new_data)







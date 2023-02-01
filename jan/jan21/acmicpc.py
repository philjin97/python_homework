# # 3003 

# chess_original= [1, 1, 2, 2, 2, 8]
# chess_input = list(map(int, input().split()))
# fix = []

# for a in range(len(chess_original)):
#     value = chess_original[a] - chess_input[a]
#     fix.append(value)

# for n in fix:
#     print(n , end=' ')

# # 10430 

# (a, b, c) = list(map(int, input().split()))

# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c) * (b % c)) % c)

# # 2588

# a = input()
# b = input()

# print(int(a) * int(b[2]))
# print(int(a) * int(b[1]))
# print(int(a) * int(b[0]))
# print(int(a) * int(b))

# # 1330 

# (a, b) = list(map(int, input().split()))

# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# # 2753

# year = int(input())

# if year % 4 == 0:
#     if year % 100 != 0:
#         print('1')
#     elif year % 400 == 0:
#         print('1')
#     else:
#         print('0')
# else:
#     print('0')

# # 14681

# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print('1')
#     elif y < 0:
#         print('4')
# elif x < 0:
#     if y > 0:
#         print('2')
#     elif y < 0:
#         print('3')

# # 2884 

# (a, b) = list(map(int, input().split()))

# if b < 45:
#     if a == 0:
#         a = 23
#         b = 60 + (b - 45)
#         print(a, b, sep=' ')

#     elif a > 0:
#         a -= 1
#         b = 60 + (b - 45)
#         print(a, b, sep=' ')
# elif b >= 45:
#     b -= 45 
#     print(a, b, sep=' ')

# # 2525

# (a, b) = list(map(int, input().split()))
# time = int(input())

# a += (b + time) // 60
# b = (b + time) % 60

# if a >= 24:
#     a -= 24

# print(a, b, sep=' ')

# # 2739

# num = int(input())

# for a in range(1, 10):
#     print(f'{num} * {a} = {num * a}')

# # 8393

# n = int(input())
# total = 0

# for a in range(n + 1):
#     total += a

# print(total)

# # 25304

# total = int(input())
# n = int(input())
# real_total = 0

# for a in range(1, n+1):
#     (a, b) = list(map(int, input().split()))
#     real_total += a * b

# if total == real_total:
#     print('Yes')
# else:
#     print('No')

# # 15552
# import sys

# T = int(input())

# for t in range( 1, T+1):
#     (a, b) = (list(map(int, sys.stdin.readline().split())))
#     print(a + b)

# # 2438 

# n = int(input())

# for a in range(1, n+1):
#     print('*' * a)

# # 2439 
# # import sys

# # n = int(sys.stdin.readline())

# # for a in range(1, n+1):
# #     for b in range(n+1 - a):
# #         print(' ', end='')
# #     for c in range(a):
# #         print('*', end='')
# #     print()

# import sys

# n = int(sys.stdin.readline())

# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end='')
#     for k in range(i+1):
#         print('*', end='')
#     print()

# # 10951 
# import sys

# while True:
#     try:
#         (a, b) = list(map(int, sys.stdin.readline().split()))
#         print(a + b)
#     except: 
#         break

# # 10807
# n = int(input())
# numbers = list(map(int, input().split()))
# v = int(input())
# count = 0

# for a in range(n):
#     if numbers[a] == v:
#         count += 1

# print(count)

# # 10818

# n = int(input())
# numbers = list(map(int, input().split()))

# print(min(numbers), max(numbers), sep=' ')

# # 2562

# numbers = []
# max = [0, 0]

# for a in range(9):
#     numbers.append(int(input()))
#     if numbers[a] > max[0]:
#         max[0] = numbers[a]
#         max[1] = a + 1

# print(max[0], max[1], sep='\n')

# # 5597 

# total = []

# for a in range(1, 31):
#     total.append(a)

# for n in range(28):
#     hw = int(input())
#     total.remove(hw)

# for missing in total:
#     print(missing)

# 3052 

numbers = []
remainder = {}

for n in range(10):
    numbers.append(int(input()))

for a in numbers:
    remainder[a % 42] = 0

print(len(list(remainder)))








    










    




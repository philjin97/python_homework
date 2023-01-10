# # 1. 
# n = -1

# string = input('Input a String: ')
# for s in range(len(string)):
#     if string[s] == 'e':
#         n = s
#         break
# print(n)

# # 2. 
# wd = {}

# words = input().split()
# for n in words:
#     if n in wd:
#         wd[n] += 1
#     else:
#         wd[n] = 1

# for k, v in wd.items():
#     print(k, v)

# # 3. 
# without = ''

# string = input('Input a String: ')
# for s in string:
#     if s != 'e':
#         without += s
# print(without)

# # 4. 
# n = 0

# string = input().split()
# for s in string[0]:
#     if s == string[1]:
#         n += 1
# print(n)

# # 5. 
# string = ''
# numbers = input().split()
# for n in range(len(numbers)):
#     if n == 0:
#         string += numbers[0]
#     else:
#         string += '-' + numbers[n]
# print(string)

# 6. 다시 풀어보기 
number = int(input())
n = 0 

while number > 0:
    n += number % 10
    number //= 10

print(n)









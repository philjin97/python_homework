# # 9085

# T = int(input())
# total = 0

# for t in range(1, T+1):
#     N = int(input())
#     numbers = sum(list(map(int, input().split())))
 
#     print(numbers)

# # 10824

# (a, b, c, d) = list(map(str, input().split()))
# first = a + b
# second = c + d
# print(int(first) + int(second))

# # 3009 

# row = []
# column = []

# for n in range(3):
#     (a, b) = list(map(int, input().split()))
#     if a in row:
#         row.remove(a)
#         if b in column: 
#             column.remove(b)
#         else: 
#             column.append(b)
#     else:
#         row.append(a)
#         if b in column: 
#             column.remove(b)
#         else: 
#             column.append(b)
    
# print(row[0], column[0])

# # 10952 

# a = 1
# b = 1

# while a != 0 and b != 0:
#     (a, b) = list(map(int, input().split()))
#     if a == 0 and b == 0:
#         break 
#     print(a + b)

# 1110 

number = input()        
if len(number) == 1:
    number = '0' + number
    a = '0'
else: 
    a = number[0]
b = number[-1]
result = ''
cnt = 0

while number != result:
    added = int(a) + int(b)
    string = str(added)
    a = b
    b = string[-1]
    result = a + b
    cnt += 1

print(cnt)



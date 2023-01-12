# 2072
T = int(input())
odd = 0

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    for n in numbers:
        if n % 2 == 1:
            odd += n
    print(f'#{t} {odd}')
    odd = 0


# 2056

T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
   case = str(input())
   year = case[0:4]
   month = case[4:6]
   day = case[6:8]
   
   answer = ''
   if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
       answer = year + '/' + month + '/' + day
   else:
       answer += '-1'
   print("#" + str(test_case) + " " + answer)


# 2043
(a,b) = list(map(int, input().split()))
n = 1 

while a != b:
    b += 1
    n += 1

print(n)


1933
number = int(input())
for n in range(1,number+1):
    if number % n == 0:
        print(n, end=' ')


# 1288
T = int(input())

for t in range(1, T+1):
    number = int(input())
    num = number
    numbers_dict = {}
    a = 0
    while len(numbers_dict) < 10:
        num = str(num)
        for n in num:
            numbers_dict[n] = 0
        num = int(num)
        num += number
        a += 1
    print(f'#{t} {a*number}')
















# ---------------------------------------------------------------------------
# 2056
# T = int(input())
# date = ''

# for t in range(1, T+1):
#     string = input()
#     if string[4] != '0':                                               # Checking validity of the month
#         if string[4] == '1':
#             if string[5] == '1' or string[5] == '2':
#                 continue
#             else:
#                 print(-1)
#                 break
#         else:
#             print(-1)
#             break
#     if string[4] == '0':               #for months that start with 0
#         if string[5] == '1' or string[5] == '3' or string[5] == '5' or string[5] == '7' or string[5] == '8':       # for months with 31 days
#             if string[6] != '1' or string[6] != '2' or string[6] != '3':
#                 print(-1)
#                 break
#             elif string[6] == 3:
#                 if string[7] != '0' or string[7] != '1':
#                     print(-1)
#                     break
#         if string[5] == '4' or string[5] == '6' or string[5] == '9': # for months with 30 days
#             if string[6] != '1' or string[6] != '2' or string[6] != '3':
#                 print(-1)
#                 break
#             elif string[6] == 3:
#                 if string[7] != '0':
#                     print(-1)
#                     break
#             else:
#                 continue
#         if string[5] == '2':
#             if string[6] != '1' or string[6] != '2': 
#                 print(-1)
#                 break
#             elif string[6] == 2:
#                 if string[7] == '9':
#                     print(-1)
#                     break
#             else:
#                 continue
#         else:                      # if anything other than above cases in string[5], then error
#             print(-1)
#             break
#     if string[4] == '1':           # for months that start with 1
#         if string[5] == '0' or string[5] == '2':       # for months with 31 days
#             if string[6] != '1' or string[6] != '2' or string[6] != '3':
#                 print(-1)
#                 break
#             elif string[6] == 3:
#                 if string[7] != '0' or string[7] != '1':
#                     print(-1)
#                     break
#             else:
#                 continue
#         if string[5] == '1':  
#             if string[6] != '1' or string[6] != '2' or string[6] != '3':
#                 print(-1)
#                 break
#             elif string[6] == 3:
#                 if string[7] != '0':
#                     print(-1)
#                     break
#             else:
#                 continue
#         else:
#             print(-1)
#             break
#     date = f'{string[0]}{string[1]}{string[2]}{string[3]}/{string[4]}{string[5]}/{string[6]}{string[7]}'
#     print(date)
# -----------------------------------------------------------
# T = int(input())

# for t in range(1, T+1):
#     string = input()
#     year = int(string[:4])
#     month = int(string[4:6])
#     day = int(string[6:])

#     if month > 12 or month < 1:
#         print(print(f'#{t} -1'))
#         continue

#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#             if day > 31 or day < 1:
#                 print(f'#{t} -1')
#                 continue
#     if month == 4 or month == 6 or month == 9 or month == 11:
#             if day > 30 or day < 1:
#                 print(f'#{t} -1')
#                 continue
#     if month == 2:
#             if day > 28 or day < 1:
#                 print(f'#{t} -1')
#                 continue
    
#     print(f'#{t} {year}/{month}/{day}')

# 1.
num = int(input("정수를 입력하세요"))
if num >= 0:
    print(num)
else:
    print( num * -1)

# 2. 
number_list = list(input("정수들을 입력하세요"))
n = 0 

for num in number_list:
    n += 1
print(n)

# 3.
number_list = list(input("정수들을 입력하세요"))
result = 0

for num in number_list:
    result += int(num)
print(result)

# 4.
number_list = list(input("정수들을 입력하세요"))
result = 0
n = 0

for num in number_list:
    result += int(num)
    n += 1
print(float(result / n))

# 5.
number_list = list(input("정수들을 입력하세요"))
result = 1

for num in number_list:
    result *= int(num)
print(result)

# 6. 
number_list = list(input("정수들을 입력하세요"))
result = 0

for num in number_list: 
    a = int(num)
    if a > result:
        result = a
print(result)

# 7. 
number_list = list(input("정수들을 입력하세요"))
result = int(number_list[0])

for num in number_list: 
    a = int(num)
    if a < result:
        result = a
print(result)



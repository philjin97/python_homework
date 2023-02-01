# 1.
num = int(input("정수를 입력하세요"))
if num > 0:
    print("True")
else:
    print("False")

# 2. 
num1 = int(input("첫 번째 정수를 입력하세요"))
num2 = int(input("두 번째 정수를 입력하세요"))
if num1 == num2:
    print("False")
else:
    if num1 > num2:
        print(num1)
    else: 
        print(num2)

# 3. 
num = int(input("정수를 입력하세요"))
if num > 1 and num < 10:
    print("True")
else:
    print("False")

# 4. 
num = int(input("정수를 입력하세요"))
if num > 0 and num % 2 == 0:
    print("True")
else:
    print("False")

# 5. 
num = int(input("정수를 입력하세요"))
if num >= 60:
    if num > 100:
        print("Error")
    else: 
        print("합격")
else:
    if num < 0:
        print("Error")
    else: 
        print("불합격")

# 6. 
string = (input('문자열을 입력하세요'))
for i in range(len(string) -1, 0, -1):
    print(string[i])

# 7. 
num1 = int(input("첫 번째 정수를 입력하세요"))
num2 = int(input("두 번째 정수를 입력하세요"))
if num1 > num2:
    for i in range(num2 + 1, num1 - 1):
        print(i)
elif num2 > num1:
    for i in range(num1 + 1, num2 - 1):
        print(i)
else:
    print("False")

# 8.
#1번 풀이
num1 = int(input("첫 번째 정수를 입력하세요"))
num2 = int(input("두 번째 정수를 입력하세요"))

if num1 > num2:
    for i in range( num1 - 1, num2 + 1, -1):
        print(i, end=" ")
elif num2 > num1:
    for i in range( num2 - 1, num1 + 1, -1):
        print(i, end=" ")
else:
    print("False")


#2번 풀이 
num1 = int(input("첫 번째 정수를 입력하세요"))
num2 = int(input("두 번째 정수를 입력하세요"))
result = ""

if num1 > num2:
    for i in range( num1 - 1, num2 + 1, -1):
        result += str(i) 
elif num2 > num1:
    for i in range( num2 - 1, num1 + 1, -1):
        result += str(i) 
else:
    print("False")
print(result)

# 9. 
num1 = int(input("정수를 입력하세요"))
if num1 < 1:
    print("False")
else: 
    for num in range(1 , num1, +2):
        print(num)

# 10. 
for x in range(2, 10):
    for y in range(2, 10):
        print(x, "x", y, "=", x*y)






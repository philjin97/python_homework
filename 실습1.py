# Number 1
number = int(input("Input a number."))
number += 10
print(number)

# Number 2
food = input("좋아하는 음식은?")
print(food)

# Number 3
name = input("Input your name.")
birth = int(input("When were you born?"))
print("저의 이름은", name, "이고, 올해 나이는", 2023 - birth, "입니다." )

# Number 4
sent1 = input("첫 번쨰 문장을 입력해주세요. ")
sent2 = input("두 번쨰 문장을 입력해주세요. ")
print(sent1, sent2)

# Number 5
num = int(input("숫자를 입력해주세요."))
print (-1 * num)

# Number 6
num1 = int(input("첫 번쨰 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))
print("더하기 연산: ", num1 + num2)
print("빼기 연산: ", num1 - num2)
print("곱하기 연산: ", num1 * num2)
print("몫 연산: ", num1 // num2)
print("나머지 연산: ", num1 % num2)

# Number 7
num1 = int(input("첫 번쨰 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))
num3 = int(input("세 번째 숫자를 입력하세요."))
print((num1 + num2 + num3) / 3)

# Number 8
num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))
num3 = int(input("세 번째 숫자를 입력하세요."))
num4 = int(input("네 번째 숫자를 입력하세요."))
num5 = int(input("다섯 번째 숫자를 입력하세요."))
numbers_list = [num1, num2, num3, num4, num5]
print(numbers_list)

# Number 9
sent1 = (input("문자열을 입력하세요."))
num1 = int(input("숫자를 입력하세요."))
print(sent1 * num1)

# Number 10
num = 0

num1 = int(input("첫 번째 숫자를 입력하세요."))
num += num1
print (num)
num2 = int(input("두 번째 숫자를 입력하세요."))
num += num2
print (num)
num3 = int(input("세 번째 숫자를 입력하세요."))
num += num3
print (num)
num4 = int(input("네 번째 숫자를 입력하세요."))
num += num4
print (num)
num5 = int(input("다섯 번째 숫자를 입력하세요."))
num += num5
print (num)
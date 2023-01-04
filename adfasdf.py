number_list = list(input("정수들을 입력하세요"))
result = int(number_list[0])

for num in number_list: 
    a = int(num)
    if a < result:
        result = a
print(result)

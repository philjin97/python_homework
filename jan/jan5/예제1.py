# 1. 
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스

# 2. 
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"


print(dict_variable["a"]) # A
print(dict_variable["D"]) # d
# print(dict_variable["b"]) # undefined

# 3. 
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000

# 4. 
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
예측을 작성하세요.
이름 정우영
생년원일 19000101
회사 하이퍼그로스
"""

# 5. 
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""
예측을 작성하세요.
이름 정우영 
생년월일 19000101
회사 하이퍼그로스
"""

# 6. 
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

# 7. 
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # "거주지"라는 key가 dict_variable 딕셔너리에 존재하지 않으면, 딕셔너리에 "거주지"라는 key와 그에 해당하는 value인 "서울특별시"를 추가하시오.
    
print(dict_variable) # {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}

# 8. 
list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
에러가 발생했습니다.
에러의 원인은 무엇인가요?
"""

# 9. 
# try:
#     number = 1
#     if number == 1
#         print(number)
    
    
# except:
#     print("에러가 발생했습니다.")
#     print("에러의 원인은 무엇인가요?")

# """
# Syntax Error. if <expression>: 에 해당하는 컬런이 빠졌습니다. 

# """ 

# 10. 
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3
        # 0, 4, 8, 14, 22, 30, 42, 52, 68, 80, 100

print(total) # 100 
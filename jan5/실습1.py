# 1. 
n = 0
line = input("문자열을 입력하세요")

for letter in line:
    if letter == "e":
        n += 1
    else: 
        continue

print(n)

# 2. 
n = 0
line = input("문자열을 입력하세요")
line2 = line.lower()
vowel = ["a", "e", "o", "i", "u"]

for l in line2:
    for v in vowel:
        if l == v:
            n += 1
        else: 
            continue

print(n)

# 3. 
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

print("나이: ", 2023 - int(dict_variable["생년"]), "세")

# 4. 
address = {}
address['이름'] = input("이름을 입력하세요")
address['전화번호'] = input("전화번호를 입력하세요")
address['거주지'] = input("거주지를 입력하세요")

for key, value in address.items():
    print(key,':', value)

# 5. 
basic = {}
address = {}

name = input("이름을 입력하세요")

address['전화번호'] = input("전화번호를 입력하세요")
address['이메일'] = input("이메일을 입력하세요")
address['거주지'] = input("거주지를 입력하세요")

basic[name] = address
print(basic)

# 6. 
letters = {}
line = input("문자열을 입력하세요")

for l in line:
    for n in letters.keys():
        if l == n:
            a = letters[n]
        else:
            letters[l] = 1
        
# 7. 
letters = {}
line = input("문자열을 입력하세요")
a = ""

for l in line:
    if l in letters:
        letters[l] += 1
    else:
        letters[l] = 1

        
for x, y in letters.items():
    print(x, y)


    


# 10101

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b == c == 60:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

# 2720

T = int(input())


for t in range(1, T+1):
    change = [0, 0, 0, 0]
    price = int(input())
    change[0] = price // 25
    price -= (25 * change[0])
    change[1] = price // 10
    price -= (10 * change[1])
    change[2] = price // 5
    price -= (5 * change[2])
    change[3] = price // 1
    print(change[0], change[1], change[2], change[3])

# 1453

N = int(input())
seat = list(map(int, input().split()))
computer = []
cnt = 0

for n in range(N):
    if seat[n] in computer:
        cnt += 1
    else:
        computer.append(seat[n])

print(cnt)



# N = int(input())
# seat = list(map(int, input().split()))
# count = {}
# result = 0

# for a in seat:
#     if a in count:
#         count[a] += 1
#     else:
#         count[a] = 1

# for key, value in count.items():
#     if value != 1:
#         result = value - 1

# print(result)

# 10773

k = int(input())
total = []
 
for n in range(k):
    num = int(input())
    if num == 0:
        total.pop()
    else:
        total.append(num)

print(sum(total))

# 2161

n = int(input())
original = []
trash = []

for num in range(n):
    original.append(num+1)

for num in range(n):
    if len(original) > 1:
        trash.append(original.pop(0))
        original.append(original.pop(0))
    else:
        break

for a in trash:
    print(a, end=' ')
print(original[0])

# 9012

T = int(input())


for t in range(1, T+1):
    result = 0
    string = str(input())
    for a in string:
        if a == '(':
            result += 1
        elif a == ')': 
            result -= 1
            if result < 0:
                break
    if result == 0:
        print('YES')
    else:
        print('NO')
        
    


    


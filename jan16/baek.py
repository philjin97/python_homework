# 10039 
n = 0
result = 0

while n < 5:
    a = int(input())
    if a < 40:
        a = 40
    result += a
    n += 1

print(result // 5) 

# 10871
(a, b) = list(map(int, input().split(' ')))
number = list(map(int, input().split(' ')))

for each in range(a):
    if number[each] < b:
        print(number[each], end=' ')
    
# 2480 
numbers = list(map(int, input().split()))
dice = {}

for num in numbers:
    if num in dice:
        dice[num] += 1
    else:
        dice[num] = 1

if len(dice) == 1:
    print(10000 + (num * 1000))
elif len(dice) == 2:
    for key in dice:
        if dice[key] == 2:
            print(1000 + (key * 100))
else: 
    keyss = sorted(list(dice), reverse=True)
    print(keyss[0] * 100) 

# 10886

N = int(input())
cute = {'0': 0, '1': 0}

for n in range(N):
    person = input()
    if person in cute:
        cute[person] += 1

if cute['0'] > cute['1']:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')

# 2506

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
result = 0

for n in numbers:
    if n == 1:
        result += 1 + cnt
        cnt += 1
    else:
        cnt = 0

print(result)



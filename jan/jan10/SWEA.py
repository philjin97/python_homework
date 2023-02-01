# # 1. 2029
T = int(input())
 
for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    qt = a // b
    rem = a % b
    print(f'#{t}', qt, rem)

# # 2. 2071
T = int(input())
total = 0
cnt = 0

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    for num in numbers:
        total += num
        cnt += 1
    print(f'#{t}', round(total/cnt))
    total = 0
    cnt = 0 

# 3. 1938 
a, b = list(map(int, input().split()))
print(a + b)
print(a - b)
print(a * b)
print(a//b)

# 4. 2046
num = int(input())
print('#' * num)

# 5. 2068
T = int(input())
n = 0

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num > n:
            n = num
    print(f'#{t} {n}')
    n = 0

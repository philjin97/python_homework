# 9498 

score = int(input())

if score > 89:
    print('A')
elif score > 79:
    print('B')
elif score > 69:
    print('C')
elif score > 59:
    print('D')
else:
    print('F')

# 9093 

T = int(input())

for t in range(1, T+1):
    words = input().split()
    for w in words:
        rev_w = w[::-1]
        print(rev_w, end=' ')

# 11721

sentence = input()

for n in range(len(sentence)):
    if (n + 1) % 10 == 0 and n != 0:
        print(sentence[n])
    else:
        print(sentence[n], end='')

# 2947

numbers = list(map(int, input().split()))


while numbers != [1, 2, 3, 4, 5]:
    for n in range(4):
        if numbers[n+1] > numbers[n]:
            continue
        else:
            numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
            for a in numbers:
                if numbers.index(a) == 4:
                    print(f'{a}')

                else:
                    print(a, end=' ')



                    # print(*numbers)
            
        
        
            
        
            






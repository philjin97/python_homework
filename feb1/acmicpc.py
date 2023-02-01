# 2525

(a, b) = list(map(int, input().split()))
time = int(input())

a += (b + time) // 60
b = (b + time) % 60

if a >= 24:
    a -= 24

print(a, b, sep=' ')

# 2798

(n, m) = list(map(int, input().split()))
cards = list(map(int, input().split()))
max_sum = 0

for a in cards:
    for b in cards:
        for c in cards:
            if a != b and b != c and a != c:
                if a + b + c <= m and a + b + c > max_sum:
                    max_sum = a + b + c
                    

print(max_sum)

# 9076

T = int(input())

for t in range(1, T+1):
    score = sorted(list(map(int, input().split())))
    three_score = [score[num] for num in range(1, 4)]
    if three_score[-1] - three_score[0] >= 4:
        print('KIN')
    else:
        print(sum(three_score))

# 1526 
import sys 

N = int(sys.stdin.readline())

while True:
    flag = True
    for a in str(N):
        if a != '4' and a != '7':
            flag = False
            N -= 1
    if flag:
        print(N)
        break

# 1436

n = int(input())
cnt = 0
six_n = 666

while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1


# n = int(input())
# start = '666'
# bag = []


# while len(bag) != n:
#         for i in range(len(start)):
#             if start[i] == '6':
#                 try:
#                     if start[i+1] == '6':
#                         if start[i+2] == '6':
#                             bag.append(start)
#                             start = int(start) 
#                             start += 1
#                             start = str(start)
#                 except:
#                     continue
                        
#             else:
#                 start = int(start) 
#                 start += 1
#                 start = str(start)


# print(bag)


    
    

        
    





    

        

    








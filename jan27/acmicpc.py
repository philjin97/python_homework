# 10817

import heapq

numbers = list(map(int, input().split()))

heapq.heapify(numbers)
heapq.heappop(numbers)
print(numbers[0])

# 20001 

string = input()

if string == '고무오리 디버깅 시작':
    problem = []
    while True:
        direction = input()
        if direction == '문제':
            problem.append('문제')
        elif direction == '고무오리':
            if len(problem) > 0:
                problem.pop()
            else:
                problem.append('문제')
                problem.append('문제')
        elif direction == '고무오리 디버깅 끝':
            break
    if len(problem) == 0:
        print('고무오리야 사랑해')
    else:
        print('힝구')

# 1269

(a, b) = list(map( int, input().split()))
seta = set(list(map(int, input().split())))
setb = set(list(map(int, input().split())))

print(len(seta - setb) + len(setb - seta))

# 3052

numbers = []
remainder = {}

for n in range(10):
    numbers.append(int(input()))

for a in numbers:
    remainder[a % 42] = 0

print(len(list(remainder)))

# 1181 

n = int(input())
line = []

for num in range(n):
    line.append(input())

line = list(set(line))
line.sort()
line.sort(key=lambda x:len(x))

print('\n'.join(line))

# 11286
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for num in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(number), number)) # tuple의 왼쪽 값을 비교하고 실제 값은 오른쪽.





    






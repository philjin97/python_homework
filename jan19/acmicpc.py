# 2576

total = 0
small = 0

for t in range(7):
    num = int(input())
    if num % 2 == 1:
        total += num
        if small == 0:
            small = num
        elif small > num:
            small = num

if total == 0:
    print(-1)
else: 
    print(total, small, sep='\n')

# 10822

numbers = sum(list(map(int, input().split(','))))
print(numbers)

# 2754

score = {'A+':4.3,'A0':4.0,'A-':3.7,'B+':3.3,'B0':3.0,'B-':2.7,'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0':1.0,'D-':0.7,'F':0.0,}
print(score[input()])

# 5622

phone_num = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}
word = input()
time = 0

for l in word:
    number = phone_num[l]
    time += number + 1

print(time)

# 2577
A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)
numbers = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for n in total:
    numbers[n] += 1

for a in range(10):
    print(numbers[str(a)])

# 7785

number = int(input())
attendance = {}

for n in range(number):
    log = input().split()
    if log[0] not in attendance:
        attendance[log[0]] = log[1]
    else:
        attendance.pop(log[0])

attendance_order = sorted(list(attendance), reverse=True)

for a in attendance_order:
    print(a)







    
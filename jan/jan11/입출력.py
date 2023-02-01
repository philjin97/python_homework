# 1.
numbers = list(map(int, input().split()))
for number in numbers:
    print(number, end=' ')

# 2. 
string = input().split()
for word in string:
    print(word, end=' ')

# 3. 
T = int(input())

for t in range(1, T+1):
    N = int(input())

    for _ in range(N):
        number = int(input())
        print(number)

# 4. 
T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        a, b = list(map(int, input().split()))
        print(a, b)

# 5. 
T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        string = input().split()
        for word in string:
            print(word, end=' ')
# 6. 
T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        numbers = list(map(int, input().split()))
        for number in numbers:
            print(number, end=' ')

# 7. 

(T, N) = list(map(int, input().split()))

for t in range(1, T+1):

    for _ in range(N):
        number = int(input())
        print(number)

# 8. 

(T, N) = list(map(int, input().split()))

for t in range(1, T+1):

    for _ in range(N):
        (a, b) = list(map(int, input().split()))
        print(a, b)

# 9. 
(T, N) = list(map(int, input().split()))

for t in range(1, T+1):

    for _ in range(N):
        numbers = list(map(int, input().split()))
        for number in numbers:
            print(number, end=' ')


        
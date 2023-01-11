# 2047
string = input()
string2 = string.upper()
print(string2)

# 2025 
numbers = int(input())
result = 0

for n in range(1, numbers+1):
    result += n

print(result)

# 1936
(a, b) = list(map(int, input().split()))

if a == 1 and b == 3:
    print('A')
elif a == 2 and b == 1:
    print('A')
elif a == 3 and b == 2:
    print('A')
elif b == 1 and a == 3:
    print('B')
elif b == 2 and a == 1:
    print('B')
elif b == 3 and a == 2:
    print('B')

# 2027
adds = ['+','+','+','+','+']
for n in range(5):
    adds[n] = '#'
    string = ''.join(adds)
    print(string)
    adds[n] = '+'

# 2058
number = int(input())
result = 0 

while number > 0:
    result += number%10
    number = number//10

print(result)
    
# 2019 
n = int(input())

for number in range(n+1):
    print(2**number, end=' ')



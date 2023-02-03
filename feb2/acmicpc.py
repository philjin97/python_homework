# # 1547

# n = int(input())
# graph = [[0] for _ in range(3)]
# graph[0][0] = 1

# for _ in range(n):
#     v1, v2 = list(map(int, input().split()))
#     if graph[v1 -1][0] == 1:
#         graph[v1 -1][0] = 0
#         graph[v2 -1][0] = 1
#     elif graph[v2 -1][0] == 1:
#         graph[v2 -1][0] = 0
#         graph[v1 -1][0] = 1
#     else:
#         continue

# for a in range(3):
#     if graph[a][0] == 1:
#         print(a + 1)

# # 5576

# w = sorted([int(input()) for _ in range(10)])
# k = sorted([int(input()) for _ in range(10)])

# print(w[-3] + w[-2] + w[-1], k[-3] + k[-2] + k[-1], sep=' ' )

# # 2846

# n = int(input())
# mapping = list(map(int, input().split()))
# up = []
# current_up = 0

# for a in range(n-1):
#         if mapping[a + 1] > mapping[a]:
#             if a + 1 == n - 1:
#                 current_up += mapping[a + 1] - mapping[a]
#                 up.append(current_up)
#             else:
#                 current_up += mapping[a + 1] - mapping[a]
#         else:
#             up.append(current_up)
#             current_up = 0

# up = sorted(up)

# print(up[-1])

# 1251

string = "mobitel"

string_list = []

N = len(string)


# i 와 j 의 구간을 구하는 것이 어려운 문제
for i in range(1, N -1):
    for j in range(i + 1, N):
        a = string[0:i]
        b = string[i:j]
        c = string[j:N]

        reversed_a = a[::-1]
        reversed_b = b[::-1]
        reversed_c = c[::-1]

        join_string = reversed_a + reversed_b + reversed_c

        string_list.append(join_string)

print(min(string_list))

# heapq도 사용 가능 

# import heapq import
# heappush(string_heap, join_string)
# print(heappop(string_heap))


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# string = input()
# numbering = []

# for a in string:
#     for i in range(len(alphabet)):
#         if alphabet[i] == a:
#             numbering.append([i , a])

# numbering = sorted(numbering)
# print(numbering)

# first_part = string[:string.find(numbering[0][1]) + 1]
# string = string[string.find(numbering[0][1]) + 1:]

# for n in range(1, len(numbering)+1):
#     if numbering[n][1] in string:
#         second_part = string[:string.find(numbering[n][1]) + 1]
#         string = string[string.find(numbering[n][1]) + 1:]
#         break

# first_part = first_part[::-1]
# second_part = second_part[::-1]
# string = string[::-1]

# print(first_part, second_part, string, sep='')













            
    


    













# 2606

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
total = -1

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                
dfs(1)

for a in visited:
    if a == True:
        total += 1

print(total)

# 10769

string = input()

n_happy = string.count(':-)')
n_sad = string.count(':-(')

if n_happy < n_sad:
    print('sad')
elif n_happy > n_sad:
    print('happy')
elif n_happy == 0 and n_sad == 0:
    print('none')
elif n_happy == n_sad:
    print('unsure')

# 2455





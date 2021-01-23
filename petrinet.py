input_transition = []
output_transition = []
# no of places
n = int(8)
# number of transitions
t = int(5)
edges = [
            [[1],[2,3]],
            [[2,3],[4]],
            [[3],[4,5,6]],
            [[4,5],[7]],
            [[5,6],[8]]
        ]
queue = []
# converting it into bit format using bit manipulation
for i in range(t):
    a = 0
    for x in edges[i][0]:
        a += (1<<x)
    input_transition.append(a)
    a = 0
    for x in edges[i][1]:
        a += (1<<x)
    output_transition.append(a)


queue.append(input_transition[0])
vis = set()
graph = {}
while(len(queue)):
    u = queue.pop(0)
    if u not in vis:
        vis.add(u)
    else:
        continue
    for i in range(t):
        if (u&input_transition[i] == input_transition[i]) or (u|input_transition[i] == u):
            v = (input_transition[i]^u)|output_transition[i]
            queue.append(v)
            if graph.get(u) is None:
                graph[u]=[{v,i}]
            else:
                graph[u].append({v,i})

for x in vis:
    a = [0,0,0,0,0,0,0,0]
    for i in range(9):
        if x&(1<<i):
            a[i-1]=1
    print(a)

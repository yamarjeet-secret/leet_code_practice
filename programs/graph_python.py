#edges = [ [0,1],[0,4],[4,1],[4,3],[1,3],[1,2],[3,2] ]

edges = [
[4, 5],
[1, 6],
[11, 6],
[8 ,6],
[10, 5],
[2, 5]]
temp = edges

def print_adjacency_list(Vertex,edges):
    result = []
    d = dict()
    vertex = Vertex
    for v in range(0,vertex):
        d[v] = []
        top_value = v
        result = []
        for e in edges:
            if top_value in e:
                for discard in e:
                    if not discard == top_value:
                        result.append(discard)
                        d[top_value] = result
        # if v not in d:
        #     d[v] = []
    
    final_ans = []
    dict_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    for k,v in dict_d.items():
        final_ans.append(v)
        
    print(final_ans)
    return final_ans

result = []
d = dict()
vertex = 12


def optimized_version_with_map(edges,vertex):
    d = dict()
    for v in range(0,vertex):
        d[v] = []

    for e in edges:
        a = e[0]
        b = e[1]
        d[a].append(b)
        d[b].append(a)

    final_ans = []
    print(d)
    dict_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    for k,v in dict_d.items():
        final_ans.append(v)
        
    return final_ans


#Function to return a list containing the DFS traversal of the graph.
def dfsOfGraph(V, adj):
    # code here
    s = [] #empty stack to traversal of nodes
    visited = [] #boolean array to keeptrack of visited/notvisited
    for i in range (0,V):
        visited.append(False)
    s.append(0)
    result = []
    while(len(s)>0):
        n = s.pop()
        if visited[n] == False:
            visited[n] = True
            result.append(n)
            for e in adj[n][::-1]:
                s.append(e)
    
    return result

#Function to return Breadth First Traversal of given graph.
def bfsOfGraph(V, adj):
    # code here
    s = [] #empty queue to traversal of nodes
    visited = [] #boolean array to keeptrack of visited/notvisited
    for i in range (0,V):
        visited.append(False)
    s.append(0)
    result = []
    while(len(s)>0):
        n = s.pop(0)
        if visited[n] == False:
            visited[n] = True
            result.append(n)
            for e in adj[n]:
                s.append(e)

    return result


def transitiveClosure(self, N, graph):
    # code here
    # floyd warshall algorithm
    reach = [i[:] for i in graph]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i==j:
                    reach[i][j] = 1
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
                
    return reach

V = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]
adjs = [[0, 1],
[0, 2],
[0, 4],
[0, 8],
[1, 5],
[1, 6],
[1, 9],
[2, 4],
[3, 7],
[3, 8],
[5, 8],
[6, 7],
[6, 9] ]
final_result = dfsOfGraph(V=V,adj=adj)
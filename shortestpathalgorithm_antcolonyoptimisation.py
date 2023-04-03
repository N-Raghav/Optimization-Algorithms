
import numpy as np
nv = 5

graph = np.full((nv,nv),np.inf)

graph[0][1] = 4
graph[1][0] = 4

graph[1][2] = 10
graph[2][1] = 10

graph[1][3] = 3
graph[3][1] = 3

graph[2][3] = 5
graph[3][2] = 5

graph[2][4] = 7
graph[4][2] = 7

graph[3][4] = 6
graph[4][3] = 6

print(graph)
#%%
ph = np.ones((nv,nv))
#%%

def choosevertex(graph,pheremones,currvert):
    graph = 1/graph
    
    numerator = graph[currvert]*pheremones[currvert]
    denominator = np.dot(graph[currvert],pheremones[currvert])
    
    prob = numerator/denominator
    
    roulettewheel = np.cumsum(prob)
    rb = np.random.random()
    
    nextvertex = np.where(roulettewheel > rb)[0][0]
    
    return nextvertex
#%%
def traverse(graph,pheremones,start,end):
    path = [start]
    cost = 0
    
    curr = start
    while curr != end:
        nextvertex = choosevertex(graph,pheremones,curr)
        cost += graph[curr][nextvertex]
        path += [nextvertex]
        curr = nextvertex
        
        
    return path,cost
#%%
def release(graph,pheremones,start,end,no = 10):
    paths = []
    costs = []
    
    for i in range(no):
        p,c = traverse(graph,pheremones,start,end)
        
        paths += [p]
        costs += [c]
        
    return paths,costs
#%% 
def updatepheremones(graph,pheremones,paths,costs,decay = 0.1):
    costs = np.array(costs)
    costs = 1/costs
    
    pheremones = (1-decay)*pheremones
    for p in range(len(paths)):
        path = paths[p]
        
        for v in range(len(path) - 1):
            pheremones[path[v]][path[v+1]] += costs[p]
            
    return pheremones
#%%
generations = 20
for gen in range(generations):
    p,c = release(graph,ph,0,4)
    ph = updatepheremones(graph,ph,p,c, 0)
print(ph)
print(p)
print(c)
    
    
    




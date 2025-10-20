import heapq, math, time, sys

def read_input(file):
    g, c, S, D = {}, {}, None, None
    for line in open(file):
        line = line.strip()
        if not line or line.startswith('#'): continue
        p = line.split(',')
        if p[0] == 'S': S = int(p[1])
        elif p[0] == 'D': D = int(p[1])
        elif len(p) == 2:
            v, cell = map(int, p)
            x, y = divmod(cell, 10)
            c[v] = (x, y)
            g.setdefault(v, [])
        else:
            u, v, w = map(int, p)
            g.setdefault(u, []).append((v, w))
            g.setdefault(v, []).append((u, w))
    return g, c, S, D

def h_zero(n,g,c): return 0
def h_euclid(n,g,c): x1,y1=c[n];x2,y2=c[g];return math.hypot(x1-x2,y1-y2)
def h_manh(n,g,c): x1,y1=c[n];x2,y2=c[g];return abs(x1-x2)+abs(y1-y2)

def astar(G,C,s,t,h):
    t0=time.perf_counter();pq=[(h(s,t,C),s)];heapq.heapify(pq)
    g={s:0};p={s:None};exp=push=0;mx=1
    while pq:
        f,n=heapq.heappop(pq)
        exp+=1
        if n==t:
            path=[];x=n
            while x is not None: path.append(x);x=p[x]
            path.reverse()
            return path,g[n],exp,push,mx,time.perf_counter()-t0
        for v,w in G.get(n,[]):
            ng=g[n]+w
            if ng<g.get(v,float('inf')):
                g[v]=ng;p[v]=n
                heapq.heappush(pq,(ng+h(v,t,C),v))
                push+=1;mx=max(mx,len(pq))
    return None,None,exp,push,mx,time.perf_counter()-t0

if __name__=="__main__":
    if len(sys.argv)<2: print("Usage: python astar_input.py <file>");sys.exit()
    G,C,S,D=read_input(sys.argv[1])
    modes=[("UCS",h_zero),("A* Euclidean",h_euclid),("A* Manhattan",h_manh)]
    for name,h in modes:
        path,cost,exp,push,mx,t=astar(G,C,S,D,h)
        print(f"MODE: {name}")
        if path: print(f"Optimal cost: {cost}\nPath: {' -> '.join(map(str,path))}")
        else: print("Optimal cost: NO PATH")
        print(f"Expanded: {exp}\nPushes: {push}\nMax frontier: {mx}\nRuntime (s): {t:.6f}\n")

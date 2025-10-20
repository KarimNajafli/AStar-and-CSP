import sys
from collections import deque, defaultdict

def read_input(file):
    with open(file) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    k = int(lines[0].split("=")[1])
    edges, vars = set(), set()
    for l in lines[1:]:
        u, v = map(int, l.split(","))
        if u == v: print("failure"); sys.exit()
        a, b = sorted((u, v))
        edges.add((a, b)); vars |= {u, v}
    return k, sorted(vars), edges

def ac3(dom, nbs):
    q = deque([(x, y) for x in nbs for y in nbs[x]])
    while q:
        x, y = q.popleft()
        rem = {vx for vx in dom[x] if all(vx == vy for vy in dom[y])}
        if rem:
            dom[x] -= rem
            if not dom[x]: return False
            for z in nbs[x] - {y}: q.append((z, x))
    return True

def mrv(dom, assign): return min((v for v in dom if v not in assign), key=lambda x: len(dom[x]), default=None)

def lcv(var, dom, nbs):
    vals = list(dom[var])
    vals.sort(key=lambda val: sum(val in dom[n] for n in nbs[var]))
    return vals

def backtrack(dom, nbs, assign):
    if len(assign) == len(dom):
        print("SOLUTION:", assign); return True
    var = mrv(dom, assign)
    for val in lcv(var, dom, nbs):
        saved = {v: set(dom[v]) for v in dom}
        assign[var] = val
        dom[var] = {val}
        if ac3(dom, nbs) and backtrack(dom, nbs, assign): return True
        dom.update(saved); assign.pop(var, None)
    return False

def solve(file):
    k, vars, edges = read_input(file)
    nbs = defaultdict(set)
    for u, v in edges: nbs[u].add(v); nbs[v].add(u)
    dom = {v: set(range(1, k+1)) for v in vars}
    if not ac3(dom, nbs) or not backtrack(dom, nbs, {}): print("failure")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: python csp_input.py <file>"); sys.exit()
    solve(sys.argv[1])

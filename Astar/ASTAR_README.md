# How to run (Windows)
## A*:
  ### cd Astar
  ### python astar_input.py astar_small.txt
  ### python astar_input.py astar_medium.txt
  ### Each run prints MODE, Optimal cost, Path, Expanded, Pushes, Max frontier, Runtime(s)

# Implementation notes 
## A*: Three modes: UCS (h=0), A* Euclidean, A* Manhattan.f(n)=g(n)+h(n); duplicates allowed; deterministic tie-breaking.Tracks expansions, pushes, frontier, runtime.Path reconstruction from parent map.

# Analysis & Questions
## Optimality:
All three A* modes return the same optimal cost , heuristics are admissible and consistent.
## Efficiency:
UCS ≥ A* Euclidean ≈ A* Manhattan in expansions/runtime.
## Heuristic validity:
For all edges, weights ≥ heuristic distances , both heuristics admissible.

# Output
## A* Small:

MODE: UCS
Optimal cost: 8
Path: 1 -> 2 -> 4
Expanded: 3
Pushes: 4
Max frontier: 3
Runtime (s): 0.000039

MODE: A* Euclidean
Optimal cost: 8
Path: 1 -> 2 -> 4
Expanded: 3
Pushes: 4
Max frontier: 3
Runtime (s): 0.000058

MODE: A* Manhattan
Optimal cost: 8
Path: 1 -> 2 -> 4
Expanded: 3
Pushes: 4
Max frontier: 3
Runtime (s): 0.000028


## A* Medium:
MODE: UCS
Optimal cost: 19
Path: 1 -> 2 -> 3 -> 9 -> 15 -> 21 -> 27 -> 28 -> 29 -> 30
Expanded: 34
Pushes: 33
Max frontier: 9
Runtime (s): 0.000131

MODE: A* Euclidean
Optimal cost: 19
Path: 1 -> 2 -> 3 -> 9 -> 15 -> 21 -> 27 -> 28 -> 29 -> 30
Expanded: 33
Pushes: 32
Max frontier: 9
Runtime (s): 0.000191

MODE: A* Manhattan
Optimal cost: 19
Path: 1 -> 2 -> 3 -> 9 -> 15 -> 21 -> 27 -> 28 -> 29 -> 30
Expanded: 34
Pushes: 33
Max frontier: 9
Runtime (s): 0.000160

# A* and CSP:

## Repository contents
### astar_input.py — A* implementation (UCS, Euclidean, Manhattan)
### astar_small.txt, astar_medium.txt — A* input files
### csp_input.py — CSP graph coloring solver (Backtracking + MRV + LCV + AC-3)
### csp_small.txt, csp_tight.txt — CSP input files

## How to run (Windows)
### A*:
  ### python astar_input.py astar_small.txt
  ### python astar_input.py astar_medium.txt
  ### Each run prints MODE, Optimal cost, Path, Expanded, Pushes, Max frontier, Runtime(s)
### CSP:
  ### python csp_input.py csp_small.txt
  ### python csp_input.py csp_tight.txt
  ### Prints either `SOLUTION: {...}` or `failure`

## For details , see Astar/README.md and CSP/README.md.

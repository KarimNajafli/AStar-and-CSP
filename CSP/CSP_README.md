# How to run (Windows)
## CSP:
  ### cd CSP
  ### python csp_input.py csp_small.txt
  ### python csp_input.py csp_tight.txt
  ### Prints either `SOLUTION: {...}` or `failure`

# Implementation notes 
## CSP: Backtracking with MRV (smallest domain),LCV (least constraining value),AC-3 for arc consistency after each assignment.

# Analysis & Questions
## CSP behavior:
### Small graph (3-colorable): solved.
### Tight graph (K4): requires all 4 colors.
### Changing to colors=3 , returns failure.

# Output
## CSP Small:
SOLUTION: {1: 1, 2: 2, 3: 3, 4: 1}

## CSP Tight:
SOLUTION: {1: 1, 9: 2, 15: 3, 20: 4}
  

# CS4200 Project 2: N-Queen Local Search
Author: Kenzie Lam
Course: CS4200 - Artificial Intelligence

## How to Run This Program

### Requirements

Python 3.6 or higher
No external libraries required (uses standard Python libraries only)

### Files

hillClimbing.py - Hill climbing algorithm implementation
geneticAlgorithm.py - Genetic algorithm implementation  
analysis.py - Main experimental testing program

### Running the Main Program
```bash
python analysis.py
```
Features:
- Runs 100 trials for each algorithm automatically
- Displays success rates and performance statistics
- Shows sample solutions with board configurations
- Provides comparative analysis between algorithms

### Running Individual Algorithm Tests
Uncomment the last line in analysis.py:
```python
# test_individual_algorithms()  # Remove the # to enable
```
Then run:
```bash
python analysis.py
```
Features:
- Tests single instances of each algorithm
- Shows step-by-step board configurations
- Displays success status and iteration counts

### Expected Output Format
Algorithm performance statistics:
```
1. STEEPEST-ASCENT HILL CLIMBING
----------------------------------------
Success Rate: 14.0%
Average Iterations: 4.2
Average Time: 0.000823 seconds

2. GENETIC ALGORITHM
---------------------------------------- 
Success Rate: 95.0%
Average Generations: 150.3
Average Time: 0.045672 seconds
```

Sample board solutions:
```
Solution 1: [2, 5, 7, 0, 3, 6, 4, 1]
Board configuration:
. . Q . . . . .
. . . . . . . Q
Q . . . . . . .
. . . . Q . . .
. . . . . . Q .
. Q . . . . . .
. . . . . Q . .
. . . Q . . . .
Conflicts: 0
```

### Sample Usage

Run complete experimental analysis:
1. Run `python analysis.py`
2. Wait for 100 trials per algorithm to complete
3. Review success rates and sample solutions

Test individual algorithms:
1. Edit analysis.py and uncomment `test_individual_algorithms()`
2. Run `python analysis.py`
3. Observe single test results for each algorithm

Customize algorithm parameters:
1. Edit geneticAlgorithm.py to modify population_size, max_generations, or mutation_rate
2. Edit hillClimbing.py to modify max_iterations
3. Run analysis.py to test with new parameters

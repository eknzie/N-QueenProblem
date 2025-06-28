import time

from hillClimbing import HillClimbingSolver
from geneticAlgorithm import GeneticAlgorithmSolver

def run_experiments():
    """Run experiments and collect statistics"""
    n = 8
    num_trials = 100
    hc_solver = HillClimbingSolver(n)
    ga_solver = GeneticAlgorithmSolver(n)
    
    print(f"Running 100 trials for each algorithm on 8-Queen problem")
    print("=" * 60)
    
    # Test Steepest-Ascent Hill Climbing
    print("\n1. STEEPEST-ASCENT HILL CLIMBING")
    print("-" * 40)
    hc_success = 0
    hc_total_iterations = 0
    hc_times = []
    hc_solutions = []
    
    for i in range(num_trials):
        start_time = time.time()
        solution, success, iterations = hc_solver.steepest_ascent_hill_climbing()
        end_time = time.time()
        
        if success:
            hc_success += 1
            if len(hc_solutions) < 3:
                hc_solutions.append(solution.copy())
        
        hc_total_iterations += iterations
        hc_times.append(end_time - start_time)
    
    hc_success_rate = (hc_success / num_trials) * 100
    hc_avg_iterations = hc_total_iterations / num_trials
    hc_avg_time = sum(hc_times) / len(hc_times)
    
    print(f"Success Rate: {hc_success_rate:.1f}%")
    print(f"Average Iterations: {hc_avg_iterations:.1f}")
    print(f"Average Time: {hc_avg_time:.6f} seconds")
    
    # Test Genetic Algorithm
    print("\n2. GENETIC ALGORITHM")
    print("-" * 40)
    ga_success = 0
    ga_total_generations = 0
    ga_times = []
    ga_solutions = []
    
    for i in range(num_trials):
        start_time = time.time()
        solution, success, generations = ga_solver.genetic_algorithm()
        end_time = time.time()
        
        if success:
            ga_success += 1
            if len(ga_solutions) < 3:
                ga_solutions.append(solution.copy())
        
        ga_total_generations += generations
        ga_times.append(end_time - start_time)
    
    ga_success_rate = (ga_success / num_trials) * 100
    ga_avg_generations = ga_total_generations / num_trials
    ga_avg_time = sum(ga_times) / len(ga_times)
    
    print(f"Success Rate: {ga_success_rate:.1f}%")
    print(f"Average Generations: {ga_avg_generations:.1f}")
    print(f"Average Time: {ga_avg_time:.6f} seconds")
    
    # Display sample solutions
    print("\n" + "="*60)
    print("SAMPLE SOLUTIONS")
    print("="*60)
    
    algorithms = [
        ("Hill Climbing", hc_solutions, hc_solver),
        ("Genetic Algorithm", ga_solutions, ga_solver)
    ]
    
    for alg_name, solutions, solver in algorithms:
        print(f"\n{alg_name} Solutions:")
        print("-" * 30)
        for i, solution in enumerate(solutions):
            print(f"Solution {i+1}: {solution}")
            solver.print_board(solution)
    
    return {
        'hill_climbing': {
            'success_rate': hc_success_rate,
            'avg_iterations': hc_avg_iterations,
            'avg_time': hc_avg_time
        },
        'genetic_algorithm': {
            'success_rate': ga_success_rate,
            'avg_generations': ga_avg_generations,
            'avg_time': ga_avg_time
        }
    }

if __name__ == "__main__":
    # Run the experiments
    results = run_experiments()
    
    print("\n" + "="*60)
    print("ANALYSIS SUMMARY")
    print("="*60)
    print("\nAlgorithm Performance Comparison:")
    print(f"{'Algorithm':<20} {'Success Rate':<15} {'Avg Steps':<15} {'Avg Time (s)':<15}")
    print("-" * 65)
    
    for alg_name, data in results.items():
        alg_display = alg_name.replace('_', ' ').title()
        # Handle different key names (iterations vs generations)
        avg_steps = data.get('avg_iterations', data.get('avg_generations', 0))
        print(f"{alg_display:<20} {data['success_rate']:<14.1f}% {avg_steps:<14.1f} {data['avg_time']:<14.6f}")
    

def test_individual_algorithms():
    """Test individual algorithms for demonstration"""
    print("\n" + "="*60)
    print("INDIVIDUAL ALGORITHM TESTING")
    print("="*60)
    
    hc_solver = HillClimbingSolver(8)
    ga_solver = GeneticAlgorithmSolver(8)
    
    print("\nTesting Hill Climbing:")
    solution, success, iterations = hc_solver.steepest_ascent_hill_climbing()
    print(f"Success: {success}, Iterations: {iterations}")
    hc_solver.print_board(solution)
    
    print("\nTesting Genetic Algorithm:")
    solution, success, generations = ga_solver.genetic_algorithm()
    print(f"Success: {success}, Generations: {generations}")
    ga_solver.print_board(solution)

# Uncomment the line below to test individual algorithms
# test_individual_algorithms()
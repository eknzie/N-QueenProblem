import random
from typing import List, Tuple

class GeneticAlgorithmSolver:
    def __init__(self, n=8):
        self.n = n
        
    def generate_random_state(self) -> List[int]:
        """Generate a random initial state where state[i] represents the row of queen in column i"""
        return [random.randint(0, self.n-1) for _ in range(self.n)]
    
    def count_conflicts(self, state: List[int]) -> int:
        """Count the number of queen conflicts in the current state"""
        conflicts = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                # Same row
                if state[i] == state[j]:
                    conflicts += 1
                # Diagonal
                if abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    
    def genetic_algorithm(self, population_size=100, max_generations=1000) -> Tuple[List[int], bool, int]:
        # Initialize population
        population = [self.generate_random_state() for _ in range(population_size)]
        
        for generation in range(max_generations):
            # Calculate fitness for all individuals
            fitness_scores = []
            for individual in population:
                # Fitness = number of non-attacking pairs
                max_pairs = self.n * (self.n - 1) // 2
                conflicts = self.count_conflicts(individual)
                fitness = max_pairs - conflicts
                fitness_scores.append(fitness)
            
            # Check if we found a solution
            max_fitness = max(fitness_scores)
            if max_fitness == self.n * (self.n - 1) // 2:  # Perfect solution
                best_idx = fitness_scores.index(max_fitness)
                return population[best_idx], True, generation
            
            # Create new generation
            new_population = []
            total_fitness = sum(fitness_scores)
            
            # Ensure we don't divide by zero
            if total_fitness == 0:
                total_fitness = 1
            
            for _ in range(population_size):
                # Selection: fitness-proportionate selection
                parent1 = self.fitness_proportionate_selection(population, fitness_scores, total_fitness)
                parent2 = self.fitness_proportionate_selection(population, fitness_scores, total_fitness)
                
                # Crossover: single-point crossover
                child = self.crossover(parent1, parent2)
                
                # Mutation
                if random.random() < 0.1:  # Mutation probability
                    child = self.mutate(child)
                
                new_population.append(child)
            
            population = new_population
        
        # Return best individual from final generation
        fitness_scores = [self.n * (self.n - 1) // 2 - self.count_conflicts(ind) for ind in population]
        best_idx = fitness_scores.index(max(fitness_scores))
        return population[best_idx], self.count_conflicts(population[best_idx]) == 0, max_generations
    
    def fitness_proportionate_selection(self, population, fitness_scores, total_fitness):
        """Select an individual based on fitness proportionate selection"""
        pick = random.uniform(0, total_fitness)
        current = 0
        for i, fitness in enumerate(fitness_scores):
            current += fitness
            if current >= pick:
                return population[i]
        return population[-1]  
    
    def crossover(self, parent1, parent2):
        """Single-point crossover as shown in lecture slides"""
        crossover_point = random.randint(1, self.n - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child
    
    def mutate(self, individual):
        """Randomly change one queen's position"""
        mutated = individual.copy()
        col = random.randint(0, self.n - 1)
        mutated[col] = random.randint(0, self.n - 1)
        return mutated
    
    def print_board(self, state: List[int]):
        """Print the chessboard with queens"""
        print("Board configuration:")
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print(f"Conflicts: {self.count_conflicts(state)}")
        print()
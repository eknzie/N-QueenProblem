import random
from typing import List, Tuple

class HillClimbingSolver:
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
    
    def get_neighbors(self, state: List[int]) -> List[List[int]]:
        """Get all possible neighbors by moving one queen in each column"""
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if row != state[col]:  # Don't include current state
                    neighbor = state.copy()
                    neighbor[col] = row
                    neighbors.append(neighbor)
        return neighbors
    
    def steepest_ascent_hill_climbing(self, max_iterations=1000) -> Tuple[List[int], bool, int]:
        current = self.generate_random_state()
        current_conflicts = self.count_conflicts(current)
        
        for iteration in range(max_iterations):
            if current_conflicts == 0:
                return current, True, iteration
            
            neighbors = self.get_neighbors(current)
            best_neighbor = None
            best_conflicts = current_conflicts
            
            # Find the best neighbor (steepest ascent)
            for neighbor in neighbors:
                neighbor_conflicts = self.count_conflicts(neighbor)
                if neighbor_conflicts < best_conflicts:
                    best_neighbor = neighbor
                    best_conflicts = neighbor_conflicts
            
            # If no better neighbor found, we're stuck at local minimum
            if best_neighbor is None:
                return current, False, iteration
            
            current = best_neighbor
            current_conflicts = best_conflicts
        
        return current, current_conflicts == 0, max_iterations
    
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
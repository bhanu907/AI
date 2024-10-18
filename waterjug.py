from collections import deque

def water_jug_solver(capacity_a, capacity_b, goal):
    visited = set()
    queue = deque([(0, 0, [])])
    while queue:
        a, b, path = queue.popleft()
        
        if a == goal or b == goal:
            return path + [(a, b)]
        
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        
        # Possible actions
        actions = [
            (capacity_a, b),  # Fill jug A
            (a, capacity_b),  # Fill jug
            B
            (0, b),           # Empty jug A
            (a, 0),           # Empty jug B
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),  # Pour A into B
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a)),  # Pour B into A
        ]
        
        for action in actions:
            if action not in visited:
                queue.append((action[0], action[1], path + [(a, b)]))
    
    return None  # No solution found

def main():
    try:
        capacity_a = int(input("Enter the capacity of jug A (in liters): "))
        capacity_b = int(input("Enter the capacity of jug B (in liters): "))
        goal = int(input("Enter goal amount (in liters): "))
        
        if goal > max(capacity_a, capacity_b):
            print("The goal amount exceeds the capacity of both jugs.")
            return
        
        solution = water_jug_solver(capacity_a, capacity_b, goal)
        
        if solution:
            print("Solution found:")
            for step in solution:
                print(f"Jug A: {step[0]} , Jug B: {step[1]} ")
        else:
            print("No solution.")
    
    except ValueError:
        print("Please enter valid integers for the capacities and goal.")

if __name__ == "__main__":
    main()

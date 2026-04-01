# Map Coloring using CSP (Backtracking)

# Variables (regions)
regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Domain (colors)
colors = ['Red', 'Green', 'Blue']

# Constraints (adjacency list)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Check if assignment is valid
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def backtracking(assignment):
    # If all regions assigned → solution found
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    # Try all colors
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color

            result = backtracking(assignment)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None

# Run CSP
solution = backtracking({})

# Print result
if solution:
    print("Solution Found:")
    for region in solution:
        print(region, "→", solution[region])
else:
    print("No solution exists")

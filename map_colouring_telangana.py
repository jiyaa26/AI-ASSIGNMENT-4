# Telangana Map Coloring using CSP (Backtracking)

# List of districts (33)
districts = [
    "Adilabad","Komaram Bheem","Nirmal","Mancherial","Nizamabad","Jagitial",
    "Peddapalli","Karimnagar","Rajanna Sircilla","Kamareddy","Siddipet",
    "Medak","Sangareddy","Vikarabad","Hyderabad","Medchal","Ranga Reddy",
    "Yadadri","Bhadradri","Khammam","Mahabubabad","Warangal Urban",
    "Warangal Rural","Jangaon","Jayashankar","Mulugu","Nagarkurnool",
    "Mahabubnagar","Wanaparthy","Jogulamba","Gadwal","Narayanpet","Suryapet","Nalgonda"
]

# Colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Adjacency (simplified – enough for assignment)
neighbors = {
    "Adilabad": ["Komaram Bheem", "Nirmal"],
    "Komaram Bheem": ["Adilabad", "Mancherial"],
    "Nirmal": ["Adilabad", "Nizamabad"],
    "Mancherial": ["Komaram Bheem", "Peddapalli"],
    "Nizamabad": ["Nirmal", "Kamareddy"],
    "Jagitial": ["Karimnagar", "Peddapalli"],
    "Peddapalli": ["Mancherial", "Jagitial"],
    "Karimnagar": ["Jagitial", "Rajanna Sircilla"],
    "Rajanna Sircilla": ["Karimnagar", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Rajanna Sircilla"],
    "Siddipet": ["Medak", "Karimnagar"],
    "Medak": ["Siddipet", "Sangareddy"],
    "Sangareddy": ["Medak", "Vikarabad"],
    "Vikarabad": ["Sangareddy", "Ranga Reddy"],
    "Hyderabad": ["Medchal", "Ranga Reddy"],
    "Medchal": ["Hyderabad", "Yadadri"],
    "Ranga Reddy": ["Hyderabad", "Vikarabad"],
    "Yadadri": ["Medchal", "Suryapet"],
    "Bhadradri": ["Khammam", "Mulugu"],
    "Khammam": ["Bhadradri", "Mahabubabad"],
    "Mahabubabad": ["Khammam", "Warangal Rural"],
    "Warangal Urban": ["Warangal Rural", "Jangaon"],
    "Warangal Rural": ["Mahabubabad", "Warangal Urban"],
    "Jangaon": ["Warangal Urban", "Siddipet"],
    "Jayashankar": ["Mulugu"],
    "Mulugu": ["Jayashankar", "Bhadradri"],
    "Nagarkurnool": ["Mahabubnagar"],
    "Mahabubnagar": ["Nagarkurnool", "Wanaparthy"],
    "Wanaparthy": ["Mahabubnagar", "Jogulamba"],
    "Jogulamba": ["Wanaparthy", "Gadwal"],
    "Gadwal": ["Jogulamba", "Narayanpet"],
    "Narayanpet": ["Gadwal"],
    "Suryapet": ["Yadadri", "Nalgonda"],
    "Nalgonda": ["Suryapet"]
}

# Check constraints
def is_valid(region, color, assignment):
    for neighbor in neighbors.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking
def backtracking(assignment):
    if len(assignment) == len(districts):
        return assignment

    unassigned = [d for d in districts if d not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtracking(assignment)

            if result:
                return result

            del assignment[region]

    return None

# Run
solution = backtracking({})

# Output
if solution:
    print("Coloring Solution:\n")
    for d in solution:
        print(f"{d} → {solution[d]}")
else:
    print("No solution found")

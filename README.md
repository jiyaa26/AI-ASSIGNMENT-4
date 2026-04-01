**Map Coloring Problem of Australia using CSP**

Introduction

In this assignment, I have implemented the **Map Coloring Problem** using the concept of a **Constraint Satisfaction Problem (CSP)**. The aim is to assign colors to different regions of Australia in such a way that no two neighboring regions have the same color.

This is a classic problem in Artificial Intelligence and helps in understanding how constraints can be applied to find valid solutions.

---

Problem Statement

The task is to color the seven states and territories of Australia:
WA, NT, Q, SA, NSW, V, and T

The condition is simple:

* No two adjacent regions should have the same color.

---

Approach

To solve this problem, I used the **Backtracking algorithm**, which is a common technique used in CSP.

* Each region is treated as a variable.
* Each variable can take one of three colors: Red, Green, or Blue.
* The algorithm assigns colors one by one and checks if the assignment is valid.
* If a conflict occurs (same color for neighboring regions), it backtracks and tries a different color.

---

Constraints (Adjacency)

The neighboring relationships between regions are defined as follows:

* WA → NT, SA
* NT → WA, SA, Q
* SA → WA, NT, Q, NSW, V
* Q → NT, SA, NSW
* NSW → Q, SA, V
* V → SA, NSW
* T → No neighbors

---

How to Run the Code

1. Save the file as `map_coloring_csp.py` or `csp.py`
2. Open the terminal in the file location
3. Run the following command:

```bash
python3 csp.py
```

---

Output

The program will display a valid coloring of all regions.
Each region will be assigned a color such that no constraints are violated.

(Note: The exact colors may vary each time, but the solution will always be correct.)

---

What I Learned

* How CSP works in real problems
* Implementation of backtracking
* Importance of constraints in decision-making problems

---

Conclusion

This assignment helped me understand how problems with multiple conditions can be solved using CSP techniques. The backtracking approach ensures that all constraints are satisfied while still finding a valid solution efficiently.

---

**Map Coloring of Telangana using CSP**

Introduction

In this assignment, I extended the Map Coloring problem to the **33 districts of Telangana**. The goal is to assign colors to each district such that no two neighboring districts have the same color.

This problem is solved using the concept of a **Constraint Satisfaction Problem (CSP)**, which is commonly used in Artificial Intelligence.

---

Objective

To color all districts of Telangana in such a way that:

* Adjacent districts do not share the same color
* A limited number of colors is used efficiently

---

Approach

I used the **Backtracking algorithm** to solve this problem.

* Each district is treated as a variable
* Each variable can take one of the colors: Red, Green, Blue, or Yellow
* The algorithm assigns colors step by step
* If a conflict occurs, it goes back and tries a different color

This ensures that all constraints are satisfied.

---

Constraints

Each district has neighboring districts, and no two neighbors can have the same color. These relationships are stored in the form of an adjacency list in the code.

---

How to Run the Code

1. Save the file as `telangana_map_coloring.py`
2. Open terminal in the file location
3. Run:

```bash
python3 telangana_map_coloring.py
```

---

Output

The program prints a valid color assignment for all districts.

Each run may produce a different valid solution, but all constraints will always be satisfied.

---

What I Learned

* How CSP can be applied to real-world problems
* Implementation of backtracking for larger datasets
* Handling multiple constraints efficiently

---

Conclusion

This assignment helped me understand how scaling a CSP problem increases complexity and how backtracking helps in finding valid solutions. It also gave insight into solving real-life problems like map coloring using AI techniques.

---



**Sudoku Solver using CSP**

Introduction

In this assignment, I implemented a **Sudoku Solver** using the concept of a **Constraint Satisfaction Problem (CSP)**. Sudoku is a popular puzzle where numbers must be filled in a 9×9 grid following certain rules.

This problem is a good example of how CSP techniques can be applied to solve real-world logical puzzles.

---

Objective

To solve a given Sudoku puzzle such that:

* Each row contains numbers from 1 to 9 without repetition
* Each column contains numbers from 1 to 9 without repetition
* Each 3×3 subgrid contains numbers from 1 to 9 without repetition

---

Approach

I used the **Backtracking algorithm** to solve the Sudoku.

* Empty cells are treated as variables
* Possible values (1–9) form the domain
* Constraints ensure no repetition in rows, columns, and subgrids
* The algorithm fills cells one by one
* If a conflict occurs, it backtracks and tries another number

---

How It Works

1. Find an empty cell in the grid
2. Try numbers from 1 to 9
3. Check if the number is valid
4. If valid, assign it and move to next cell
5. If not, try another number
6. If no number works, backtrack

---

How to Run the Code

1. Save the file as `sudoku_csp.py`
2. Open terminal in the file location
3. Run:

```bash
python3 sudoku_csp.py
```

---

Output

The program prints the solved Sudoku grid.

If no solution exists, it will display a message accordingly.

---

What I Learned

* How CSP applies to puzzles like Sudoku
* Importance of constraints in problem solving
* Backtracking as a powerful solving technique

---

Conclusion

This assignment helped me understand how logical constraints can be used to systematically solve complex puzzles. The CSP approach ensures that all Sudoku rules are satisfied while efficiently finding a solution.

---



**Crypt-arithmetic Puzzle using CSP**

Introduction

In this assignment, I solved a **crypt-arithmetic puzzle** using the concept of a **Constraint Satisfaction Problem (CSP)**. The puzzle is:

SEND + MORE = MONEY

Each letter represents a unique digit, and the goal is to find the correct digit assignment that satisfies the equation.

---

Objective

To assign digits (0–9) to the letters such that:

* Each letter has a unique digit
* The arithmetic equation is satisfied
* Leading letters (S and M) are not zero

---

Approach

I used a **Backtracking approach with permutations** to solve this problem.

* All possible digit combinations are generated
* Each combination is checked against constraints
* Invalid assignments are discarded
* The correct solution is printed once found

---

Constraints

* No two letters can have the same digit
* S ≠ 0 and M ≠ 0 (no leading zeros)
* SEND + MORE = MONEY must hold true

---

How to Run the Code

1. Save the file as `cryptarithmetic_csp.py`
2. Open terminal in the file location
3. Run:

```bash
python3 cryptarithmetic_csp.py
```

---

Output

The program prints:

* The digit assigned to each letter
* The numerical values of SEND, MORE, and MONEY

---

What I Learned

* How CSP can be applied to arithmetic puzzles
* Importance of constraints in reducing search space
* Use of permutations and backtracking together

---

Conclusion

This assignment helped me understand how logical constraints and systematic search can solve puzzles that seem complex at first. CSP provides a structured way to approach such problems efficiently.

---




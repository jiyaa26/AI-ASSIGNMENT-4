# Crypt-arithmetic Puzzle: SEND + MORE = MONEY
# Using CSP (Backtracking)

from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')

# Digits 0–9
digits = range(10)

# Solve using permutations
for perm in permutations(digits, len(letters)):
    assign = dict(zip(letters, perm))

    # Leading digits cannot be zero
    if assign['S'] == 0 or assign['M'] == 0:
        continue

    # Form numbers
    SEND = 1000*assign['S'] + 100*assign['E'] + 10*assign['N'] + assign['D']
    MORE = 1000*assign['M'] + 100*assign['O'] + 10*assign['R'] + assign['E']
    MONEY = (10000*assign['M'] + 1000*assign['O'] +
             100*assign['N'] + 10*assign['E'] + assign['Y'])

    # Check equation
    if SEND + MORE == MONEY:
        print("Solution Found:\n")
        print(assign)
        print(f"\n{SEND} + {MORE} = {MONEY}")
        break

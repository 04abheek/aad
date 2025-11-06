from typing import List, Tuple

def mod_inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chinese_remainder_theorem(congruences: List[Tuple[int, int]]) -> int:
    M = 1
    for _, mod in congruences:
        M *= mod
    
    result = 0
    for remainder, mod in congruences:
        Mi = M // mod
        yi = mod_inverse(Mi, mod)
        result += remainder * Mi * yi
    
    return result % M

def main():
    # Example congruences: (remainder, modulus)
    congruences = [(2, 3), (3, 5), (2, 7)]
    solution = chinese_remainder_theorem(congruences)
    print("The solution to the constraint satisfaction problem is:", solution)

if __name__ == "__main__":
    main()

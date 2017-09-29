from ProjectEulerUtils import find_prime_factors, is_prime

ceiling_to_use = 600851475143
print max([p for p in find_prime_factors(ceiling_to_use) if is_prime(p)])
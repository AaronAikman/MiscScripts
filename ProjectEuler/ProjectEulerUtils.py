# Some help from Stack Overflow used for finding more efficient algorithms for factorials and the sieve of eratosthenes


def find_multiples(possible_multiples, ceiling):
    found_multiples = []
    for i in range(ceiling):
        found_some = False
        for multip in possible_multiples:

            if i % multip == 0:
                found_some = True
        if found_some:
            found_multiples.append(i)
    return found_multiples


def find_fib(ceiling):
    a,b,c = 1, 1, 1
    fib_list = []
    while a <= (ceiling):
        fib_list.append(a)
        c = a
        a += b
        b = c
    return fib_list


def find_prime_factors(ceiling):
    n = 2
    fac = []
    while n <= int(ceiling):
        B = 1
        while ceiling % n == 0:
            B = 0
            ceiling /= n
        if B == 0:
            fac.append(n)
        n += 1
    return fac

'''
Too Slow
def find_factors(ceiling):
    n = 1
    fac = []
    while n <= int(ceiling):
        is_fac = False
        if ceiling % n == 0:
            is_fac = True
        if is_fac:
            fac.append(n)
        n += 1
    return fac
'''


def find_factors(num):
    divisors = [1, num]
    for eachNum in range(2, int(num ** .5) + 1):
        if num % eachNum == 0:
            divisors += [eachNum]
            if num / eachNum != eachNum:
                divisors += [(num / eachNum)]
    return divisors


def is_prime(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            factors.append(i)
    if not factors:
        return True
    else:
        return False


def find_primes(ceiling):
    a = [True] * ceiling
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, ceiling, i):
                a[n] = False




def find_palindromic_number(digit_len):
    a = range((1*10**digit_len))
    b = a
    all_mults = []
    for i in a:
        for j in b:
            all_mults.append(i*j)
    pal_mults = [k for k in all_mults if str(k) == str(k)[::-1]]
    return max(pal_mults)


'''
Too Slow
def find_smallest_multiple(ceiling):
    n = ceiling
    while True:
        count = 0
        for j in range(1, ceiling+1):
            if n % j == 0:
                count += 1
        if count == ceiling:
            return n
        else:
            print '{} is only divisible by {} numbers'.format(n, count)
        n += 1
'''


def find_smallest_multiple(ceiling):
    i = 1
    ceiling += 1
    for k in range(1, ceiling):
        if i % k > 0:
            for j in range(1, ceiling):
                if (i*j) % k == 0:
                    i *= j
                    break
    return i


'''
Too Slow
def find_triangular_numbers():
    i = 1
    while True:
        a = 0
        for j in range(1,i):
            a += j
        yield a
        i += 1
'''

def find_triangular_numbers():
    b = 1
    res = 0
    while True:
        res += b
        #        print (b, res)
        yield res
        b +=1


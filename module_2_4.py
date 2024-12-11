numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers_)):
    if numbers_[i]<2:
        continue
    is_primes = True
    for j in range(2,numbers_[i]):
        if numbers_[i] % j == 0:
            not_primes.append(numbers_[i])
            is_primes = False
            break
    if is_primes:
        primes.append(numbers_[i])

print(primes)
print(not_primes)
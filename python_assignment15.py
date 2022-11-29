# Assignment 15
n = int (input("Please enter a number: "))
primes_list = []
i = 2
is_prime = False
while i<n:
    is_prime = True
    for k in range(2,i):
        if i%k == 0:
            is_prime = False
    if is_prime == True:
        primes_list.append(i)
    i += 1
print(primes_list)
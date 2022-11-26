#Assignment 14
f1 = 1
f2 = 1
i = 1
fibonacci = [f1, f2]
while i in range(9) : #Range ne kadar fazla olursa o kadar fazla fibonacci sayısı alırız.
  f3 = f1 + f2
  fibonacci.append(f3)
  f1 = f2
  f2 = f3
  i += 1
print(fibonacci)
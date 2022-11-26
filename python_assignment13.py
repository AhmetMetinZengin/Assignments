#Assignment 13
number = int(input("Enter a number to check if it is a prime number: "))
a = 2
while a <= number: #Eğer burada sqrt kullanabilseydik kod 100 000 000 civarı sayılara 1000 kat daha hızlı ulaşırdı.
  if a == number :
    print(f"{number} is a prime number.")
    break
  elif number % a == 0 :
    print(f"{number} is not a prime number.")
    break
  else :
    print(a)
    a += 1


#Assignment 13 improved
import math
number = int(input("Enter a number to check if it is a prime number: "))
a = 2
while a <= math.sqrt(number) + 1 : #Geliştirilmiş versiyon
      if number % a == 0 :
        print(f"{number} is not a prime number.")
        break
      elif a % 2 == 0 :
        a += 1
      elif a == math.ceil(math.sqrt(number)) : #ceil methodu üstteki en yakın sayıya yuvarlıyor.
        print(f"{number} is a prime number.")
        break
      else :
        a += 1
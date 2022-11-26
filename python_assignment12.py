#Assignment 12
while True : #Bu kısım sayının float, non-numeric veya negatif olmamasını sağlıyor.
      sayı = input("Please enter a positive integer:")
      if int(sayı.find(".")) != -1 :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
      elif sayı.isnumeric() == False :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
      elif abs(int(sayı))!=int(sayı) :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
      else :
       break
a = 0 #Bu kısım Armstrong sayısı olup olmadığını kontrol ediyor.
sayı_listesi = list(sayı)
for x in sayı_listesi :
  a = a + (int(x))**(len(sayı))
if a == int(sayı) :
  print(f"{sayı} is an Armstrong number.")
else :
  print(f"{sayı} is not an Armstrong number.")


#Assignment 12 Improved
b = 1
while True : #Bu kısım sayının float, non-numeric veya negatif olmamasını sağlıyor.
      sayı = input("Please enter a positive integer:")
      if int(sayı.find(".")) != -1 :
        if b == 1 :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
          b += 1
        elif b != 1 :
          print("Don't you know what a positive integer means? ENTER A POSITIVE INTEGER!!!")
      elif sayı.isnumeric() == False :
        if b == 1 :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
          b += 1
        elif b != 1 :
          print("Don't you know what a positive integer means? ENTER A POSITIVE INTEGER!!!")
      elif abs(int(sayı))!=int(sayı) :
        if b == 1 :
          print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
          b += 1
        elif b != 1 :
          print("Don't you know what a positive integer means? ENTER A POSITIVE INTEGER!!!")
      else :
       break
a = 0 #Bu kısım Armstrong sayısı olup olmadığını kontrol ediyor.
sayı_listesi = list(sayı)
for x in sayı_listesi :
  a = a + (int(x))**(len(sayı))
if a == int(sayı) :
  print(f"{sayı} is an Armstrong number.")
else :
  print(f"{sayı} is not an Armstrong number.")
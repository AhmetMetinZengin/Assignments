#Assignment 11
year = int(input("Bir sayı giriniz: "))
if year%4 == 0 :
  if year % 100 == 0 :
    if year % 400 == 0 :
      print(f"{year} is a leap year.")
    else :
      print(f"{year} is not a leap year.")
  else :
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")
#Assignment 9
my_name = "Joseph" #Assignment belirli bir şifrenin olduğunu söylüyordu.
password = "W@12" #O yüzden input() kullanmadım.
user_name = input("Please enter your name ")
if my_name == user_name :
  print(f"Hey {my_name}! Here's your password: {password}")
else :
  print(f"Hey {user_name}, nice try.")
#Assignment 10
age = (input("Are you a cigarette addict older than 75 years old? ") == "yes")
chronic = (input("Do you have a severe chronic disease? ") == "yes")
immune = (input("Is your immune system too weak? ") == "yes")
risk = age or chronic or immune
if risk == True :
  print("You have a high risk of being infected with Coronavirus.")
else :
  print("You don't have a risk of being infected with Coronavirus.")
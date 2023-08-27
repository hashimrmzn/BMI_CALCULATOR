


while True:
  name= str(input("Please enter your name: "))

  print("Now you are going to Calculate Your Bmi")

  print( name + "  you have to give me  yours's body informations like   ")
  try: 
   height = float(input("Enter your height in cm: "))
   weight = float(input("Enter your weight in kg: "))
  except ValueError:
            print("Invalid input. Try again.")
            continue

  BMI = weight / (height/100)**2
  print(f"You BMI is {BMI}")

  if BMI <= 18.4:
    print(name + " You are underweight.")
  elif BMI <= 24.9:
    print(name + " You are healthy.")
  elif BMI <= 29.9:
    print(name + " You are over weight.")
  elif BMI <= 34.9:
    print(name + " You are severely over weight.")
  elif BMI <= 39.9:
    print(name + " You are obese.")
  else:
    print(name + " You are severely obese.")

  
  again= input("Should I Calculate again:" )
  if again == 'no':
       print("Thanks For using me!")
       break
    
else:
     print("Invalid, choose the correct number for calculation :")
      
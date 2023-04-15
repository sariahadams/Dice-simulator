
#Dice roll simulator: Uses a the random module to generate a random number between the range from 1 to 6 when the user wants.

import random
#randomization feature

while True:
  print('1. Roll Dice') 
  print('2. Exit program')
  user = int(input("Pick an option\n"))
#Displays option choices for the user

  if user == 1:
    number = random.randint(1,6)
    
  #using random.randint activates the random module. We set a limit from 1 to 6 because this is the type of dice we're using

    print(number)

  else:
    print("Thanks for playing! Have a nice day!")
    break

#program ceases if user chooses option 2.

#End of program 

import random    # import random function for computer choice
def welcome(name):  # welcomes player 
  print ( f"hello",name) # greets player 

welcome("player")        # prints a welcome message 


# Ask user if they would like to play
# a game of Rock, Paper Scissors.

game=input("Would you like to play Rock-Paper-Scissors? (y- yes , n -no)").lower()    # Asks player if they would like to play
if game == "y":     # if user says yes 
 print ("Great lets play") # prints out response
elif game=="n":
   print("Thats Okay see you next time! ")   # if user says no prints this 
   exit()# exit the game if no is chosen 

print("------------------START-----------------------")


print(" Lets Battle!!") # start
throw= (" Rock- Paper -Scissors shoe !!!") # starts game 
print(throw)   # prints question 
print("Options:")
choices=["Rock",    # list 1  with choices 
         "Paper"
         ,"Scissors"]
print(choices) #prints list for user 

#Make a scoring system 

player_score= 0  # sets score to zero
computer_score=0 # sets score to zero 

# Start game loop

while True:  # while statment 
   #  computer_choice= throw[random.randint(0,2)] # uses random function to chose a value from 
  #list of choices
   
    computer_choice = random.choice(choices)
    score_track=f"Players score: {player_score} , Computer scorce:{ computer_score}" # keeps track of score between player and computer 
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    print("Please select a input...") # Asks user to chose a imput
    player_choice= input("'r'=Rock ,'p'= Paper,'s'=Scissors:") .lower() # gives user options and takes input 


 # player's choices and result determination
    if player_choice == 'r':
        player_choice = "Rock"
    elif player_choice == 'p':
        player_choice = "Paper"
    elif player_choice == 's':
        player_choice = "Scissors"
    else:
        print("Invalid input. Please choose 'r', 'p', or 's'.")
        continue  # Skip the rest of the loop and ask again if invalid input


    # Game logic for each possible outcome
    if player_choice == computer_choice:
        print("It's a tie!")
        player_score += 1
        computer_score += 1
        print("-------------------")
        print ( score_track)

    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        print(f"You win! {player_choice} beats {computer_choice}")
        player_score+= 1
        print("-------------------")
        print ( score_track)
    else:

      (player_choice == "Scissors" and computer_choice == "Rock") or \
      (player_choice == "Rock" and computer_choice == "Paper") or \
      (player_choice == "Paper" and computer_choice == "Scissors")
      print(f"You lose! {computer_choice} beats {player_choice}")
    computer_score+= 1
    print("-------------------")
    print ( score_track) #prints score_track for player to know score 

    # Ask if player wants to play again
    play_again = input("Play again? Enter 'y' for yes or 'n' for no: ").lower()
    if play_again != 'y':
        break  # Break the loop and end the game

# Print the final score of the game
print(score_track)  # Prints the final score
if computer_score > player_score:
    print("Computer wins the game!")
elif player_score > computer_score:
    print("Player wins the game!")
else:
    print("It's a tie!")




#Asks if player wants to play another round  (2nd time appearing)
play_again=input("Play again? Enter 'y' for yes or 'n' for no. ")
if input=='y': 
  print (player_choice)
if input=='n':
   print( "Alright")


# Print the final score of the game 
print ( score_track) # prints the final score 
if computer_score==player_score :
        print ("You guys tied no winner !")
elif computer_score < player_score :
   print (" Player has won the game ")
else: 
   computer_score > player_score 
   print (" Computer won the game ")





# Rate game 
def rate_game():  

   rating=input("Would you rate this game from one through ten ? (yes/no):")
   if rating=="yes":
         rate=int(input("Provide your rating (1-10):"))
         if 1 <=rate <= 10:
          print(f"Thank you for rating of {rate}! I hope to play agian soon!")
         else:
           print("Please enter a valid rating betweem 1 -10.")
   else:
         print ("Okay thank you for playing ")
rate_game()



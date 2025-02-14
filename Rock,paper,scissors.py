import random    # import random function for computer choice
def welcome(name):  # welcomes player 
  print ( f"hello",name) # greets player 
welcome("player")        # prints a welcome message 


# Ask user if they would like to play
# a game of Rock, Paper Scissors.

game=input("Would you like to play Rock-Paper-Scissors? (y- yes , n -no)").lower()    # Asks player if they would like to play
if game == "y":     # if user says yes 
 print ("Great lets play") # prints out response
elif game=="n":print("Thats Okay see you next time! ")   # if user says no prints this 


print(" Lets Battle!!") # start
throw= (" Rock- Paper -Scissors shoe ") # starts game 
print(throw)   # prints question 
choices=["Rock",    # list 1  with choices 
         "Paper"
         ,"Scissors"]
print(choices) #prints list for user 

#Make a scoring system 

player_score= 0  # sets score to zero
computer_score=0 # sets score to zero 

#Asks if player wants to play another round 
play_again = input("Play again? Enter 'y' for yes or 'n' for no. ") 
# if input=='y': 
#   # print (player_choice)
# if input=='n':
#    print( "Alright")


while True:  # while statment 
    computer_choice= throw[random.randint(0,2)] # uses random function to chose a value from 
  #list of choices
    score_track=f"Players score: {player_score} , Computer scorce:{ computer_score}" # keeps track of score between player and computer 
    print ( score_track) #prints score_track for player to know score 
    print("Please select a input") # Asks user to chose a imput
    player_choice= input("'r'=Rock ,'p'= Paper,'s'=Scissors:") .lower() # gives user options and takes input 


# Result options if player chosses Rock as input 
    if player_choice =='r':
        player_choice=="Rock"
    if computer_choice== player_choice:
     print("You are tied")
     computer_score+= 1 and player_score+1 # adds points to both computer and user if tie 
    elif computer_choice=="Paper":
      print ("Paper covers Rock! You lose this round ...")
      computer_score += 1    # keep track of score for computer 
    else:
      print("Rock crushes scissors!You win this round!!!")
      player_score+= 1   # Adds points to players score if they win 
      print (play_again)

#Result options if player chosses Paper as input 
    if player_choice=='p':
        player_choice="Paper"
    if computer_choice== player_choice:
         print("You are tied")
         computer_score+=1 and player_score+1 # adds points to both computer and user if a tie 
    elif computer_choice=="Scissors":
         print("Scissors cut paper! You lose this round... ")
         computer_score+= 1 # keep track of score for computer 
    else:
         print("Paper covers rock! You win !!!")
         player_score+=1  # Adds point to users score if they win 
         print (play_again)

#Results if player chosses Scissors as input 
    if  player_choice =='s':
       player_choice="Scisscors "
    if computer_choice== player_choice :
       print(" You are tied")
       computer_score+=1 and player_score+1 #adds points to both computer and user if a tie 
    elif computer_choice=="Rock":
       print("Rock crushes scissors!You lose this round...")
       computer_score+=1 # keep track of score 
    else:
       print("Scissors cut Paper!You win !!!")
       player_score=+1 # adds a point to users score if they win 
       print (play_again)
       break 
    

#Asks if player wants to play another round  (2nd time appearing)
play_again = input("Play again? Enter 'y' for yes or 'n' for no. ") 
if input=='y': 
  print (player_choice)
if input=='n':
   print( "Alright")


# Print the final score of the game 
print ( score_track) # prints the final score 
if computer_score!=player_score :
        print ("You guys tied no winner !")
elif computer_score < player_score :
   print (" Player has won the game ")
else: 
   computer_score > player_score 
   print (" Computer won the game ")





# Rate game 
def rate_game():  

   rating=input("Would you rate this gamefrom (1-10)(yes/no):")
   if rating=="yes":
         rate=int(input("Provide your rating (1-10):"))
         if 1 <=rate <= 10:
          print(f"Thank you for rating of {rate}! I hope to play agian soon!")
         else:
           print("Please enter a valid rating betweem 1 -10.")
   else:
         print ("Okay thank you for playing ")
rate_game()



# import random
# def welcome(name):  # welcomes player 
#   print ( f"hello",name) # greets player 
# welcome("player")

# game=input("Would you like to play Rock-Paper-Scissors? (y- yes , n -no)").lower()    # Asks player if they would like to play
# if game == "y":     # if user says yes 
#  print ("Great lets play")
# elif game=="n":print("Thats Okay see you next time! ")   # if user says no 

# question= (" Rock- Paper -Scissors shoe ") # starts game 
# print(question)
# choices={"Rock",
#          "Paper"
#          ,"Scissors"}

# "Rock"==1 # gives the choices values for user to chose 
# "Paper"==2
# "Scissors"==3
# print(choices)

# print("please chose a input...")
# get_player_choice=int(input("Rock(1),Paper(2),or Scissors(3) :"))

# if get_player_choice== 1:
#    get_player_choice=='Rock'
# elif get_player_choice== 2:
#    get_player_choice=="Paper"
# elif get_player_choice==3:
#   player_choice='Scissors'

# player_choice =get_player_choice()
# #--------------------computer choice 

# def get_computer_choice(): 
#     #use imported random function from library 
# computer_choice =get_computer_choice()
# choice = random.randint(1,3) 

# # ------------- give asigned values for later 
 
# #assign what the computer chose to rock, paper, or scissors 
# if choice == 1: 
#         choice = 'Rock' 
# elif choice == 2: 
#         choice = 'Paper' 
# else: 
#         choice = 'Scissors' 

#     #return value 
# print(choice) 
# computer_choice= choice
# #--------------------------------


# win=0      # set the values win ,lose, and tie to zero for later in game
# lose=0
# tie=0


# #----------------------------------------------------- 

# print(computer_choice)
# if computer_choice== player_choice:
#  if computer_choice =='Scissors' and player_choice=="Rock":
#   Result='Win' 
#   print("Rock has crushed the scissors !! You win this round !")
# elif computer_choice=='Rock' and player_choice=='Scissors':
#   Result='Lost'
#   print("Sadly the Rock has crushed the scissors. You lose...")
# elif computer_choice=='Paper' and player_choice=='Rock':
#    Result='Lost'
#    print("Sadly the Paper has covered the rock . You lose ...")
# elif computer_choice=='Rock' and player_choice=='Paper':
#    Result='Win'
#    print("Paper has covered Rock!You win!")
# elif computer_choice=='Scissors' and player_choice=="Paper":
#     Result='Lost'
# elif computer_choice=='Paper' and player_choice=="Scissors":
#    Results='Win'

# #-----Ask user to play another round 
# play_again = input("Play again? Enter 'y' for yes or 'n' for no. ") 
# if input=='y': 
#   print (question)
# if input=='n':
#    print( "Alright")

#  #---------------Scores
# player_score= 0
# computer_score=0
# Result=()
# def winner (computer_choice,player_choice):
# #-------------

#    if Result=='Lost':
#        computer_score + 1 
#    elif Result =="Win":
#      player_score+1
#    else: player_choice==computer_choice
# Result=="Tie"
# player_score+1 and computer_score+1


# Result='lose'
# print('you lost')

# def rate_game():  

#    rating=input("Would you rate this gamefrom (1-10)(yes/no):")
#    if rating=="yes":
#          rate=int(input("Provide your rating (1-10):"))
#          if 1 <=rate <= 10:
#           print(f"Thank you for rating of {rate}! I hope to play agian soon!")
#          else:
#            print("Please enter a valid rating betweem 1 -10.")
#    else:
#          print ("Okay thank you for playing ")
# rate_game()
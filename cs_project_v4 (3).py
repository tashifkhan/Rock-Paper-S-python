import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

'''
credit: ascii art from
“https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe”
'''

rule1 = '''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
rule2 = '''
If you win a match you get +1 points.
If you lose a match you get none.
In the case o12 rdff a draw, you do not get any points.
'''
rule3 = '''
Here you can choose how many rounds you want to play and the number of players.
All the players play rock paper scissors for the number of rounds specified
At the end player(s) with the max points win. 
''' 
rule4 = '''
You can play ROCK by typing either r or rock
Similarly for PAPER you can type p or paper
And for SCISSORS you can type s or scissors
'''
score = []
count = 0
option = [rock, paper, scissors]

print("Welcome to the game of ROCK PAPER SCISSORS")
print(" "*13 + "~Tashif, Sankalp & Sparsh")
print()
print()

print(rule1)
print(rule2)
print(rule3)
print(rule4)
print("_"*80)
num_players = int(input("how many players?\n"))
num_rounds = int(input("how many rounds?\n"))
print()
if num_players > 1:
  for j in range (1, num_players+1):
    count = 0
    print("Currently player", j, "is playing")
    print()
    for i in range (1, num_rounds+1):
      player_choice = input("What do you choose? rock, paper or scissors?\n")
      if player_choice.upper() == "ROCK" or player_choice.upper() == "R":
        num_player_choice = rock
        print(option[0])
      elif player_choice.upper() == "PAPER" or player_choice.upper() == "P":
        num_player_choice = paper
        print(option[1])
      elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S":
        num_player_choice = scissors
        print(option[2])
      else:
        print("incorrect input!")
        print()
        print("You broke the rules...")
        print("Go back and read the instructions again")
        print("and your session has been terminated")
        break

      computer_choice = random.choice(option)
      print("Computer chose:")
      print(computer_choice)

      if player_choice.upper() == "ROCK" or player_choice.upper() == "R" and computer_choice == scissors:
        count += 1
        print("you got +1")
        print()
      elif player_choice.upper() == "PAPER" or player_choice.upper() == "P" and computer_choice == rock:
        count += 1
        print("you got +1")
        print()
      elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S" and computer_choice == paper:
        count += 1
        print("you got +1")
        print()
      elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S" and computer_choice == rock:
        count += 0
        print("you didn't gain any point 😔")
        print()
      elif player_choice.upper() == "ROCK" or player_choice.upper() == "R" and computer_choice == paper:
        count += 0
        print("you didn't gain any point 😔")
        print()
      elif player_choice.upper() == "PAPER" or player_choice.upper() == "P" and computer_choice == scissors:
        count += 0
        print("you didn't gain any point 😔")
        print()
      elif computer_choice == num_player_choice:
        count += 0
        print("you didn't gain any point... it was a draw😐")
        print()
      
    print("score of player " + str(j) + " = " + str(count))
    score.append(count)
    print("_"*63)
    print()
#max_score is the maximum score
#temp_score is used to determine if two people scored the same maximum score
  max_score = max(score)
  temp_score = []
  for x in range(len(score)):
    if score[x] == max_score:
      temp_score.append(x)
  if max_score == 0:
    print("You all lost")
  elif len(temp_score) == 1:
    print("player", temp_score[0]+1, "won")
  else:
    print("players", end=" ")
    for z in temp_score:
      print(z+1, end=",")
    print(" won")

elif num_players == 1:
  for k in range (1, num_rounds+1):
    player_choice = input("what do you choose? rock, paper or scissors?\n")
    if player_choice.upper() == "ROCK" or player_choice.upper() == "R":
        num_player_choice = rock
        print(option[0])
    elif player_choice.upper() == "PAPER" or player_choice.upper() == "P":
        num_player_choice = paper
        print(option[1])
    elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S":
        num_player_choice = scissors
        print(option[2])
    else:
      print("incorrect input!")
      print()
      print("please enter one of the following:")
      print("rock, paper or scissors")

    computer_choice = random.choice(option)
    print("Computer chose:")
    print(computer_choice)
  
    if player_choice.upper() == "ROCK" or player_choice.upper() == "R" and computer_choice == scissors:
      count += 1
      print("you got +1")
      print()
    elif player_choice.upper() == "PAPER" or player_choice.upper() == "P" and computer_choice == rock:
      count += 1
      print("you got +1")
      print()
    elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S" and computer_choice == paper:
      count += 1
      print("you got +1")
      print()
    elif player_choice.upper() == "SCISSORS" or player_choice.upper() == "S" and computer_choice == rock:
      count += 0
      print("you didn't gain any point 😔")
      print()
    elif player_choice.upper() == "ROCK" or player_choice.upper() == "R" and computer_choice == paper:
      count += 0
      print("you didn't gain any point 😔")
      print()
    elif player_choice.upper() == "PAPER" or player_choice.upper() == "P" and computer_choice == scissors:
      count += 0
      print("you didn't gain any point 😔")
      print()
    elif computer_choice == num_player_choice:
      count += 0
      print("you didn't gain any point... it was a draw😐")
      print()

  print("you scored:", count)
  print()
  if count > num_rounds//2:
    print("well done!")
    print("you won 🙂")
  else:
    print("you lost 😔")

#made by TASHIF AHMAD KHAN, SANKALP KATYAYANAN & SPARSH AGGARWAL
print("made by TASHIF AHMAD KHAN, SANKALP KATYAYANAN & SPARSH AGGARWAL")

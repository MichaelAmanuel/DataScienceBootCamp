# -*- coding: utf-8 -*-
"""Rock_Paper_Scissor_Michael.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FcCmMPQW8Bw64sUtdqzVpuHjAmL0Rrqp
"""

# Rock smashes scissirs
# Paper cover  rock
# Sissirs cut paper


import random

def game(user, com):
  if user == 'rock':
    if com == 'sissir':
      return 'You won'
    elif com == 'paper':
      return 'computer won'
    else:
      return 'the game is tie'

  elif user == 'paper':
    if com == 'rock':
      return 'You won'
    elif com == 'sissir':
      return 'computer won'
    else:
      return 'the game is tie'

  elif user == 'sissir':
    if com == 'saper':
      return 'You won'
    elif com == 'sock':
      return 'computer won'
    else:
      return 'the game is tie'

def check_result(result):
    if result == 'You won':
        return False

    elif result == 'the game is tie':
        print('The game is tie')

    elif result == 'computer won':
        print('The Computer won')


def coun_game():
    game_play = True
    while game_play:
        possible_action = ['rock', 'paper', 'sissir']
        user_input = input('select from Rock, Paper and Sissir.  ')
        com = random.choice(possible_action)

        print(f"The computer selects {com}")
        result = game(user_input, com)
        if check_result(result) == False:
            game_play = False

    print('Congrats you won the game')
    if input('Do you want to play agine? Write y for Yes n for No.') == 'y':
        coun_game()
    else:
        exit()
coun_game()

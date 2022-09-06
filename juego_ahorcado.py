import random
import unicodedata
from os import system
from time import sleep
from assets import *

lst = []
lives = 6

def clear():
  _ = system('clear')
  print(header + "\n")
  
def get_word():
  words = []
  with open("./data.txt", "r", encoding="utf-8") as f:
    for word in f:
      words.append(word)
  word = random.choice(words)
  word = ''.join((c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn'))
  return word.upper()

def print_hang_man():
  global lives
  if lives == 6:
    print(hang0)
  elif lives == 5:
    print(hang1)
  elif lives == 4:
    print(hang2)
  elif lives == 3:
    print(hang3)
  elif lives == 2:
    print(hang4)
  elif lives == 1:
    print(hang5)
  elif lives == 0:
    print(hang6)

def start(word):
  global lst
  listed_word = list(word)
  listed_word.remove('\n')
  for i in range(len(word) - 2):
    if i == 0:
      lst.append(listed_word[i])
    lst.append("_")
  print_hang_man()
  print("\n" + str(lst))
  game(word)

def end_game(word):
  global lives
  if lives <= 0:
    clear()
    print_hang_man()
    print("\nPerdiste\n\nLa palabra era: \n")
    print(word)
  else:
    clear()
    print(win)
    print("\nGanaste!!!!!!!!\n")
  
def game(word):
  global lst
  listed_word = list(word)
  listed_word.remove('\n')
  while lst != listed_word:
    global lives
    if lives <= 0:
      break
    select = input("\nIntroduce una letra: \n").upper()
    if(len(select) > 1):
      lives -= 1
      print("\nIngresa solo una letra, has perdido un intento\n")
      sleep(1)
    if(word.find(select) == -1):
      lives -= 1
      print("\nUps esa letra no esta, has perdido un intento\n")
      sleep(1)
    for pos, char in enumerate(word):
      if(char == select):
        lst[pos] = select
    clear()
    print_hang_man()
    print("\n" + str(lst))
    print("\nAdivina la palabra!")
  end_game(word)
    
def run():
  word = get_word()
  clear()
  start(word)

if __name__ == '__main__':
  run()

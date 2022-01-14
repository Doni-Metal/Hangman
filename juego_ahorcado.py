import random
import unicodedata
from os import system
from time import sleep
from assets import *

def clear():
  _ = system('clear')

def get_word():
  words = []
  with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for word in f:
      words.append(word)
  word = random.choice(words)
  word = ''.join((c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn'))
  return word.upper()

lst = []
lives = 6

def print_hang_man():
  global lives
  if lives == 6:
    print(hang0)
  if lives == 5:
    print(hang1)
  if lives == 4:
    print(hang2)
  if lives == 3:
    print(hang3)
  if lives == 2:
    print(hang4)
  if lives == 1:
    print(hang5)


def start(word):
  for i in range(len(word) -1):
    lst.append("_")
  print(header)
  print(hang0)
  print("\nAdivina la palabra!\n")
  print(*lst)

def game(word):
  global lives
  if lives == 0:
    raise Exception
  select = input("\nIntroduce una letra: \n").upper()
  if(len(select) > 1):
    lives -= 1
    print("\nIngresa solo una letra\n")
    sleep(2)
  if(word.find(select) == -1):
    lives -= 1
    print("\nUps esa letra no esta\n")
    sleep(2)
  else:
    for pos, char in enumerate(word):
      if(char == select):
        lst[pos] = select
  try:
    if(lst.index("_")):
      clear()
      print(header)
      print_hang_man()
      print("\nAdivina la palabra!\n")
      print(*lst)
      game(word)
  except ValueError:
    clear()
    print(header + "\n")
    print(win)
    print(*lst)
    print("\nGanaste!!!!!!!!\n")
  except Exception as ex:
    clear()
    print(header)
    print(hang6)
    print("\nPerdiste\nLa palabra era: ")
    print(word)
    


def run():
  word = get_word()
  clear()
  print(word)
  start(word)
  game(word)
  


if __name__ == '__main__':
  run()
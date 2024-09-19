import random
import time

print("smol doge health 25, attk 15, defense 15")
print("buff doge health 90, attk 60, defense 60")
print("emotional damage health 100, attk 70, defense 90")
print("gigachad health 175, attk 110, defense 100")
print("Galaxy brain health 125, attk 125, defense 125")
print()

print("your deck:") 
print("1 smol doge")
print("2 smol doge")
print("3 smol doge")
print("4 buff doge")
print("5 buff doge")
print("6 emotional damage")
print("7 emotional damage")
print("8 gigachad")
print("9 gigachad")
print("10 GalaxyBrain")

items = ["bonk bat","biblically accurate sandwich","uno reverse card","dyson soul harvester"]
monsters = ["stonks","kentucy fried cat","among us","Noot Noot","MRBeast","pop cat","pepe the frog","Rush E","john cena","kirby"]
player_deck = ["smol doge","smol doge","smol doge","buff doge","buff doge","emotional damage", "emotional damage","gigachad","gigachad","GalaxyBrain"]
player_ded_card = []
boss_cards = ["Ronald McDonald destroyer of worlds","The Rolling Of The Ricks"]
current_monster = monsters[random.randint(0,9)]
ememy_move = random.randint(1,3)
current_card = player_deck[random.randint(0,9)]
enemy_defend = False
player_defend = False

def monster_setup():
  global enemy_attk
  global enemy_def
  global enemy_health
  global enemy_max_health
  if current_monster == "stonks":
    enemy_max_health = 45
    enemy_health = 45
    enemy_attk = 35
    enemy_def = 55
  elif current_monster == "kentucy fried cat":
    enemy_max_health = 75
    enemy_health = 75 
    enemy_attk = 45
    enemy_def = 45
  elif current_monster == "among us":
    enemy_max_health = 80
    enemy_health = 80
    enemy_attk = 65
    enemy_def = 55
  elif current_monster == "Noot Noot":
    enemy_max_health = 35
    enemy_health = 35
    enemy_attk = 85
    enemy_def = 30
  elif current_monster == "MRBeast":
    enemy_max_health = 115
    enemy_health = 115
    enemy_attk = 75
    enemy_def = 45
  elif current_monster == "pop cat":
    enemy_max_health = 60
    enemy_health = 60
    enemy_attk = 50
    enemy_def = 85
  elif current_monster == "pepe the frog":
    enemy_max_health = 65
    enemy_health = 65
    enemy_attk = 75
    enemy_def = 45
  elif current_monster == "Rush E":
    enemy_max_health = 60
    enemy_health = 60
    enemy_attk = 95
    enemy_def = 60
  elif current_monster == "john cena":
    enemy_max_health = 115
    enemy_health = 115
    enemy_attk = 100
    enemy_def = 110
  elif current_monster == "kirby":
    enemy_max_health = 125
    enemy_health = 125
    enemy_attk = 105
    enemy_def = 125
def card_setup():
  global player_attk
  global player_hp
  global player_def
  global player_max_health
  if current_card == "smol doge":
    player_max_health = 25
    player_hp = 25
    player_attk = 15
    player_def = 15
  elif current_card == "buff doge":
    player_max_health = 90
    player_hp = 90
    player_attk = 60
    player_def = 60
  elif current_card == "emotional damage":
    player_max_health = 100
    player_hp = 100
    player_attk = 70
    player_def = 90
  elif current_card == "gigachad":
    player_max_health = 175
    player_hp = 175
    player_attk = 110
    player_def = 100
  elif current_card == "GalaxyBrain":
    player_max_health = 125
    player_hp = 125
    player_attk = 125
    player_def = 125
def enemy_move():
  global player_defend
  global player_hp
  global player_def
  global enemy_health
  global enemy_defend
  if ememy_move == 1:
    if player_defend == True:
      print("the enemy attacked")
      player_def -= enemy_attk
      if player_def <= 0:
        print("you ran out of defence")
        player_hp -= 10
        player_defend = False
      else:
        print("you blocked the attack")
        player_defend = False
    else:
      print("the enemy atttack and dib", enemy_attk,"damage")
      player_hp -= enemy_attk
  elif ememy_move == 2:
    print("the enemy defends")
    enemy_defend = True
  else:
    enemy_health += 10
    if enemy_health > enemy_max_health:
      enemy_health = enemy_max_health
      print("enemy is at max halth already")
    else:
      print("emeny heald")
      
def death_function():
  if player_hp <= 0:
    player_ded_card.append(current_card)
    player_deck.remove(current_card)
    print("your current card died")
    current_card = player_deck[random.randint(0,9)]
    print("your new card is",current_card)
    card_setup()

      
def player_choice_3Paths():
  choice = input("which path do you choose?")
  print("1. left")
  print("2. forward")
  print("3. right")
  if choice == 1:
    print("you go left")
  elif choice == 2:
    print("you go forward")
  elif choice == 3:
    print("you go right")
  else:
    print("you go forward")

def player_choice_2Paths():
  choice = input("which path do you choose?")
  print("1. left")
  print("2. right")
  if choice == 1:
    print("you go left")
  elif choice ==2: 
    print("you go right")

def fight_sequence():
  global player_def
  global player_attk
  global enemy_def
  global enemy_health
  global player_hp
  global enemy_defend
  global player_defend
  while player_hp <= 0:
    death_function()
  print("you have encountered a",current_monster)
  print("your current card is",current_card)
  print("1. attack")
  print("2. defend")
  print("3. heal")
  check = "wong"
  while check == "wong":
    fight_choice = int(input("what do you want to do "))
    if fight_choice == 1:
      check = "V"
      if enemy_defend == True:
        enemy_def -= player_attk
        if enemy_def <= 0:
          enemy_health -= 10
          enemy_defend = False
        else:
          print("the enemy blocked the attack")
          enemy_defend = False
      else:
        enemy_health -= player_attk
        print("you did", player_attk,"damage")
    elif fight_choice == 2:
      check = "N"
      print("you defend")
      player_defend = True
    elif fight_choice == 3:
      check = "J"
      player_hp += 25
      if player_hp > player_max_health:
        player_hp = player_max_health
        print("you are already at max health")
      else:
        print("you healed")
    else:
      print("twry a gian")
  enemy_move()
##############################################################
card_setup()
monster_setup()
fight_sequence()
death_function()
player_deck += player_ded_card
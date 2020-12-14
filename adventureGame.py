import time

def initialization():
  player_char1 = input('enter a direction (N or S): ')
  try:
      if player_char1 == 'N':
          print('You went North')
          bearScenario() # this chain of events is mostly done
      if player_char1 == 'S':
          print('You went South')
          cabinScenario()
  except ValueError:
      print('That is not a valid input! ')


class player:
  def _init_(self, name, health = 100):
      self.name = name
      self.health = health


def bearScenario(): # If you go North You meet a bear...
   time.sleep(1)
   # Scenario:
   print('\nYou encounter a bear now what do you do?! ')
   # Answer choices:
   print('     [A] You stab the bear')
   print('     [B] your run the opposite direction')
   print('     [C] you give up and curl up into a ball')
   bear_char = input().upper()
   try:
       if bear_char == "A": # North -> Meet bear -> Stab bear ->
           print('\nThe bear gets the knife and STABS YOU BACK but you '
                 'punch it in the face and take it back! ')
           player.health = 60 # Player loses health
           print(' player health reduced to ' + str(player.health) + '!')
           stabbing = input('\nQuick! enter S to stab it back! ').upper()
           stabs = 0
           while stabbing == 'S': # Stabbing Action part of answer choice 'A'
               print('STAB! ')
               print('SHANK!')
               stabs += 1
               time.sleep(.3)
               if stabs == 2:
                   stabs = 0
                   stabbing = 'Not S' # Incrementing variable to a random var not 'S'
                   deadBear()
       if bear_char == 'B': # North -> Meet bear -> Run away ->
           mommaSpider()
       if bear_char == 'C': # North -> Meet bear -> Scared ->
           print('\nThe Bears attacks you and you die!! ')
           restart() # Asks to play again?
   except ValueError:
       print('that is not a valid input! ')


def deadBear(): # North -> Meet bear -> Stab Bear ->
   time.sleep(1)
   # Scenario:
   print('\nYou killed the bear, now what do you do? ')
   # Answer choices:
   print('     [A] youre hungry so you eat the meat ')
   print('     [B] Youre cold so you skin the bear and wear the skin ')
   print('     [C] You feel bad for killing the bear so you break down and cry ')
   deadBear_char1 = input().upper()
   try:
       if deadBear_char1 == 'A': # North -> Meet bear -> Stab Bear -> Eat Bear ->
           print('\nDelicious! but... ')
           print('\n You get very sick due to eating the raw meat...')
           player.health = 30
           print(' player health increased to ' + str(player.health) + '!')
           foodPoisoning()
       if deadBear_char1 == 'B': # North -> Meet bear -> Stab Bear -> Wear Bear ->
           print('\nThe dead bear skin attracts vultures that start to pick at you! ')
           player.health = 20
           print(' player health reduced to ' + str(player.health) + '!')
           vultures()
       if deadBear_char1 == 'C': # North -> Meet bear -> Stab Bear -> Father Bear
           print('\nThe father bear comes devastated that you stabbed his wife so he eats you! ')
           restart()
   except ValueError:
       print('sorry that is not a valid input! ')


def mommaSpider(): # Go North -> Meet bear -> Run Away ->
   # Scenario:
   print('\nYou fall in a hole full of spiders! You freak out and'
         'start to scream at the top of your lungs!')
   time.sleep(1)
   print('\noh no.....')
   time.sleep(1)
   print('\nthe MOTHER spider heard you and is returning to her HOLE!! ')
   print('\nThe Momma spider starts to eat you! It took your arm already! What now?!')
   # Answer choices:
   print('     [A] Scream for help at the top of your lungs! ') # North -> Meet bear -> Run away -> Grab Spider
   print('     [B] you pretend to be a spider ') # North -> Meet bear -> Run away -> Be a Spider
   print('     [C] you stand stand completely still and hope the spider wont see you move ') # North -> Meet bear -> Run away -> Stand Still
   mommaSpider_char1 = input().upper()
   try:
       if mommaSpider_char1 == 'A':
           print('\nSpiderman heard you and came to save you and you lived happily ever after! Congradulations!!')
           restart()
       if mommaSpider_char1 == 'B':
           print('\nThe mom thinks you are a spider and feeds you spider milk ')
           print('The milk was not meant for human consumption and you slowly turn into a spider!')
           player.health = 50
           print(' player health reduced to ' + str(player.health) + '!')
           houseSpider()
       if mommaSpider_char1 == 'C':
           print('\nIts not a T-rex, they can still see you... ')
           print('\nYou get eaten')
           restart()
   except ValueError:
       print('sorry that is not a valid input! ')

def houseSpider():
   # Scenario:
   print('\nYou become very tiny and venture into someones cabin in the woods! ')
   # Answer choices:
   print('     [A] You become curious and start to crawl around... ')
   print('     [B] you stay in the corner because you dont understand what is happening and youre scared' )
   houseSpider_char1 = input().upper()
   try:
       if houseSpider_char1 == "A":
           print('\nThe witch that lives in the house was missing a spider ingredient! ')
           print('\nYou get thrown into a boiling cauldron... and die. ')
           restart()
       if houseSpider_char1 == "B":
           print('\nThe lady that lives in the house screams, grabs a broom and youre done.! ')
           restart()
   except  ValueError:
       print('sorry that is not valid input! ')

def vultures():
   # Scenario:
   print('\nYou become very veak and are half picked alive... but you hear something.. ')
   # Answer choices:
   print('     [A] Crawl and go check it out... ')
   print('     [B] Youre terrified and weak so you stay in place. ')
   vultures_char1 = input().upper()
   try:
       if vultures_char1 == "A":
           print('\nThe vultures circling you got a trucks attention who came to see why there was vultures in the sky ')
           print('\nYou get saved by the man! ')
           restart()
       if vultures_char1 == "B":
           print('\nThe vultures continue to eat you and they eat very good, and you died.. ')
           restart()
   except  ValueError:
       print('sorry that is not valid input! ')

def foodPoisoning():
   # Scenario:
   print('\nYou become very veak ill because of the raw meat... your stomach is in pain')
   # Answer choices:
   print('     [A] You swear you passed a river so you trace back your steps..')
   print('     [B] You sit down to rest... ')
   foodPoisoning_char1 = input().upper()
   try:
       if foodPoisoning_char1 == "A":
           river()
       if foodPoisoning_char1 == "B":
           print('\nYou sit besides a tree and close your eyes.. ')
           time.sleep(.5)
           print('but... ')
           time.sleep(.8)
           print('you slowly start to drift away to bed...')
           time.sleep(1)
           print('and never wake up again...')
           restart()
   except  ValueError:
       print('sorry that is not valid input! ')

def river():
   # Scenario:
   print('\nYou find the river!')
   # Answer choices:
   print('     [A] You run to it as fast as you can!')
   print('     [B] You carefully walk towards it... ')
   river_char1 = input().upper()
   try:
       if river_char1 == "A":
           print('This giant eagle swoops out of nowhere and just lets out a huge cry and feeds you to her babies..')
           restart()
       if river_char1 == "B":
           print('\nYou get to the river and you drink water with your hands... ')
           time.sleep(.6)
           drinking = input('\nQuick! enter D to drink water! ').upper()
           drinks = 0
           while drinking == 'D':  # drinking Action part of answer choice 'B'
               print('GULP! ')
               print('gulp!')
               drinks += 1
               time.sleep(.3)
               if drinks == 2:
                   drinks = 0
                   drinking = 'Not D'  # Incrementing variable to a random var not 'D'
                   print('\nYou accidentally ingest a piranha... no further details needed to know what happen...')
                   restart()
   except  ValueError:
       print('sorry that is not valid input! ')


    #South choices

def cabinScenario(): # If you go South you find a cabin.
  time.sleep(1)
  # Scenario:
  print('\nYou see a cabin in an open area. What do you do? ')
  # Answer choices:
  print('     [A] You enter the cabin')
  print('     [B] You keep walking')
  print('     [C] You look around')
  cabin = input().upper()
  try:
      if cabin == "A": # South -> find cabin -> enter cabin ->
          print('\nThe door is unlocked. You open to find a man cleaning his gun. Startled at your intrusion, the man shoots you instantly! ')
          player.health = 30 # Player loses health
          print(' player health reduced to ' + str(player.health) + '!')
          stabbing = input('\nQuick! Enter S to stab the man  ').upper()
          stabs = 0
          while stabbing == 'S': # Stabbing Action part of answer choice 'A'
              print('STAB! ')
              stabs += 1
              time.sleep(.3)
              if stabs == 2:
                  stabs = 0
                  stabbing = 'Not S' # Incrementing variable to a random var not 'S'
                  deadMan()
      if cabin == 'B': # South -> find cabin -> keep walking ->
          angryWolf()
      if cabin == 'C': # South -> find cabin -> look around ->
          print('\nYou peer through the window to see a man cleaning his gun. Glad you had not barged in, you knock on his door')
          print('\nThe man answers the door. He looks at you, his gun at his side')
          print('\nTurns out he is super nice, and drives you back into town. Wow that really worked out ')
          restart()
  except ValueError:
      print('that is not a valid input! ')

def deadMan():  # South -> Get shot -> Stab Man ->
  time.sleep(1)
  # Scenario:
  print('\nYou killed the man, now what do you do? ')
  # Answer choices:
  print('     [A] You look around and loot him ')
  print('     [B] You take his gun and get out of the cabin!')
  print('     [C] You feel bad for killing the man. Overcome by guilt, you fall to your knees and start crying. Also, you are bleeding profusely and you die. ')
  deadMan_char1 = input().upper()
  try:
      if deadMan_char1 == 'A':  # South -> enter cabin -> Stab man -> loot man ->
          print('\nYou find a first aid kit and heal yourself. Youre still bleeding, but you will be fine for now. Fortunately, you find car keys and leave the cabin to see if you can drive off ')
          player.health = 90
          print(' player health increased to ' + str(player.health) + '!')
          carScenario()
      if deadMan_char1 == 'B':  # South -> enter cabin -> Stab man -> gun ->
          print('\nThe gun has a couple rounds in it, so you feel somewhat better. Unfortunately, you forgot to check for first aid, and you lose some health as you bleed from your wound')
          player.Health = 20
          print(' player health reduced to ' + str(player.health) + '!')
          gameHunter()
      if deadMan_char1 == 'C':  # South -> enter cabin -> Stab man -> bleed out ->
          player.Health = 0
          print(' player health reduced to ' + str(player.health) + '!')
          restart()
  except ValueError:
      print('sorry that is not a valid input! ')


def carScenario(): # car
  time.sleep(1)
  # Scenario:
  print('\nYou find cabin mans car parked behind his house. What do you do? ')
  # Answer choices:
  print('     [A] You get in and drive to the nearest town')
  print('     [B] You steal his stuff and find a gun in the glove compartment')
  print('     [C] You take the gasoline from his car and set everything on fire')
  car = input().upper()
  try:
      if car == "A": # South -> find cabin -> enter cabin ->
          print('\nYou drive back into town, feeling uneasy, but glad to be alive. You recover at the nearest hospital. ')
          player.health = 100 # Player recovers health
          print(' player health increased to ' + str(player.health) + '!')
          print('\nToo bad the police arent as thrilled youre alive and well. They arrest you for murder, as you killed cabin man then stole his car. Youll be going away for a long time, sicko')
          restart()
      if car == 'B': # South -> find cabin -> keep walking ->
          largeOwl()
      if car == 'C': # South -> find cabin -> look around ->
          print('\nSmart move, covering your tracks.')
          print('\nUnfortunately, you light yourself on fire in the process')
          print('\nAs you slowly burn to death, you wonder why you did this. Why did you do this?  ')
          player.health = 0  # Player loses health
          print(' player health decreased to ' + str(player.health) + '!')
          restart()
  except ValueError:
      print('that is not a valid input! ')


def angryWolf(): # South -> find cabin -> keep walking ->
  time.sleep(1)
  # Scenario:
  print('\nYou walk mindlessly until you bump into something. You look down and see a wagging tail. The wolf, however, is far from happy.')
  time.sleep(1)
  print('\nBet you wish it was a puppy')
  time.sleep(2)
  print('\nThe wolf jumps back and bares its fangs. Time for a showdown. What do you do? ')
  # Answer choices:
  print('     [A] You stab the wolf') # South -> find cabin -> keep walking -> stab wolf
  print('     [B] You run away ') # South -> find cabin -> keep walking ->
  print('     [C] You get on all fours and pretend to be a dog to confuse it ') # South -> find cabin -> keep walking ->
  angryWolf_char1 = input().upper()
  try:
      if angryWolf_char1 == 'A':
          print('\nYou stab the wolf. You feel bad because you watch Game of Thrones and you love the Stark family, but you gotta do what you gotta do ')
          print('\nYou manage to hurt it and scare it off, but it still sunk its teeth into your arm before fleeing ')
          player.health = 80  # Player loses health
          print(' player health reduced to ' + str(player.health) + '!')
          stabbing = input('\nQuick! Enter S to stab the wolf  ').upper()
          stabs = 0
          while stabbing == 'S':  # Stabbing Action part of answer choice 'A'
              print('STAB! ')
              stabs += 1
              time.sleep(.3)
              if stabs == 2:
                  stabs = 0
                  stabbing = 'Not S'  # Incrementing variable to a random var not 'S'
                  gameHunter()
      if angryWolf_char1 == 'B':
          print('\nYou cannot outrun an apex predator. As you are eaten, you wish you watched more David Attenborough narrated documentaries on Animal Planet. Probably still would have died though  ')
          restart()
      if angryWolf_char1 == 'C':
          print('\nThat was really stupid. The wolf is not amused. Honestly, this was natural selection.')
          print('\nYou get eaten')
          restart()
  except ValueError:
      print('sorry that is not a valid input! ')

def gameHunter(): # Go south -> take gun ->
  time.sleep(1)
  # Scenario:
  print('\nYoure walking and bleeding and bleeding and walking. Suddenly, you hear voices!')
  time.sleep(1)
  print('\nOut of the woods, two hunters come out laughing and talking loudly. You stand still, hoping not to startle them ')
  time.sleep(2)
  print('\nThe hunters are startled anyway. Youre bleeding and holding a gun. Not exactly subtle ')
  print('\nThey point their guns at you as you do likewise. Seems pretty tense. bad time to be bleeding out')
  player.health = 10  # Player loses health
  print(' player health reduced to ' + str(player.health) + '!')
  print('\nI know. Harsh. Anyway, what do you do?')
  # Answer choices:
  print('     [A] Drop your weapon and ask for help ')
  print('     [B] Shoot at them ')
  gameHunter_char1 = input().upper()
  try:
      if gameHunter_char1 == 'A':
          print('\nThey rush to help you and drive you back into town. Unfortunately, youre still bleeding out  ')
          player.health = 5  # Player loses health
          print(' player health reduced to ' + str(player.health) + '!')
          print('\nYou barely make it to the hospital, where you are treated for your wounds and make a full recovery')
          player.health = 100  # Player restores health
          print(' player health increased to ' + str(player.health) + '!')
          print('\nHappy ending! Yay! Except not really, as you are charged by the police for trespassing and murder, for the death of the cabin owner. At least you stopped bleeding out?')
          restart()
      if gameHunter_char1 == 'B':
          print('\nYou cock the gun, but manage to trip over a rock as you charge to shoot at the hunters')
          print('\nRidiculous. Not only your decision, but also your execution. ')
          print('\nYou fall to the ground, as the hunters shoot you dead in self defense')
          restart()
          # function
  except ValueError:
      print('sorry that is not a valid input! ')


def largeOwl(): # South -> find cabin -> keep walking ->
  time.sleep(1)
  # Scenario:
  print('\nYou run as fast as you can away from the cabin. You run as fast you can right into a tree. Unfortunately, it was occupied')
  time.sleep(1)
  print('\nA large, snowy owl looks down at you from its perch. It looks like Hedwig, but if Hedwig ate Hedwig. Its talons flexed menacingly.')
  time.sleep(2)
  print('\nThe Owl spreads its wings, preparing to attack you. Quick, what do you do?! ')
  # Answer choices:
  print('     [A] Shoot it quick') # South -> find cabin -> keep walking -> stab wolf
  print('     [B] Stab it as it comes at you ') # South -> find cabin -> keep walking ->
  print('     [C] Hold your ground, dont make any moves ') # South -> find cabin -> keep walking ->
  largeOwl_char1 = input().upper()
  try:
      if largeOwl_char1 == 'A':
          print('\nYou aim your gun at it but it comes at you before you have time to think')
          print('\nIt slashes your arm with its talons, but you push it off before you get it in your sights ')
          player.health = 40  # Player loses health
          print(' player health reduced to ' + str(player.health) + '!')
          shooting = input('\nQuick! Enter S to shoot the owl!  ').upper()
          shots = 0
          while shooting == 'S':  # Shooting Action part of answer choice 'A'
              print('BOOM! ')
              shots += 1
              time.sleep(.3)
              if shots == 2:
                  shots = 0
                  shooting = 'Not S'  # Incrementing variable to a random var not 'S'
          print('\nYou kill the owl, but suddenly you hear a screeching all around you. Youre surrounded by large, angry owls flying at you.')
          print('\nAs youre being torn to shreds, you wish you were a wizard')
          restart()
      if largeOwl_char1 == 'B':
          print(
              '\nWhy would you stab it if you had a gun? It leaves you barely breathing')
          player.health = 20  # Player loses health
          print(' player health reduced to ' + str(player.health) + '!')
          stabbing = input('\nQuick! Enter S to stab the owl  ').upper()
          stabs = 0
          while stabbing == 'S':  # Stabbing Action part of answer choice 'A'
              print('STAB! ')
              stabs += 1
              time.sleep(.3)
              if stabs == 2:
                  stabs = 0
                  stabbing = 'Not S'  # Incrementing variable to a random var not 'S'
                  print('\nYoure left bleeding but victorious. You decide to keep on walking, delirious and bleeding out, but alive.')
                  gameHunter()
      if largeOwl_char1 == 'C':
          print('\nDeath was swift. Dont know what you were expecting')
          print('\nGood for you, though. You had a gun AND a knife, but you chose to abstain from murder. Well, murder of animals.')
          print('\nPETA would be proud')
          restart()
  except ValueError:
      print('sorry that is not a valid input! ')

def restart(): # Happens when you complete game or die
  restartQ = input('\nWould you like to play again!? Enter [Y] or [N] ').upper()
  if restartQ == 'Y':
      main() # 'Yes' ... Starts Initialization() indirectly
  if restartQ == 'N':
      exit() # 'No' ... Exits Game


def main():
  initialization() # Starts Chain reaction of events


main()

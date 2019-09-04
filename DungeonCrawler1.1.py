import math
import random


class Room:
    def __init__(self, coordinate):
        self.x = int(coordinate / 10)
        self.y = coordinate % 10
        xysum = self.x + self.y
        self.monsterattack = 1 + random.randrange(0, math.ceil(xysum), 1)
        self.monsterhealth = 1 + random.randrange(0, math.ceil(xysum), 1)
        self.defenseitem = 1 + random.randrange(0, 2, 1)
        self.attackitem = 1 + random.randrange(0, 2, 1)
        if self.x == 1 and self.y == 1:
            # top right left corner
            self.monsterattack = 0
            self.monsterhealth = 0
            self.doors = (21, 12)
        elif self.x == 9 and self.y == 1:
            # top right corner
            self.doors = (81, 92)
        elif self.x == 1 and self.y == 9:
            # bottom left corner
            self.doors = (29, 18)
        elif self.x == 9 and self.y == 9:
            # bottom right corner
            self.doors = (89, 98)
        elif self.x == 1:
            # left border
            self.doors = (self.x * 10 + self.y - 1, self.x * 10 + self.y + 1, (self.x + 1) * 10 + self.y)
        elif self.x == 9:
            # right border
            self.doors = (self.x * 10 + self.y - 1, self.x * 10 + self.y + 1, (self.x - 1) * 10 + self.y)
        elif self.y == 1:
            # top border
            self.doors = ((self.x - 1) * 10 + self.y, (self.x + 1) * 10 + self.y, self.x * 10 + self.y + 1)
        elif self.y == 9:
            # bottom border
            self.doors = ((self.x - 1) * 10 + self.y, (self.x + 1) * 10 + self.y, self.x * 10 + self.y - 1)
        else:
            # center block
            self.doors = (
                (self.x - 1) * 10 + self.y, (self.x + 1) * 10 + self.y, self.x * 10 + self.y - 1,
                self.x * 10 + self.y + 1)

        if self.x == 9 and self.y == 9:
            self.containsexit = True
        else:
            self.containsexit = False


# create and initialize all rooms
rooms = {}
for address in list(range(11, 100)):
    # print(address, math.ceil((int(address/10) + address%10)/2))
    rooms[address] = Room(address)
    print(rooms[address].x, rooms[address].y, rooms[address].monsterattack, rooms[address].monsterhealth, rooms[address].doors)

# set up values for player's current stats, ie location, etc
playerattack = 1
playerdefense = 1
currentlocation = 11
health = 3
wongame = False

print('Game Starts')

while not wongame and health > 0:
    defeatedmonster = False
    combatinput = ''

    # divider
    print('-----------------------------------------------------------------------------------------------------------')

    # displays current location + doors
    print('You are currently in room with coordinates:', currentlocation)
    print('There are doors leading to:', rooms[currentlocation].doors)

    # displays monster info. asks if player wants to attack
    if rooms[currentlocation].monsterhealth == 0 or rooms[currentlocation].monsterattack == 0:
        defeatedmonster = True
        if currentlocation == 11:
            print('This is the starting room and there are no monsters.')
        else:
            print('The monster here has been defeated already.')
    else:
        print('There is a monster in this room with atk of:', rooms[currentlocation].monsterattack,
              'and defense of:',
              rooms[currentlocation].monsterhealth)
        if currentlocation == 99:
            print('This is the room with the exit door. If you defeat the monster in this room you win the game!')
            print('You can also retreat from the monster and leave through a door as usual.')
            print('TIP: If you are not ready/confident, you can always loot other rooms first to improve your stats.')
        else:
            print(
                'You can fight this monster to obtain the loot in this room, or simply leave the room through a door.')
        playerscore = playerattack + playerdefense
        monsterscore = rooms[currentlocation].monsterattack + rooms[currentlocation].monsterhealth
        ratio = playerscore / monsterscore
        diceroll = random.randrange(0, 200, 1)
        if ratio > 2:
            percent = 100
        else:
            percent = ratio/2*100
        print('The chance of winning against this monster is:', '%.1f' % percent, 'percent')
        combatinput = input(
            'Do you want to fight this monster? "Y" or "y" for "Yes", all other inputs equate to "No"')

    # block to calculate combat stuff
    if combatinput == 'Y' or combatinput == 'y':
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! COMBAT RESULTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        playerscore = playerattack + playerdefense
        monsterscore = rooms[currentlocation].monsterattack + rooms[currentlocation].monsterhealth
        ratio = playerscore / monsterscore
        diceroll = random.randrange(0, 200, 1)
        if ratio >= 2:
            percent = 100
        else:
            percent = ratio/2*100
        if diceroll >= ratio*100:
            dead = True
            print('You lost in combat after fighting with a winning chance of:', '%.1f' % percent, 'percent.')
            health = health - 1
            print('You now have', health, "health left.")
            if health <= 0:
                break
        else:
            print('You successfully defeated the monster after fighting with a winning chance of:', '%.1f' % percent,
                  'percent. ')
            rooms[currentlocation].monsterhealth = 0
            defeatedmonster = True

    # displays stats of item and calculates stat changes
    if defeatedmonster:
        if currentlocation == 99:
            wongame = True
            break
        if rooms[currentlocation].attackitem == 0 or rooms[currentlocation].defenseitem == 0:
            print('The items in this room have already been looted.')
        else:
            print('You find some items that boost your attack by:', rooms[currentlocation].attackitem,
                  'and your defense by:', rooms[currentlocation].defenseitem)
            playerattack = playerattack + rooms[currentlocation].attackitem
            playerdefense = playerdefense + rooms[currentlocation].defenseitem
            print('Your new attack is:', playerattack, 'and your new defense is:', playerdefense)
            rooms[currentlocation].attackitem = 0
            rooms[currentlocation].defenseitem = 0

    # handles player choice in moving to the next room
    rawdoorinput = input('Which room do you travel to? Enter coordinates: ')
    if rawdoorinput.isdigit() and int(rawdoorinput) in rooms[currentlocation].doors:
        currentlocation = int(rawdoorinput)
    else:
        while not(rawdoorinput.isdigit() and int(rawdoorinput) in rooms[currentlocation].doors):
            print('Invalid door. Please enter a purely numeric door number from the displayed list of available doors.')
            print(rooms[currentlocation].doors)
            rawdoorinput = input('Which room do you travel through? Enter coordinates: ')

    currentlocation = int(rawdoorinput)

if health <= 0:
    print('You have lost all of your health. Game Over.')
if wongame:

    print('*************   Congratulations, you won!   *************')

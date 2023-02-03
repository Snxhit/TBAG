# Importing modules required.
import time
import random
import tabulate
from tabulate import tabulate









#Initializing variables required
playerLvl = 1
noOfDeaths = 0 #Currently on hold
playerStatus = 'alive'
playerGold = 500
keyFound = False
choice1 = None
notChoice1 = None
cx1 = None
bx1 = None
statTableHead = ["Stats", "Amount"]
statsTable = None
trsChestGold = None
trsChestGoldMD = None
buyShop = None
shopVisited = False
metalDetectorFound = False
armorWorn = False
swordEquipped = False
map1F = False
map2F = False
map3F = False








#Defining functions 1
def die(): #1
    #print('You have died. Try again next time.')
    time.sleep(2)
    playerStatus = 'dead'
    exit()
def lvlUp(): #2
    print('Congratulations, you have leveled up.')
    time.sleep(2)
def g1(): #3
    None
def g2(): #4 
    None
def trsChest(): #5
    None







#Stats table [NOT WORKING -- EDIT AFTER VARIABLES ARE MODIFIED.]
statsTable = [
    ["Player Level", playerLvl],
    ["Player Gold", playerGold],
    ["Shop unlocked?", keyFound]
]
#NOT USED






#Lists
caveList1 = [1,1,1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5, 6,6,6,6,6,6,6,6,6,6,6]
caveList2 = [1,1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5]
caveList3 = [1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
caveList4 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
buildList1 = [1,1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5]
buildList2 = [1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
buildList3 = [1, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
buildList4 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3, 4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
trsChestGoldList = [500, 500, 600, 750, 800, 800, 850, 900, 1000]
trsChestGoldListMD = [600, 700, 900, 900, 1300, 1400, 1500]






#Starting of the game
print('Welcome, adventurer!')
print('----------------------------------------')
print('      You have been stranded alone...')
print('      ...in the petrifying, dark forest...')
print('      ...the forest of the undead.')
print('      Play wisely.')
print('      For your life depends on this.')
print('----------------------------------------')
print('You look infront of you... and find an entrance to a cave, and a very old commercial building. There is also a shop...')







#some bullshitery
while True:
    print('----------------------------------')
    print('Now, where would you like to go?')
    time.sleep(0.5)
    print('Type "stats" to view your statistics.')
    notChoice1 = input('Choose wisely (building, cave, shop).: ')
    choice1 = notChoice1.lower()
    print('----------------------------------')







#choice1 = CAVE
    if choice1 == 'cave':
        if armorWorn == False:
            if swordEquipped == False:
                cx1 = random.choice(caveList1)
                if cx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif cx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif cx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif cx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif cx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif cx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound]], headers=statTableHead, tablefmt="grid"))
                    die()
            if swordEquipped == True:
                cx1 = random.choice(caveList3)
                if cx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif cx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif cx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif cx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif cx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif cx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound]], headers=statTableHead, tablefmt="grid"))
                    die()
        if armorWorn == True:
            if swordEquipped == False:
                cx1 = random.choice(caveList2)
                if cx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif cx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif cx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif cx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif cx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif cx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))
                    die()
            if swordEquipped == True:
                cx1 = random.choice(caveList4)
                if cx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif cx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif cx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif cx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif cx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif cx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))
                    die()







#choice1 = BUILDING
    if choice1 == 'building':
        if armorWorn == False:
            if swordEquipped == False:
                bx1 = random.choice(buildList1)
                if bx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif bx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif bx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif bx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif bx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif bx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound]], headers=statTableHead, tablefmt="grid"))
                    die()
            if swordEquipped == True:
                bx1 = random.choice(buildList3)
                if bx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif bx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif bx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif bx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif bx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif bx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound]], headers=statTableHead, tablefmt="grid"))
                    die()
        if armorWorn == True:
            if swordEquipped == False:
                bx1 = random.choice(buildList2)
                if bx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif bx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif bx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif bx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif bx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif bx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))
                    die()
            if swordEquipped == True:
                bx1 = random.choice(buildList4)
                if bx1 == 2:
                    lvlUp()
                    playerLvl += 1
                elif bx1 == 3:
                    if metalDetectorFound == False:
                        print('You stumbled upon 100 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 100
                    if metalDetectorFound == True:
                        print('You stumbled upon 100 Gold, found 100 more with Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                elif bx1 == 4:
                    if metalDetectorFound == False:
                        print('You stumbled upon 200 Gold.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 200
                    if metalDetectorFound == True:
                        print('You stumbled upon 200 Gold, found 200 more with the help of your Metal Detector.')
                        print('You swiftly pick it up and put it in your bag')
                        time.sleep(1)
                        playerGold += 400
                elif bx1 == 5:
                    if metalDetectorFound == False:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGold = random.choice(trsChestGoldList)
                        time.sleep(2)
                        print('You found ' + str(trsChestGold))
                        playerGold += trsChestGold
                    if metalDetectorFound == True:
                        print('Oooh! Shiny! You found a treasure chest!')
                        print('You open it and you found...')
                        trsChestGoldMD = random.choice(trsChestGoldListMD)
                        time.sleep(2)
                        print('You found ' + str(trsChestGoldMD))
                        playerGold += trsChestGoldMD
                elif bx1 == 6:
                    print('You found a key made of gold!')
                    print('This looks like a key to a very safe vault.')
                    time.sleep(2)
                    keyFound = True
                elif bx1 == 1:
                    print('You have died. Better luck next time!')
                    print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))
                    die()






#choice1 = SHOP
    if choice1 == 'shop':
        if keyFound == False:
            print('EH?! Who\'re you kid?! Get lost.')
            print('*You were kicked out of the shop*')
        if keyFound == True:
            if shopVisited == False:
                print('Oh? You found the key to my shops secret stash?!')
                time.sleep(2)
                shopVisited = True
                print('Well? It\'s a surprise. I lost that key in those darned caves 30 years ago...')
                time.sleep(2)
                print('That day... I don\' wanna ever remember it again...')
                time.sleep(2)
                print('*The old man cries*')
                time.sleep(1)
                print('[...]')
                time.sleep(1)
                print('[...]')
                time.sleep(1)
                print('[...]')
                time.sleep(2)
                print('Well, I will go, unlock that ol\' stash of mine. Come back later if ya needa\' buy sumth!')
                time.sleep(2)
                print('Also, thanks! This old man\'ll neva forget ya!')
                time.sleep(2)
                print('*You leave the shop.*')
                continue
            if shopVisited == True:
                print('Welcome back, kid.')
                time.sleep(2)
                shopVisited == True
                print('Well? Would you like to buy something this time around?')
                time.sleep(3)
                print("\n".join(['I\'ve got: ', ' -----------------------------------------------' , ' |  1• Lithium Armor - 2,000G', ' |  2• Lithium Sword - 1,000G', ' |  3• Metal Detector - 3,000G', ' |  4• Map 1 - 5,000G', ' |  5• Map 2 - 10,000G', ' |  6• Map 3 - 20,000G', ' -----------------------------------------------']))
                time.sleep(2)
                print('You have got', str(playerGold), 'on you right now.')
                time.sleep(1)
                print('Pssst.. You might find a way back \'ome if ya can buy those 3 maps im sellin\'!')
                time.sleep(3)
                buyShop = input('Now, what do you want to buy? (Use 1, 2, 3, 4, 5, 6) ')
                if buyShop == '1':
                    if armorWorn == False:
                        if playerGold > 2000:
                            print('Alright kiddo. Heres your Lithium Armor.')
                            time.sleep(1)
                            print('*Successfully bought and equipped Lithium Armor. Increased defense stat.*')
                            time.sleep(2)
                            armorWorn = True
                            playerGold -= 2000
                        elif playerGold < 2000:
                            print('You trynna fool me, huh?')
                            print('Go get some Gold for yourself first, kid.')
                    elif armorWorn == True:
                        print('Ya already own this!')
                elif buyShop == '2':
                    if swordEquipped == False:
                        if playerGold > 1000:
                            print('Alright kiddo. Heres your Lithium Sword.')
                            time.sleep(1)
                            print('*Successfully bought and equipped Lithium Sword. Increased defense, attack stat.*')
                            time.sleep(2)
                            swordEquipped = True
                            playerGold -= 1000
                        elif playerGold < 1000:
                            print('You trynna fool me, huh?')
                            print('Go get some Gold for yourself first, kid.')
                    elif swordEquipped == True:
                        print('Ya already own this!')
                elif buyShop == '3':
                    if metalDetectorFound == False:
                        if playerGold > 3000:
                            print('Heres your Metal Detector.')
                            time.sleep(1)
                            print('*Successfully bought and equipped Metal Detector. Gold finding rate increased.*')
                            time.sleep(2)
                            metalDetectorFound = True
                            playerGold -= 3000
                        elif playerGold < 3000:
                            print('You trynna fool me, huh?')
                            print('Go get some Gold for yourself first, kid.')
                    elif metalDetectorFound == True:
                        print('Ya already own this!')
                elif buyShop == '4':
                    if map1F == False:
                        if playerGold > 5000:
                            if playerLvl >= 10:
                                print('Congrats on gettin\' the first map!')
                                time.sleep(1)
                                print('*You are a step closer to finishing!*')
                                playerGold -= 5000
                                map1F = True
                            elif playerLvl < 10:
                                print('Sorry! You don\'t have enough levels! (Required: 10)')
                        elif playerGold < 5000:
                                print('Gotta get sum money on ya\' folk!')
                    elif map1F == True:
                        print('Ya already own this!')
                elif buyShop == '5':
                    if map2F == False:
                        if playerGold > 10000:
                            if playerLvl >= 20:
                                print('Congrats on gettin\' the second map!')
                                time.sleep(1)
                                print('*You are a step closer to finishing!*')
                                playerGold -= 10000
                                map2F = True
                            elif playerLvl < 20:
                                print('Sorry! You don\'t have enough levels! (Required: 10)')
                        elif playerGold < 10000:
                                print('Gotta get sum money on ya\' folk!')
                    elif map2F == True:
                        print('Ya already own this!')
                elif buyShop == '6':
                    if map3F == False:
                        if playerGold > 20000:
                            if playerLvl >= 30:
                                print('Congrats on gettin\' the last map!')
                                time.sleep(1)
                                print('*You are a step closer to finishing!*')
                                playerGold -= 20000
                                map3F = True
                            elif playerLvl < 30:
                                print('Sorry! You don\'t have enough levels! (Required: 10)')
                        elif playerGold < 20000:
                                print('Gotta get sum money on ya\' folk!')
                    elif map3F == True:
                        print('Ya already own this!')






#choice1 = STATS
    elif choice1 == 'stats':
        time.sleep(1)
        print('Here are your stats!')
        time.sleep(1)
        print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))




#THE END!!!!
    if map1F == True:
        if map2F == True:
            if map3F == True:
                print('--------------------------------------------------')
                print('Congratulations. You have successfully finished the game.')
                print('Goodbye, adventurer.')
                print('*You found the way back home...*')
                time.sleep(2)
                print('Here are your final stats...')
                time.sleep(1)
                print(tabulate([["Player Level", playerLvl],["Player Gold", playerGold],["Key found?", keyFound],["Armor worn?", armorWorn],["Sword Equipped?", swordEquipped]], headers=statTableHead, tablefmt="grid"))
                time.sleep(3)
                print('--------------------------------------------------')
                time.sleep(1)
                print('                  [+--]')
                time.sleep(1)
                print('                  [-+-]')
                time.sleep(1)
                print('                  [--+]')
                time.sleep(1)
                print('                  [-+-]')
                time.sleep(1)
                print('                  [+--]')
                time.sleep(1)
                print('                  [-+-]')
                time.sleep(1)
                print('                  [--+]')
                print('--------------------------------------------------')
                time.sleep(2)
                exit()
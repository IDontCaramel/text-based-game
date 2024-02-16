import os
import pystyle
from pystyle import Colors, Colorate
from pystyle import Write, Colors
import time
import random
import string

# controls
# north / n
# east / e
# south / s
# west / w
# inspect / i
# look / l
# inventory / inv
# use / u 


running = True


code = (''.join(random.choice('1234567890') for i in range(4)))


 
def Main_Game(inv=' '):
    os.system("cls")
    

    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    Write.Print(dialog, Colors.green ,interval= 0.0025)
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")

    if inv == 'DEATH':
        exit()
    elif inv != ' ':
        print(Colorate.Color(Colors.light_blue, f'you got {inv}', 1))
        print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
        inv = ''
    else:
        pass
    
    Player_Input = input("what are you going to do:")
        
    Player_Input = Player_Input.lower()
    Player_Input = Player_Input.strip(' ')
    
    if Player_Input == 'dev':
        devcom(Player_Input)
        
    elif Player_Input == 'help':
        help()  
               
    else:
        Room_Check(Player_Input)


            
    
def help():
    global dialog
    dialog = '''these are all the valid comands in the game
    
north / n
moves player north

east / e
moves player east 

south / s
moves player south

west / w
moves player west

inspect / i
inspects the item you want to inspect
example command: "inspect garbage"

look / l
looks around the room

inventory / inv
shows you the items in ur inventory
'''
    Main_Game()

    
def Inspect_Item(Player_input):
    global inventory
    global dialog

    item = Player_input.split()
    
    if len(item) < 2:
        dialog = "Please specify an item to inspect. \n"
        return
    
    item_name = item[1]
    
    if Curent_Room == 1:
        Inspect_Room_1(item_name)
    elif Curent_Room == 2:
        Inspect_Room_2(item_name)
    elif Curent_Room == 5:
        Inspect_Room_5(item_name)


def Inspect_Room_1(item_name):
    global dialog
    global inventory
    global Curent_Room
    
    inv = ' '
    
    if item_name in ['matress', 'matres']:
        if 'knife' not in inventory:
            dialog = '''You walk to the matress and look at it. It's quite musty and has a few stains.
Then you turn it over and see that beneath it there lies a knife.
'''         
            inventory.append("knife")
            inv = 'knife'
        else:
                dialog = '''You already inspected this item. \n'''
                
    elif item_name in ['light switch', 'switch', 'light']:
        if 'lock pick' not in inventory:
            Curent_Room = 5
            dialog = '''you walk to the light switch and turn it off and on again. 
the light stops flickering, you take a look around the room and spot a lock pick laying in the corner
''' 
            inventory.append('lock pick')
            inv = 'lock pick'
        else:
            dialog = 'You already inspected this item. \n'
                        
    elif item_name in ['garbage', 'pile']:
        if 'cheese' not in inventory:
            dialog = '''you rummage through the garbage but it's all kinda filthy.
but you find a piece of cheese and take it with you for a later snack.
'''
            inventory.append("cheese")
            inv = 'cheese'
        else:
            dialog = 'You already inspected this item. \n'
    else:
        dialog = f'''Sorry, but the item "{item_name}" that you tried to inspect isn't something that you can inspect.
'''
    Main_Game(inv)


def Inspect_Room_2(item_name):
    global dialog
    global inventory
    
    inv = ' '
    
    if item_name in ['book', 'bookshelf', 'shelf']:
        if 'martial arts' and 'lock picking' not in inventory:
            dialog = '''you look in the bookshelf and see two books in particular.
a book about martial arts and a book about lock picking.
(if you want to read a specific book you can inspect an individual book)
'''
            
        else:
                dialog = '''You already inspected these items item. \n'''
                
                
                
    elif item_name in ['martial arts', 'arts', 'martial']:
        if 'martial arts' not in inventory:
            dialog = '''you read the book of martial arts and you learn how to use them.
            
If you know the enemy and know yourself, you need not fear the result of a hundred battles. 
If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. 
If you know neither the enemy nor yourself, you will succumb in every battle.

― Sun Tzu, The Art of War 

(maybe this skill will be usefull at another point)
''' 
            inventory.append('martial arts')
            inv = 'martial arts'
        else:
            dialog = 'You already inspected this item. \n'


    elif item_name in ['lock picking', 'lock', 'picking']:
        if 'lock picking' not in inventory:
            dialog = '''you read the book about lock picking and you learn how to pick locks.
(maybe this skill will be usefull at another point)
'''
            inventory.append("lock picking")
            inv = 'lock picking'
        else:
            dialog = 'You already inspected this item. \n'
    
    elif item_name in ['window']:
        dialog = '''you walk to the window and open it you take a whif of the fresh air.
you decide you dont want to be stuck in here anymore and you commit suicide.
'''     
        inv = 'DEATH'
    
    elif item_name in ['garbage', 'pile']:
        if 'note' not in inventory:
            dialog = f'''you rumage throught the garbage and see a stick note with the code ({code})
(maybe this note will be usefull at another point)
'''
            inv = 'note'
        else:
            dialog = 'You already inspected this item. \n'
    
    else:
        dialog = f'''Sorry, but the item "{item_name}" that you tried to inspect isn't something that you can inspect.
'''
    Main_Game(inv)

def Inspect_Room_5(item_name):
    global dialog
    inv = ' '
    if item_name in ['chest']:
        code = input('wat was de code die op het briefje stond: ')
        if code == code:
            Game_Win()
        else:
            dialog = '''the code was wrong
'''
    else:
        dialog = f'''Sorry, but the item "{item_name}" that you tried to inspect isn't something that you can inspect.
'''

def use():
    global dialog
    dialog = "use"




def look():
    global dialog
    
    if Curent_Room == 1:
        dialog ='''you look around and you see a light switch.
You also see a matress on the floor and a pile of garbage.
and you see two doorways one in the east and one in west.
'''
    
    elif Curent_Room == 2:
        dialog = '''you look around the room and see the book shelf with some books sticking out in particular.
you also see a pile of garbage and a window.
and you see two doorways one in the south and one in the west.
'''
  
    elif Curent_Room == 3:
        dialog = '''you look around but dont see much besides a table with a map on it.
and you see two doorways in the north and in the west.
'''
    elif Curent_Room == 4:
        dialog = '''you look around and you see the body laying on the floor.
and you see a door on the east side.
'''
    elif Curent_Room == 5:
        dialog = '''you look around and see a chest 
and you see a door on the east
'''
    Main_Game()







def Room_Check(Player_input):
    if Curent_Room == 1:
        Room_1(Player_input)
    elif Curent_Room == 2:
        Room_2(Player_input)
    elif Curent_Room == 3:
        Room_3(Player_input)
    elif Curent_Room == 4:
        Room_4(Player_input)
    elif Curent_Room == 5:
        Room_5(Player_input)




def Room_1(Player_input):
    global Curent_Room
    global dialog
    
        
    if Player_input in ['north', 'n']:
        dialog = '''you cant move in that direction
'''
    
    elif Player_input in ['east', 'e']:
        Curent_Room = 2
        dialog = '''You walk into the room and you see a bookshelf in the corner and some more garbage on the floor.
you also see a window with light shining through. 
and you see a two doorways one on the west and anther one in the south.
'''
        
    elif Player_input in ['south', 's']:
        dialog = '''you cant move in that direction
'''

    elif Player_input in ['west', 'w']:
        if 'key' in inventory:
            Curent_Room = 5
            dialog = '''you try the key you found earlier and it fits.
you turn the key and open the door, you look around and see a chest.
you see a doorway in the east
'''
        elif 'lock pick' in inventory:
            lockpick()
            dialog = '''using the lock pick you found earlier its now your task to pick the lock.
'''
        else:
            dialog = '''you walk up to the door and try to open it but its locked
(maybe explore more to find a key)
'''


    elif Player_input in ['look', 'l']:
        look()

    elif Player_input.startswith('inv'):
        dialog = f'de items in your inventory are: \n{inventory}\n'
        
    elif Player_input.startswith('i'):
            Inspect_Item(Player_input)
            
    elif Player_input.startswith('u'):
        use()


    
    else:
        invalid(Player_input)
        
    Main_Game()




def Room_2(Player_input):
    global Curent_Room
    global dialog
    
        
    if Player_input in ['north', 'n']:
        dialog = '''you cant move in that direction
'''
    
    elif Player_input in ['east', 'e']:
        dialog = '''you cant move in that direction
'''
        
    elif Player_input in ['south', 's']:
        Curent_Room = 3
        dialog = '''you walk into the room and dont see much, execpt for a table in the corner
and two doorways one on the north and on in the west.
'''

    elif Player_input in ['west', 'w']:
        Curent_Room = 1
        dialog = '''you into the room and you see a light switch.
You also see a matress on the floor and a pile of garbage.
and you see two doorways one in the east and one in west.
'''

    elif Player_input in ['look', 'l']:
        look()

    elif Player_input.startswith('inv'):
        dialog = f'de items in your inventory are: \n{inventory}\n'
        
    elif Player_input.startswith('i'):
            Inspect_Item(Player_input)
            
    elif Player_input.startswith('u'):
        use()

    else:
        invalid(Player_input)
        
    Main_Game()



def Room_3(Player_input):
    global Curent_Room
    global dialog
    
        
    if Player_input in ['north', 'n']:
        Curent_Room = 2
        dialog = '''You walk into the room and you see a bookshelf in the corner and some more garbage on the floor.
you also see a window with light shining through. 
and you see a two doorways one on the west and anther one in the south.
'''
    
    elif Player_input in ['east', 'e']:
        dialog = '''you cant move in that direction
'''
        
    elif Player_input in ['south', 's']:
        dialog = '''you cant move in that direction
'''

    elif Player_input in ['west', 'w']:
        Curent_Room = 4
        fight()
        

    elif Player_input in ['look', 'l']:
        look()

    elif Player_input.startswith('inv'):
        dialog = f'de items in your inventory are: \n{inventory}\n'
        
    elif Player_input.startswith('i'):
            Inspect_Item(Player_input)
            
    elif Player_input.startswith('u'):
        use()

    else:
        invalid(Player_input)
        
    # Main_Game()



def Room_4(Player_input):
    global Curent_Room
    global dialog
    
        
    if Player_input in ['north', 'n']:
        dialog = '''you cant move in that direction
'''
    
    elif Player_input in ['east', 'e']:
        Curent_Room = 3
        dialog = '''you walk into the room and dont see much, execpt for a table in the corner
and two doorways one on the north and on in the west.
'''
        
    elif Player_input in ['south', 's']:
        dialog = '''you cant move in that direction
'''

    elif Player_input in ['west', 'w']:
        dialog = '''you cant move in that direction
'''
        

    elif Player_input in ['look', 'l']:
        look()

    elif Player_input.startswith('inv'):
        dialog = f'de items in your inventory are: \n{inventory}\n'
        
    elif Player_input.startswith('i'):
            Inspect_Item(Player_input)
            
    elif Player_input.startswith('u'):
        use()

    else:
        invalid(Player_input)
        
    Main_Game()



def Room_5(Player_input):
    global Curent_Room
    global dialog
    
        
    if Player_input in ['north', 'n']:
        dialog = '''you cant move in that direction
'''
    
    elif Player_input in ['east', 'e']:
        Curent_Room = 1
        dialog = '''you into the room and you see a light switch.
You also see a matress on the floor and a pile of garbage.
and you see two doorways one in the east and one in west.
'''
        
    elif Player_input in ['south', 's']:
        dialog = '''you cant move in that direction
'''

    elif Player_input in ['west', 'w']:
        dialog = '''you cant move in that direction
'''
        

    elif Player_input in ['look', 'l']:
        look()

    elif Player_input.startswith('inv'):
        dialog = f'de items in your inventory are: \n{inventory}\n'
        
    elif Player_input.startswith('i'):
            Inspect_Item(Player_input)


    else:
        invalid(Player_input)
        
    Main_Game()

def lockpick():
    print('''type the number that aligns with the pins hight
(type it without spaces between the numbers)
          
6:                 _ 
5:         _      | |
4:     _  | |     | |
3:    | |_| |  _ _| |
2:    | | | |_| | | |
1:    | | | | | | | |
''')
    code = input('code: ')
    if code == '4352336':
        Game_Win()
    else:
        lockpick()


def fight():
    global dialog
    global Curent_Room
    Curent_Room = 4
    
    os.system('cls')
    text = '''you walk into the room and you dont see anything at first.
But then a person blocks you from exiting the room.

███████╗██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
█████╗  ██║██║  ███╗███████║   ██║   
██╔══╝  ██║██║   ██║██╔══██║   ██║   
██║     ██║╚██████╔╝██║  ██║   ██║   
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

'''
    time.sleep(2)
    Write.Print(text, Colors.light_red ,interval= 0.0025)
    weapon_list = []
    if 'martial arts' in inventory:
        weapon_list.append('martial arts')
    if 'knife' in inventory :
        weapon_list.append('knife')
    if 'cheese' in inventory:
        weapon_list.append('cheese')
    if weapon_list == []:
        dialog = '''he attacks you but your not strong enough to defeat him so you lose the fight
        
██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝ 
'''     
        time.sleep(2)
        start_menu()
    else:
        Write.Print(('your weapons:', str(weapon_list)), Colors.light_blue, interval=0.0025)

        fight_command = input('\nyou atack him with: ')
        
        fight_command = fight_command.lower()
        
        if fight_command in ['cheese']:
            dialog = '''you pull the cheese out of you pockets and show your opponent the cheese.
he looks strangly at you but then shrugs and pull out a key. 
you trade the cheese for the key and walk away
'''     
            inventory.append('key')
            fight_won = True
            
        elif fight_command in ['knife']:
            dialog = '''you pull out a knife and do some moves you saw in movies.
u somehow stab him and he sags to the floor, a key falls out of his pocket and you take it.
'''
            inventory.append('key')
            fight_won = True
                    
        elif fight_command in ['martial arts', 'martialarts', 'arts', 'martial']:
            dialog = '''you remember the book you read earlier and chanel your inner bruce lee.
you do some SICK moves and impress your opponent. 
he looks a bit flabbergasted and then POW you kick him in his nuts.
he sags to the floor and a key falls out of his pocket and you take it.
'''
            inventory.append('key')
            fight_won = True
         
        else:
            dialog = f'''you stumble around and try to get your {fight_command} but you cant seem to find.
you were to slow and thus you died.

██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
   ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
   ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝ 
'''         
            time.sleep(2)
            start_menu()
    
    


def devcom(player_input):
    global Curent_Room
    
    com = input('dev console: ')
    
    if com == 'room1':
        Curent_Room = 1
        
    elif com == 'room2':
        Curent_Room = 2
        
    elif com == 'room3':
        Curent_Room = 3
    
    elif com == 'room4':
        fight()
        
    elif com  == 'room5':
        Curent_Room = 5
        
    elif com == 'addinv':
        inventory.extend(('knife', 'lock pick', 'cheese', 'martial arts', 'lock picking', 'key'))
        
    elif com == 'croom':
        print(Curent_Room)
        time.sleep(4)
    elif com == 'game':
        lockpick()


    Main_Game()


def Game_Win():
    you_win = '''██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ '''
    
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print(Colorate.Horizontal(Colors.green_to_cyan, you_win, 1))
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    time.sleep(4)
    start_menu()


def invalid(Player_input):
    os.system('cls')
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print(Colorate.Color(Colors.orange, Invalid_ascii, 1))
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print(Colorate.Color(Colors.light_red, f"the input {Player_input} was not recognized", 1))
    print(Colorate.Color(Colors.light_red, 'you can write help and get a list of commands :)', 1))

    time.sleep(2)
    Main_Game()
    
Invalid_ascii = '''██╗███╗   ██╗██╗   ██╗ █████╗ ██╗     ██╗██████╗     ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗
██║████╗  ██║██║   ██║██╔══██╗██║     ██║██╔══██╗    ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝
██║██╔██╗ ██║██║   ██║███████║██║     ██║██║  ██║    ██║██╔██╗ ██║██████╔╝██║   ██║   ██║   
██║██║╚██╗██║╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║    ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║   
██║██║ ╚████║ ╚████╔╝ ██║  ██║███████╗██║██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝   ██║   
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝ '''


def start_menu():
    os.system('cls')
    pess_to_play = '''██████╗ ██████╗ ███████╗███████╗███████╗    ███████╗███╗   ██╗████████╗███████╗██████╗     ████████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
██████╔╝██████╔╝█████╗  ███████╗███████╗    █████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝       ██║   ██║   ██║    ██████╔╝██║     ███████║ ╚████╔╝ 
██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║    ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗       ██║   ██║   ██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  
██║     ██║  ██║███████╗███████║███████║    ███████╗██║ ╚████║   ██║   ███████╗██║  ██║       ██║   ╚██████╔╝    ██║     ███████╗██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
'''
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print(Colorate.Horizontal(Colors.green_to_cyan, pess_to_play, 1))
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print('''press enter to start
hint: if your stuck somewhere you can type help to get a list of comands          
''')
    input()
    Main_Game()


Start_Scene = '''you wake up in a room on the ceiling you there is a flickering light just enough light to see around you.
you see a door in the east direction and a door in the west direction. 
further more there you see a matress and pile of some garbage and a lightswitch next to the west door

if you dont know where to start type help to see a full list of commands :)
'''    




inventory = []

dialog = Start_Scene

Curent_Room = 1

fight_won = False







start_menu()
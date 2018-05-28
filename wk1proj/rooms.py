#!/usr/bin/env python3

#Written by: Kyle Jorgensen
#This is a nine room area that keeps track of your coordinates as you navigate
#north,south,east,west. Descriptions inspired by George R.R. Martin's Song of Ice and Fire.
#Code is a little clunky at this point but it works nicely.

x = 0 #Set coordinates
y = 0
location = [x,y] #set location variable

class Room(object): #setup class for rooms
    def __init__(self,name,coords,description): #toString
        self.name = name
        self.coords = location
        self.description = description
        self.paths = [] #Not in use yet
    def describe_room(self): #function to return room description
        return self.description

    def room_coords(): #function to return room description for give coords
        if location == [0,0]:
            return start_room.describe_room()
        elif location == [-1,0]:
            return west_room.describe_room()
        elif location == [1,0]:
            return east_room.describe_room()
        elif location == [0,1]:
            return north_room.describe_room()
        elif location == [0,-1]:
            return south_room.describe_room()
        elif location == [-1,1]:
            return nw_room.describe_room()
        elif location == [1,1]:
            return ne_room.describe_room()
        elif location == [-1,-1]:
            return sw_room.describe_room()
        elif location == [1,-1]:
            return se_room.describe_room()
        else:
            print('I have no idea what I just did.')

##Big block of room names, coords, and descriptions, respectively
start_room = Room('Start',[0,0],'''
You are in TLG Learning.  You feel like you've been here before...
Perhaps forever?  The feeling of déjà vu is overwhelming.
You better get out of here ASAP.
There are exits to the North, South, East, and West.
''')
west_room = Room('West',[-1,0],'''
You are in the West. Casterly Rock looms regal in the distance.
The lion does not concern himself with the opinions of sheep.
There are exits to the North, South, and East.
''')
east_room = Room('East',[1,0],'''
You are in the East. The Knights of the Vale have mustered all of their
strength, ready for war with the the bastard, Ramsay Bolton.
There are exits to the North, South, and West.
''')
north_room = Room('North',[0,1],'''
You are in the North. The coming winter has brought snow and frigid
temperatures to the rolling hills and forests, making a hardscrabble
existence. The North remembers.
There are exits to the South, East, and West.
''')
south_room = Room('South', [0,-1],'''
You are in the South. The hot sun beats down on the rocky desert
around you as you squint your eyes and begin to sweat. You hope to
find a desert oasis to quench your growing thirst.
There are exits to the North, East, and West.
''')
nw_room = Room('Northwest',[-1,1],'''
You are in the Northwest.  The Stony Shore where you stand is presently
serving as a landing for a raiding party of Ironborn. Perhaps it's not
safe here...
There are exits to the South and East.
''')
ne_room = Room('Northeast',[1,1],'''
You are in the Northeast. House Karstark has fallen on hard times, and
the land surrounding you reveals this truth through derelict farms and
eerie quiet. War has taken its toll on these people.
There are exits to the South and West.
''')
sw_room = Room('Southwest',[-1,-1],'''
You are in the Southwest. Hightower, the lighthouse of Oldtown stands proud
before you as you revel in the sense of intellect that surrounds you. Truly
this is the greatest seat of knowledge in the world.
There are exits to the North and East.
''')
se_room = Room('Southeast', [1,-1],'''
You are in the Southeast. Here in Sunspear, House Martell rules from their
castle. Beware the treacherous Sand Snakes!
There are exits to the North and West.
''')

print (Room.room_coords(), end='') #Tell user where they start
while True: #Loop until user quits
    command = input('Where do you want to go? (or \'look\' again or \'quit\')\n') #Prompt the user
    if command.lower() == "north": #lowercase for caps fault tolerance
        if abs(location[1] + 1) > 1: #if chosen move would put user out of range
            print("You cannot go that way.")
        else:
            location[1] += 1 #increment y coord
            print('Your coordinates: ' + str(location), end='') #report coords
            print (Room.room_coords(), end='') #print room description

    elif command.lower() == "south":
        if abs(location[1] - 1) > 1:
            print("You cannot go that way.")
        else:
            location[1] -= 1 #decrement y coord
            print('Your coordinates: ' + str(location), end='')
            print (Room.room_coords(), end='')

    elif command.lower() == "east":
        if abs(location[0] + 1) > 1:
            print("You cannot go that way.")
        else:
            location[0] += 1 #increment x coord
            print('Your coordinates: ' + str(location), end='')
            print (Room.room_coords(), end='')

    elif command.lower() == "west":
        if abs(location[0] - 1) > 1:
            print("You cannot go that way.")
        else:
            location[0] -= 1 #decrement x coord
            print('Your coordinates: ' + str(location), end='')
            print (Room.room_coords(), end='')

    elif command.lower() == "quit":
        break #exit the loop
    elif command.lower() == "look":
        print (Room.room_coords(), end='') #print description again
    else:
        print("I Don't Understand that direction") #for invalid moves
print("Thanks for playing.") #exit message

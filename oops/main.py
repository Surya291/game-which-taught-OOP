from room import Room
from character import Enemy, Character,Friend
from item import Item 

backpack = []

wase = Item()
wase .set_name("Wase")
wase.set_description("A Nice decorated pot")

plate = Item()
plate .set_name("Plate")
plate.set_description("plate")

glass = Item()
glass .set_name("glass")
glass.set_description("Glass")







kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")

# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude!")

dave.set_weakness("cheese")

dining_hall.set_character(dave)
kitchen.set_item(wase)
dining_hall.set_item(glass)
ballroom.set_item(plate)


# Add a new character

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
kitchen.set_character(catrina)



current_room = kitchen

dead = False

while dead == False:
  
  print("\n")
  current_room.get_details()
  thing = current_room.get_item()
  inhabitant = current_room.get_character()
  #print(inhabitant)
  print(thing)
  if thing is not None:
	  thing.describe()
  if inhabitant is not None:
    inhabitant.describe()
  command = input("> ")
  if command == "take":
    backpack.append(thing.name)
    print(backpack)


  elif command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "fight":
    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is a Friend"
    if inhabitant == None or isinstance(inhabitant, Friend):
      print("There is no one here to fight with")
    else:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      for i in backpack:
        if i == fight_with:
          print("u have it!!")

			    		  
          if inhabitant.fight(fight_with) == True:
        # What happens if you win?
            print("Hooray, you won the fight!")
            current_room.set_character(None)
          else:
        # What happens if you lose?figt
            print("Oh dear, you lost the fight.")
            print("That's the end of the game")
            dead = True
      else:
        print("Sorry")        
  elif command == "hug":
    if inhabitant == None:
      print("There is no one here to hug :(")
    else:
      if isinstance(inhabitant, Enemy):
        print("I wouldn't do that if I were you...")
      else:
        inhabitant.hug()
      
      
  
      

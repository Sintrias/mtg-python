import random
import os
import sys

def is_basic_land(land):
    land = land.lower()
    basic_lands = ["mountain", "island", "swamp", "plain", "forest"]
    for lands in basic_lands:
        if(land == lands):
            return True
        else:
            return False
print("Welcome to deck tracker")
answer = "n"
deck_list = {}
sideboard_list = {}
while(answer == "n"):
    print("What would you like to name your deck?")
    deck_name = sys.stdin.readline()
    print("Would you like to set your deck name as "+ deck_name+ "?(y/n)")
    answer = sys.stdin.readline().rstrip()
deck_size = 0
sideboard_size = 0
count = 1
while(deck_size<60):
    print("Entry number ",count, ". Provide card name:")
    card = sys.stdin.readline().strip();
    print(card," is the card you entered is this okay?")
    answer = sys.stdin.readline().strip()
    if(answer != "y"):
        continue
    print("How many copies would you like to include?")
    answer = sys.stdin.readline().strip()
    if (is_basic_land(card)):
        deck_list[card] = int(answer)
        count += 1
        deck_size += deck_list[card]
    elif (1 <= int(answer) < 5) :
         deck_list[card] = int(answer)
         count+=1
         deck_size+=deck_list[card]
    else:
        print("You can only have 1 to 4 copies in your deck")
        continue
print("Would you like to add sideboard?(y/n")
answer = sys.stdin.readline.strip()
if(answer == 'y'):
    while(sideboard_size < 15):
        print("Provide card name:")
        card = sys.stdin.readline().strip()
        print("You entered ", card)
        print("How many copies would you like?")
        answer = sys.stdin.readline().strip()
        if(1 <= int(answer) < 5 and sideboard_size+int(answer) < 15) :
            print("You added ", answer, " copies of ", card)
            sideboard_list[card] = int(answer)
            sideboard_size+= int(answer)

        else:
            print("You can have up to 15 sideboard cards and must be within 1 to 4 cards")
        print("Add more?(y/n)")
        answer = sys.stdin.readline().strip()
        if(answer.lower() == "n"):
            break;
print("Your deck name:", deck_name)
print("Main deck list: ")
for keys, val in deck_list:
    print(keys, ":", val)
print("Your side board list: ")
for keys, val in sideboard_list:
    print(keys, ":", val)

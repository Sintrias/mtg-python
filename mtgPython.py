import random
import os
import sys

# modern_card_list = ["Path to Exile", "Thoughtseize", "Serum Visions",
#              "Fatal Push"]
# print("#1 played card in modern", modern_card_list[0])
# print(modern_card_list[1:3])
#
# standard_card_list = ["Thraben Inspector", "Gideon, Ally of Zendikar",
#                       "Negate", "Fetal Push"]
# all_card_list = [modern_card_list,standard_card_list]
# print(all_card_list)
# print("%s"%("#4 most played card in Standard : "),all_card_list[1][3])
# standard_card_list.append("Harnessed Lightening")
# standard_card_list.append("Abrade")
# standard_card_list.insert(5,"Attune with Aether")
# standard_card_list.remove("Abrade")
# standard_card_list.sort()
# standard_card_list.reverse()
# del standard_card_list[0]
# all_card_list2 = standard_card_list + modern_card_list
#
# print(len(all_card_list2))
#
# print(standard_card_list)
# print(max(all_card_list2))
# print(min(all_card_list2))

deckList = {"Liliana, the Last Hope" : 3, "Distended Mindbender" : 2, "Emrakul, the Promised End" : 1, "Nissa" : "2"}

print(deckList["Liliana, the Last Hope"])

del deckList["Nissa"]
print(deckList)
deckList["Nissa, the Vastwood Seer"] = "2"
print(deckList)
print(len(deckList))
print(deckList.get("Nissa, the Vastwood Seer"))

print(deckList.keys())
print(deckList.values())

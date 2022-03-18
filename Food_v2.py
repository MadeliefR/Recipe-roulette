# #v0.0.1
    #lijst met gerechten
    #random 1 selecteren en printen
        #print(random.choice(food_list))

#v.0.0.2 
    #lijst met gerechten 
    #random 6 gerechten selecteren en printen
    #minimaal 1x vis, 1x kip, 1x vega
   

# v.0.0.3
     # niet meer dan 2x pasta, 1x vis, 2x vega, 1x stampot, 1x soep
     # swoarma niet in combinatie met taco's
     # relationele databases 

# v.0.0.4
    #koppelen aan flask

    
# v.0.0.5  
    # ipv gerechten in strings, gerechten in afbeelding
    # recept bij weergeven (ook in afbeelding)



import random
from secrets import choice

#v0.0.2
#lijst met gerechten

#random 6 gerechten kiezen, waarvan minimaal 1x kip, 1x vega, 1x vis, 1x pasta.
    #manier 1:
        # verschillende lijsten maken per hoofd ingredient (kip, vega, vis etc)
        # dan uit elke lijst minstens 1 kiezen en dan nog random andere
    #manier 2:
        # alles in 1 lijst met de  de naam van het hoofdgerecht erbij
        # misschien in een dictionairy dat ie 1 kiest uit de keys van kip
        # of dat ie minimaal 1x een gerecht moet kiezen met het woord kip 

    #lijst met grechten, per categorie
food_chicken = ["perziken met kip", "poke bowl","Spaanse kip", 
    "oven pasta met boursin", "Noten pasta", "wok", ] 
food_vega = ["Gado gado", "groente soep", "tomaat & puntpaprika ovensoep", ]
food_fish = ["vissticks met spinazi", "Zalm, spinazi, boursin & pasta", 
    "zalm in zilverfolie", "fish quisine", "bloemkool soep & zalm"]
food_other= ["chili con carne", "winter pasta", "swoarma in courgette", 
    "loaded potato soup", "lasagne", "taco's", "boerenkool stampot", 
    "andijvie stampot", "aardapel, vlees & groente" ]
 
    # uitkiezen van aantal gerechten, per lijst
desired_number= int (input ("hoeveel recepten wil je ontvangen? : "))
pick1 = random.sample(food_other, desired_number-3)  
pick2 = random.choice(food_chicken)
pick3 = random.choice(food_vega)
pick4 = random.choice(food_fish)
food = [pick1, pick2, pick3, pick4]
print(food)








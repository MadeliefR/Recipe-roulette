
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

    #lijst met gerechten
food_list = ["perziken met kip", "chili con carne", 
"poke bowl", "winter pasta", "visticks met spinazi", 
"zalm uit de oven", "Gado gado", "shwoarma in courgette",
"Spaanse kip", "groente soep", "lasagne", "Noten pasta", 
" taco's", "boerenkool stampot", "andijvie stampot" ]

#zelf invullen van het aantal gerechten dat je terug wilt krijgen
desired_number = int (input ("hoeveel recepten wil je ontvangen? : "))
#desired_number = int(3)
food_choices = random.sample(food_list, desired_number)

    #random kiezen van 1 gerecht
print(food_choices)
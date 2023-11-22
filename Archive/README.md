# Vicky_Reigons

## What does this do?

This is a tool to parse the game Victoria 3 state_region table in map_data, which is a custmized data structure in txt file, to the standard json data structure. This is intended to help user can quickly browse, modify the table as their wishes.
My initial intention is to use this tool strip off the data from another mod. Which make it cleaner, simpler and has most compatibility to vanilla game and other mods.

## How it works

It is very crude. By modified the orignal string to json format, then edit it. Then output a string which follow the format that game in use.
It mainly use Regex for editing, perhaps there might some magic operation, which could vulnerable and not suit for all cases.
Currently I think this can only be used in state_region. Because I didn't do the research on other file. I just knew the custmized Json parser at the end of the development. But because this is just a personal hobby, I may not going too deep in this area. If the game developer(Paradox) is not going to overhaul the entire structure, currently it should be enough for my personal usage.

## Furture?

I imported the vanilla game stat_region setting in Au, and did some modification. The twisted file can be recognized by the game and mounted correctly. Next step I would like to use it to do some batch work, which migrates another mod's setting into a vanilla game friendly version.
Further development is depended on my demand.

## Perhaps doing the work manually is faster than "Automation". I really hope I am not wasting time and looks like a jester.

# Aftermath

I saw other people's code and reminds me the language parser I built in the University, which I totally forget. (Not my fault, I totally can not understand that when I was taking that course)
So I would like to rewrite the code to follow more generic parser's concept.

import sys
from gameMap import gameMap

mymap = gameMap("maps/map3.txt")
while not mymap.victory():
    print(str(mymap))
    print(mymap.pos)
    mymap.move(input("Enter a direction: ").upper())

print(str(mymap))
print("you won!!")
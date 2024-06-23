##Robert Fernandez
##Complete
##This program will show the falling distance of an object.

import distance
import math

#This will ask the user for the time it took for the object to fall.
def fallingDistance(fallingtime):
    gravity = 9.8
    distance = (1/2) * gravity * (fallingtime ** 2)
    return distance
    
#This will print the distance the object fell.
def main():
    print("Time\tFalling Distance\n--------------" )
    for currentTime in range (1, 11):
        print( currentTime,"\t      ", format(fallingDistance(currentTime), ".2f"))

main()

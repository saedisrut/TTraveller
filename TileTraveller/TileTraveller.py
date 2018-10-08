a,b = 1,1

while (a,b) != (3,1):

    if b == 1:
        val_dir = ["n", "N"]
        print ("You can travel: (N)orth.")
        
    if (a,b) == (2,2) or (a,b) == (3,3):
        val_dir = ["s", "S", "w", "W"] 
        print ("You can travel: (S)outh or (W)est.")
        
    if (a,b) == (3,2):
        val_dir = ["n", "N", "s", "S"] 
        print ("You can travel: (N)orth or (S)outh.")
        
    if (a,b) == (1,2):
        val_dir = ["n", "N", "e", "E", "s", "S"]
        print ("You can travel: (N)orth or (E)ast or (S)outh.")
        
    if (a,b) == (1,3):
        val_dir = ["e", "E", "s", "S"]
        print ("You can travel: (E)ast or (S)outh.")
        
    if (a,b) == (2,3):
        val_dir = ["w", "W", "e", "E"]
        print ("You can travel: (E)ast or (W)est.")

    direction = str(input("Direction: "))
    
    if direction not in val_dir:
        print ("Not a valid direction!")
        direction = str(input("Direction: "))

    if direction == "e" or direction == "E":
        a += 1
    if direction == "w" or direction == "W":
        a -= 1
    if direction == "n" or direction == "N":
        b += 1
    if direction == "s" or direction == "S":
        b -= 1
    
    if (a,b) == (3,1):
        print ("Victory!")

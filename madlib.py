'''
Mad Lib Function
----------------
Gets called at the end of the program to 'start' the game
'''

def madlib():
    #Asks user for input
    noun1 = input("Write in a noun")
    noun2 = input("Write in a noun")
    adj1 = input("Write in an adjective")

    #Prints out the mad lib
    print("The " + noun1 + " went to the store.")
    print("The store was all out of " + noun2)
    print("This made the " + noun1 + " feel " + adj1)


#Print Welcome Message
print("Welcome to Mad Libs!")

#Starts the MadLibs game by calling the function madlib() above
madlib()

'''
Extra credit assignments
--------------------
1. Can you add a "play again" feature that restarts the game?
2. Can you make several mad libs and the program randomly selects one for the user?

'''

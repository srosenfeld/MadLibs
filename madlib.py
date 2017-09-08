'''
Mad Lib Function
----------------
Gets called at the end of the program and plugs in variables
'''
def madlib():
    print(noun1)
    print(noun2)
    print(adj1)


#Print Welcome Message
print("Welcome to Mad Libs!")

#Asks user for input
noun1 = input("Write in a noun")
noun2 = input("Write in a noun")
adj1 = input("Write in an adjective")


#Plugs the variables into the MadLib and prints them out
madlib()


'''
Extra credit assignments
--------------------
1. Can you add a "play again" feature that restarts the game?
2. Can you make several mad libs and the program randomly selects one for the user?

'''

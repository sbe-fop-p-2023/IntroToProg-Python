# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Sam Ewald,10.08.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(objFileName, "r")
# row = objFile.readline()
for row in objFile:
    lstRow = row.split(",")
    print(lstRow)
    dicRow = {"toDoItem": lstRow[0], "priority": lstRow[1]}
    print(dicRow)
    lstTable.append(dicRow)
objFile.close()

print(lstTable)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print(lstTable)
        for dicRow in lstTable:
            print(dicRow)
            print(dicRow["toDoItem"] + ", " + dicRow["priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strItem = input("Enter the name of a chore: ")
        strPrior = input("What priority is this chore? ")
        dicRow = {"toDoItem": strItem, "priority": strPrior}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        remChore = input("Which chore do you want to remove from the list? ")
        binItemRemoved = False
        for dicRow in lstTable:
            toDoItem, priority = dict(dicRow).values()
            if toDoItem == remChore:
                lstTable.remove(dicRow)
                binItemRemoved = True
                print("\nChore complete!")
            else:
                print("\nThat's isn't on your list.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        if "yes" == str(input("Would you live to save this list? (Yes or No)")).strip().lower():
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["toDoItem"] + "," + dicRow["priority"] + "\n")
            objFile.close()
            input("List saved! Press [Enter] to return to the menu.")
        else:
            input("Data was not saved. Press [Enter] to return to the menu.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program

import classes as Manager

if __name__ == "__main__":
    Manager.printHelp()
    inputHandler = Manager.UserInputHandler()
    userInput = inputHandler.getUserInput()
    
    inputHandler.processCommand(userInput)
    
    pass
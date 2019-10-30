import classes as Manager

if __name__ == "__main__":
    inputHandler = Manager.UserInputHandler()
    while True:
        userInput = inputHandler.getUserInput()
        parseInput = inputHandler.processCommand(userInput)
        print(parseInput)
        if parseInput["command"] =="help":
            Manager.printHelp()
        # TODO:
        elif parseInput["command"] =="add":
            pass
        # TODO:
        elif parseInput["command"] =="update":
            pass
        # TODO:
        elif parseInput["command"] =="del":
            pass
        # TODO:
        elif parseInput["command"] =="reset":
            pass
        # TODO:
        elif parseInput["command"] =="simulate":
            pass
        # TODO:
        elif parseInput["command"] =="show":
            pass
        # TODO:
        else:
            pass
        

import classes as Manager

if __name__ == "__main__":
    inputHandler = Manager.UserInputHandler()
    addHandler = Manager.AddHandler()
    while True:
        userInput = inputHandler.getUserInput()
        parseInput = inputHandler.processCommand(userInput)
        print(parseInput)
        if parseInput["command"] =="help":
            Manager.printHelp()
        # TODO:
        elif parseInput["command"] =="add":
            print(parseInput['rest'])
            ret = addHandler.addAdjuster(parseInput['rest'])
            print(ret)
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
        

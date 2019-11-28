#!/usr/bin/env python3
print("Welcome To Machinery Simulation!")
print("Loading Modules...")
import classes as Manager
import matplotlib.pyplot as plt

if __name__ == "__main__":
    inputHandler = Manager.UserInputHandler()
    addHandler = Manager.AddHandler()
    editHandler = Manager.EditHandler()
    simulate = Manager.Simulate()
    

    while True:
        userInput = inputHandler.getUserInput()
        parseInput = inputHandler.processCommand(userInput)
        # print(parseInput)
        if parseInput["command"] =="help":
            Manager.printHelp()

        elif parseInput["command"] =="add":
            if parseInput["option"] == Manager.ADJ:
                # print(parseInput['rest'])
                ret = addHandler.addAdjuster(parseInput['rest'])
                
                print("Adjuster Added, success_code(id):",ret)
            elif parseInput["option"] == Manager.MCH:
                # print(parseInput['rest'])
                try:
                    ret = addHandler.addCatgeory(*parseInput['rest'])
                except expression as identifier:
                    pass
                # ret = addHandler.addCatgeory(*parseInput['rest'])
                print("Category Added, success_code",ret) 
        
        elif parseInput["command"] =="update":
        
            if parseInput["option"] == Manager.ADJ and parseInput['rest'] is not None:
                print(parseInput['rest'])
                ret = editHandler.updateAdjuster(parseInput['rest'])
                print("Adjuster Updated, success_code(id):",ret)
            elif parseInput["option"] == Manager.MCH and parseInput['rest'] is not None:
                # print(*parseInput['rest'])
                ret = editHandler.updateCategory(*parseInput['rest'])
                print("Category Updated, success_code",ret)
        
        elif parseInput["command"] =="del":
            if parseInput["option"] == Manager.ADJ and parseInput['rest'] is not None:
                ret = editHandler.deleteAdjuster(parseInput['rest'][0])
                print("Adjuster deleted ",ret)
            elif parseInput["option"] == Manager.MCH and parseInput['rest'] is not None: 
                ret = editHandler.deleteCategory(parseInput['rest'][0])
                print("Category deleted ",ret)

        
        elif parseInput["command"] =="reset":
            Manager.FileHandler().deleteAll()
            
        elif parseInput["command"] =="simulate":
            datas = simulate.calculateUtilization()
            machUtil = datas['mch']
            names = list(machUtil.keys())
            values = list(machUtil.values())
            
            plt.bar(names, values)
            plt.suptitle('Machine Utilization : 500hs') 
            plt.show()

        # TODO:
        elif parseInput["command"] =="show":
            
            fileHandler = Manager.FileHandler()
            data = fileHandler.readAll()
            print(data)        
        # TODO:
        elif parseInput["command"] =="exit":
            break;
            pass
        
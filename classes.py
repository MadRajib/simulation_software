import re
def printHelp():
    helpString = '''
Help :
* Add Machinery details to the system:
    
    add mc <Categeory name, Quantity, MTTF Value >

* Add Adjuster details to the system :
    add ad <expertise machine>

* Update Categories details in the system :
    update mc < Category name, name=new name, quantity=new value, MTTF =new value >

* Delete categories from the system :
    
    del mc <Category name>

* Update Adjuster details in the system :
    
    update ad < adjuster id, add or remove = [list of expertise machines]

* Delete Adjuster from the system :
    
    del ad <Adjuster id>

* Simulate the process :

    simulate 

* Show past results :

    show results 
    show results number=n #show last n records

* Reset the software :
    reset
''' 
    print(helpString)


class UserInputHandler():
    # TODO:
    def __init__(self, *args, **kwargs):
        self.__validCommands = ("help",
                                 "add",
                                 "update",
                                 "del",
                                 "reset",
                                 "show",
                                 "simulate",
                                )
        self.__validOptions = ("ad","mc","results")

        self.__validateRegex = {
            "mc_add" : "\s*\w+\s*[ ]\s*\d+\s*[ ]\s*\d+(\.\d+)?\s*",
            "ad_add" : "\s*\w+[ ]\s*",
            "mc_update":"",
            "ad_update":"",
            "ad_del":"\s*\d+\s*",
            "mc_del":"\s*\w+\s*",
        }
    def getUserInput(self,):
        inp = input("Please Enter Commands\n")
        line = inp.strip()
        return line #string
   
   
   
   
   
   
   
    # TODO:
    def processCommand(self,line):
        line += " ;"
        _1stArg , restArg = line.split(" ",1)
        
        restArg.strip()                       # Filter out the white spaces

        data = {
            'command':None,
            'option' : None,
            'rest':None,
        }



        # parsing commands and options
        #------------------------------------------------------------------------------

        # If 1st argument is invalid then print error
        if _1stArg not in self.__validCommands:
            print("Error: Invalid Command! - > ",_1stArg)
            return data


        data['command'] = _1stArg
        print(restArg)
        if restArg !=";":
            _2ndArg,restArg = restArg.strip().split(" ",1)
            
            if _2ndArg not in self.__validOptions:
                print("Error: Invalid Option! - > ",_2ndArg)
                return data
            data['option'] = _2ndArg
        


        # For Add
        #---------------------------------------------------------------------------
        if data["command"] == "add":

            # Match for adjuster
            if data["option"] =="ad":
                p = re.compile(self.__validateRegex['ad_add'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    return data
                else:
                    data['rest'] = restArg.strip().split()
            # match for machinery
            else:
                p = re.compile(self.__validateRegex['mc_add'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    return data
                else:
                    data['rest'] = restArg.strip().split()



        # For Update
        #------------------------------------------------------------------------------
        elif data["command"] == "update":
            
            pass
        # For delete
        #-----------------------------------------------------------------------------
        elif data["command"] == "del":
            if data["option"] == "ad":
                p = re.compile(self.__validateRegex['ad_del'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    return data
                else:
                    data['rest'] = restArg.strip().split()
            else:
                p = re.compile(self.__validateRegex['mc_del'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    return data
                else:
                    data['rest'] = restArg.strip().split()

                pass
        # For show
        # ----------------------------------------------------------------------------------------------- 
        elif data["command"] =="show":
            pass
        
        print(data)
        return data 


class Simulate():
    # TODO:
    def __init__(self, *args, **kwargs):
        pass
    # TODO:
    def calculateUtilization(self):
        data = ""
        return data #float list
    # TODO:
    def save(self):
        pass


class FileHandler():
    # Private variables
    # TODO:
    __machineryFilePath = ""
    # TODO:
    __adjusterFilePath = ""
    # TODO:
    __utilizationFilePath =""
    # TODO:
    def __init__(self, *args, **kwargs):
        pass
    # TODO:
    def readFromFile(self, name):
        data = ""
        return data # string
    # TODO:
    def writeToFile(self,name,data):
        success = ""
        return success #int
    # TODO:
    def deleteAll(self):
        pass
    # TODO:
    def searchAdjuster(self,id):
        data = ""
        return data #STRING
    # TODO:
    def searchCategory(self,name):
        data =""
        return data #stirng
     # TODO:
    def updateCategoryFile(self,option,name,qunatity,MTTF):
         sucess = ""
         return sucess #int
    # TODO:
    def updateAdjusterFile(self,option,name,qunatity,MTTF):
         sucess = ""
         return sucess #int
    # TODO:
    def updateUtilization(self,option,list):
        success= ""
        return success  #int



class AddHandler():
    # TODO:
    def __init__(self, *args, **kwargs):
        pass
    # TODO:
    def addCatgeory(self,name,quantity,MTTF):
        pass
    # TODO:
    def addAdjuster(self,expertise):
        _id =""
        return _id # id
    

class EditHandler():
    # TODO:
    def __init__(self, *args, **kwargs):
        pass
    # TODO:
    def updateCategory(self,qunatity,MTTF):
        pass
    # TODO:
    def updateAdjuster(self,option,expertise):
        pass
    # TODO:
    def deleteCategory(self,name):
        pass

    # TODO:
    def deleteAdjuster(self,id):
        pass

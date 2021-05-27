import re
from tinydb import TinyDB, Query ,where
import os

_ADJ = 0
_MCH = 1
_UTL = 2

ADJ = ("ad")
MCH = ("mc")
RSLT = ("results")

def printHelp():
    helpString = '''
Help :
* Add Machinery details to the system:
    
    add mc <Categeory name, Quantity, MTTF Value >

* Add Adjuster details to the system :
    add ad <expertise machine>

* Update Categories details in the system :
    update mc < Category name, new name,new value, new value >

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
   
    def __init__(self, *args, **kwargs):
        self.__validCommands = ("help",
                                 "add",
                                 "update",
                                 "del",
                                 "reset",
                                 "show",
                                 "exit",
                                 "simulate",
                                )
        self.__validOptions = ("ad","mc","results")

        self.__validateRegex = {
            "mc_add" : "\s*\w+\s*[ ]\s*\d+\s*[ ]\s*\d+(\.\d+)?\s*",
            "ad_add" : "\s*\w+[ ]\s*",
            "mc_update":"\s*\w+\s*[ ]\s*\w+\s*[ ]\s*\d+\s*[ ]\s*\d+(\.\d+)?\s*",
            "ad_update":"\s*\d+\s+(remove|add)\s(\s*\w+\s*)*",
            "ad_del":"\s*\d+\s*",
            "mc_del":"\s*\w+\s*",
            "show_result":"\s*\d+\s*"
        }
    def getUserInput(self):
        print()
        inp = input("Please Enter Commands\n")
        line = inp.strip()
        return line #string
   
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
            print()
            return data


        data['command'] = _1stArg
        # print(restArg)
        if restArg !=";":
            _2ndArg,restArg = restArg.strip().split(" ",1)
            
            if _2ndArg not in self.__validOptions:
                print("Error: Invalid Option! - > ",_2ndArg)
                print()
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
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]
            # match for machinery
            else:
                p = re.compile(self.__validateRegex['mc_add'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]



        # For Update
        #------------------------------------------------------------------------------
        elif data["command"] == "update":
             # Match for adjuster
            if data["option"] =="ad":
                p = re.compile(self.__validateRegex['ad_update'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]
            # match for machinery
            else:
                p = re.compile(self.__validateRegex['mc_update'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > \n")
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]

            
            pass
        # For delete
        #-----------------------------------------------------------------------------
        elif data["command"] == "del":
            if data["option"] == "ad":
                p = re.compile(self.__validateRegex['ad_del'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]
            else:
                p = re.compile(self.__validateRegex['mc_del'])
                if p.match(restArg) == None:
                    print("Error: Invalid Arguments! - > ")
                    print()
                    return data
                else:
                    temp = restArg.strip().split()
                    data['rest'] = temp[:len(temp)-1]

                pass
        # For show
        # ----------------------------------------------------------------------------------------------- 
        elif data["command"] =="show":
            p = re.compile(self.__validateRegex['show_result'])
            if p.match(restArg) == None:
                print("Error: Invalid Arguments! - > ")
                print()
                return data
            else:
                temp = restArg.strip().split()
                data['rest'] = temp[:len(temp)-1]
        
        return data 


class Simulate():
    
    def __init__(self, *args, **kwargs):
        pass
        
    # TODO:
    def calculateUtilization(self):
        datas = FileHandler().readAll()
        # print(self.datas)
        uti = {
            'mch':dict(),
            'adj':[],
        }

        machineries =  datas['mch']
        adjusters = datas['adj']
        TotalTime = 500;
        serviceTime = 10;
        for m in machineries:
            uti['mch'][m['name']] = int(m['quantity'])*TotalTime*(1- serviceTime/float(m['MTTF']))
        
        # for m in machineries:
        #     uti['mch'].append( int(m['quantity'])*TotalTime*(1- serviceTime/float(m['MTTF'])) )
            # print(uti)

        return uti #float list
    # TODO:
    def save(self):
        pass




class AddHandler():
    
    def __init__(self, *args, **kwargs):
        pass
    
    def addCatgeory(self,name,quantity=0,MTTF=0):
        data = {
            "name":name,
            "quantity":int(quantity),
            "MTTF":float(MTTF),
        }
        _id = -1
        search_result = FileHandler().searchCategory(name)
        if len(search_result)!=0 and float(search_result[0]["MTTF"])==float(MTTF):
            # print("found ",search_result)
            data["quantity"] = data["quantity"] + int(search_result[0]["quantity"])
            _id = FileHandler().updateCategory(search_result[0].doc_id,data["name"],data["quantity"],data["MTTF"])
        else:
            _id = FileHandler().writeToFile(_MCH,data)
        return _id
    
    def addAdjuster(self,expertise):
        _id = -1
        data = {
            "ident":"",
            "expertise":expertise
        }
        _id = FileHandler().writeToFile(_ADJ,data)
        return _id # id
    

class EditHandler():

    def __init__(self, *args, **kwargs):
        pass

    def updateCategory(self,name,new_name,quantity,MTTF):
        search_result = FileHandler().searchCategory(name)
        if not search_result:
            print("Sorry the Entry Doesnt Exits!")
            print()
            return -1
        return FileHandler().updateCategoryFile(search_result[0].doc_id,new_name,int(quantity),float(MTTF))
        
    def updateAdjuster(self,option,id,expertise):
        # FileHandler().updateAdjusterFile("",id,expertise)
        return 1
    def deleteCategory(self,name):
        search_result = FileHandler().searchCategory(name)
        if not search_result:
            print("Sorry the Entry Doesnt Exits!")
            print()
            return -1
        return FileHandler().deleteRow(_MCH,name)

    def deleteAdjuster(self,id):
        search_result = FileHandler().searchAdjuster(id)
        if not search_result:
            print("Sorry the Entry Doesnt Exits!")
            print()
            return -1
        return FileHandler().deleteRow(_ADJ,search_result[0].doc_id)


class FileHandler():
    # Private variables
    
    __machineryFilePath = os.path.abspath("./data/machinery.json")
    
    __adjusterFilePath = os.path.abspath("./data/adjuster.json")
    
    __utilizationFilePath =os.path.abspath("./data/simulationResult.json")
    


    def __init__(self, *args, **kwargs):
        self.mcDB = TinyDB(self.__machineryFilePath)
        self.adDB = TinyDB(self.__adjusterFilePath)
        self.utDB = TinyDB(self.__utilizationFilePath)
    
    def close_db(self):
        self.mcDB.close()
        self.adDB.close()
        self.utDB.close()
    
    # TODO:
    def readAll(self):
        data = {
            "adj":None,
            "mch":None,
        }
        data["adj"] = self.adDB.all()
        data["mch"] = self.mcDB.all()
        return data # string
    
    def writeToFile(self,name,data):
        if name == _ADJ:
            success =  self.adDB.insert(data)
            adjuster = Query()
            self.adDB.update({'ident':success}, doc_ids=[success] )
        elif name == _MCH:
            success =  self.mcDB.insert(data)
        return success #int

    def deleteAll(self):
        
        self.adDB.purge_tables()
        self.mcDB.purge_tables()
        self.utDB.purge_tables()
        
    def deleteRow(self,store,id):
        if store == _ADJ :
            self.adDB.remove(where('ident')==id)
        elif store == _MCH:
            self.mcDB.remove(where('name')==id)
            
    
    def searchAdjuster(self,id):
        adjuster = Query()
        data = self.adDB.search(adjuster.ident == int(id))
        return data #STRING

    def searchCategory(self,name):
        category = Query()
        data = self.mcDB.search(category.name == name)
        return data

    def updateCategoryFile(self,id,new_name,quantity,MTTF):
        category = Query()
        sucess = self.mcDB.update({"name": new_name, "quantity": int(quantity), "MTTF": float(MTTF)},doc_ids=[id] )
        return sucess #int
    # TODO:
    def updateAdjusterFile(self,option,name,qunatity,MTTF):
         sucess = ""
         return sucess #int
    # TODO:
    def updateUtilization(self,option,list):
        success= ""
        return success  #int


if __name__ == "__main__":
    

    # Unit test
    # InputHandler
    # AddHandler
    # editHandler
    # FileHandler
    # Simulate
    pass

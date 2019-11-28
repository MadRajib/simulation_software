import unittest
from bin.classes import UserInputHandler

class TestUserInputHandler(unittest.TestCase):
    def setUp(self):
        self.userHandler = UserInputHandler();
        self.out = {
                    "command":None,
                    "option":None,
                    "rest":None,
                }

    # Positive
    def test_help(self):
        print("Testing_pos: help")
        self.checkCommands("help",cmd="help")

    def test_mc_add(self):
        print("Testing_pos: add mc name 12 10.1")
        self.checkCommands("add mc name 12 10.1",
                            cmd="add",
                            opt="mc",
                            rst=['name','12','10.1'])

    def test_ad_add(self):
        print("Testing_pos: add ad name1 name2 name3")
        self.checkCommands("add ad name1 name2 name3",
                            cmd="add",
                            opt="ad",
                            rst=['name1','name2','name3'])
    def test_mc_update(self):
        print("Testing_pos: update mc name new_name 13 10.1")
        self.checkCommands("update mc name new_name 13 10.1",
                            cmd="update",
                            opt="mc",
                            rst=['name','new_name','13','10.1'])
    def test_delete_mc(self):
        print("Testing_pos: del mc name ")
        self.checkCommands("del mc name ",
                            cmd="del",
                            opt="mc",
                            rst=['name'])
    def test_ad_update(self):
        # print("Testing_pos: update ad 12 add mach2 name2 mach2")
        # self.checkCommands("update ad 12 add mach2 name2 mach2",
        #                     cmd="update",
        #                     opt="ad",
        #                     rst=['add','12','mach2','name2','mach2'])
        # print("Testing_pos: update ad 12 remove mach2 name2 mach2")
        # self.checkCommands("update ad 12 add mach2 name2 mach2",
        #                     cmd="update",
        #                     opt="ad",
        #                     rst=['remove','12','mach2','name2','mach2'])
        pass
        
    def test_delete_ad(self):
        print("Testing_pos: del ad 12")
        self.checkCommands("del ad 12",
                            cmd="del",
                            opt="ad",
                            rst=['12'])
    def test_delete_ad(self):
        print("Testing_pos: simulate")
        self.checkCommands("simulate",
                            cmd="simulate")
    def test_show(self):
        print("Testing_pos: show")

        self.checkCommands("show",
                            cmd="show")
    def test_show(self):
        print("Testing_pos: reset")
        self.checkCommands("reset",
                            cmd="reset")
    


    # Negative
    def test_cmd_neg(self):
        print("Testing_neg: yyyty")
        self.checkCommands("yyyty")

    def test_opt_neg(self):
        print("Testing_neg: add abc")
        self.checkCommands("add abc",cmd='add')
    


    def checkCommands(self,userip,cmd=None,opt=None,rst=None):
        userip = userip
        parseInput = self.userHandler.processCommand(userip)
        
        self.out["command"] = cmd
        self.out["option"] = opt
        self.out["rest"] = rst
        self.assertEqual(parseInput,self.out)


if __name__ == "__main__":
    unittest.main()
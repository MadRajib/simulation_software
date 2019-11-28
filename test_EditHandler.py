import unittest
from bin.classes import AddHandler,EditHandler,FileHandler

class TestEditHandler(unittest.TestCase):
    def setUp(self):
        
        self.addHandler = AddHandler();
        self.editHandler = EditHandler();
        self.fileHandler = FileHandler();

        # Start From the empty db
        self.fileHandler.deleteAll();
    
    def test_updateCategory(self):
        print("Testing_pos: addCategory")
        self.addHandler.addCatgeory("mach1",10,10.1)
        out = self.editHandler.updateCategory("mach1","new_mach1",100,20.1)
        self.assertEqual(out,[1])
    
    # TODO::
    def test_updateAdjuster(self):
        print("Testing_pos: addCategory")
        id = self.addHandler.addAdjuster("mach1 mach1 ")
        out = self.editHandler.updateAdjuster("add",id,"new_mach1 new_mach2")
        self.assertEqual(out,1)
        

    def test_deleteCategory(self):
        print("Testing_pos: deleteCategory")
        self.addHandler.addCatgeory("mach1",10,10.1)
        out = self.editHandler.deleteCategory("mach1")
        self.assertEqual(out,None)

        out = self.editHandler.deleteCategory("mach1")
        self.assertEqual(out,-1)
    
    def test_deleteAdjuster(self):
        print("Testing_pos: deleteAdjuster")
    
        id = self.addHandler.addAdjuster("mach1 mach1 ")
        out = self.editHandler.deleteAdjuster(id)
        self.assertEqual(out,None)
    
        # print("Again delete")
        out = self.editHandler.deleteAdjuster(id)
        self.assertEqual(out,-1)

if __name__ == "__main__":
    unittest.main(warnings="ignore")
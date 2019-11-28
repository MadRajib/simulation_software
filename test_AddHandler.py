import unittest
from bin.classes import AddHandler,FileHandler

class TestAddHandler(unittest.TestCase):
    def setUp(self):
        
        self.addHandler = AddHandler();
        self.fileHandler = FileHandler();

        # Start From the empty db
        self.fileHandler.deleteAll();
    
    def tearDown(self):
        self.fileHandler.deleteAll();
        pass
    
    # Positive
    def test_addCategory(self):
        print("Testing_pos: Add category")
        self.assertEqual(self.addHandler.addCatgeory("name1",10,12.1),1)
        print("Testing_pos: Add category")
        self.assertEqual(self.addHandler.addCatgeory("name2",11,12.3),2)
    
    def test_addAdjuster(self):
        print("Testing_pos: Add adjuster")
        self.assertEqual(self.addHandler.addAdjuster("name1 name2 name3"),1)
        print("Testing_pos: Add category")
        self.assertEqual(self.addHandler.addAdjuster("name2 name4 name3"),2)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
import unittest
from otherProblems import *

class TestOtherPrograms(unittest.TestCase):
    def testExtractSlice(self):
        self.assertEqual(extractSlice([1,2,3,4,5,6,7,8],2,5),[3,4,5])
    def testRotateLeft(self):
        self.assertEqual(rotateLeft([1,2,3,4,5,6],2),[3,4,5,6,1,2])
    def testRotateLeftMod(self):
        self.assertEqual(rotateLeftMod([1,2,3,4,5,6],2),[3,4,5,6,1,2])
    def testRemoveKthElem(self):
        self.assertEqual(removeKthElem([1,2,3,4,5],2),[1,2,4,5])
    def testInsertGivenPos(self):
        self.assertEqual(insertGivenPos([1,2,3,4,5],2,7),[1,2,7,3,4,5])
if __name__=='__main__':
    unittest.main()

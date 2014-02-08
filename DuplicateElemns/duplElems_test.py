import unittest
from duplElems import duplElems

class TestDuplElems(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(duplElems([]),[])
    def testWithOneElem(self):
        self.assertEqual(duplElems([1]),[1,1])
    def testWithOddElems(self):
        self.assertEqual(duplElems([1,2,3]),[1,1,2,2,3,3])
    def testWithEvenElems(self):
        self.assertEqual(duplElems([1,2,3,4]),[1,1,2,2,3,3,4,4])
if __name__=='__main__':
        unittest.main()

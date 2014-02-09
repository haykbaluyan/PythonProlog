import unittest
from sliceList import sliceList

class TestSliceList(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(sliceList([1,2,3],0),[[],[1,2,3]])
    def testOutOfBoundList(self):
        self.assertEqual(sliceList([1,2,3],4),[])
    def testNormalCase(self):
        self.assertEqual(sliceList([1,2,3,4,5],2),[[1,2],[3,4,5]])
if __name__=='__main__':
    unittest.main()

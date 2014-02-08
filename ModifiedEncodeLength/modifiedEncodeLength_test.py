import unittest
from modifiedEncodeLength import modEncodeLength

class TestModEncodeLength(unittest.TestCase):
    def setUp(self):
        pass
    def testEmptyList(self):
        self.assertEqual(modEncodeLength([]),[])
    def testNoConsecDups(self):
        self.assertEqual(modEncodeLength([1,2,3,4]),[1,2,3,4])
    def testConsecDups(self):
        self.assertEqual(modEncodeLength([1,1,2,3,3,3,3,4,4,5,1,1]),[[2,1],2,[4,3],[2,4],5,[2,1]])
print(__name__)
if __name__=='__main__':
    unittest.main()

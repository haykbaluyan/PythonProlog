import unittest
from decodeRunLength import decodeRunLength

class TestDecodeRunLength(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(decodeRunLength([]),[])
    def testNoNestList(self):
        self.assertEqual(decodeRunLength([1,2,3,4]),[1,2,3,4])
    def testWithNestList(self):
        self.assertEqual(decodeRunLength([1,2,[2,4],[5,1],'q']),[1,2,4,4,1,1,1,1,1,'q'])
if __name__=='__main__':
    unittest.main()

import unittest

class Test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    
    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
    
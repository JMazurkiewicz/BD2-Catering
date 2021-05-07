import unittest

class Test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    
    def test_string(self):
        self.assertEqual('hello', 'HeLLo'.lower())

if __name__ == '__main__':
    unittest.main()

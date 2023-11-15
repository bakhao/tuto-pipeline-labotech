import unittest
from main import reverse_list

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_reverse_list(self):
        data = [1,3,5]
        data_reversed = [5,3,1]
        self.assertEqual(reverse_list(data), data_reversed)

if __name__ == '__main__':
    unittest.main()

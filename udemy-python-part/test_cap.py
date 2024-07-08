import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
    def test_two(self):
        text = 'pratik mishra'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Pratik Mishra')

if __name__ == '__main__':
    unittest.main()
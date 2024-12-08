import unittest
from source.computer import computer_pon
from unittest.mock import patch

class TestComputer(unittest.TestCase):
    
    @patch('source.computer.random.randint')
    def test_computer_1(self, mock_randint):
        mock_randint.return_value = 1
        self.assertEqual(computer_pon(), 'グー')
    
    @patch('random.randint')
    def test_computer_2(self, mock_randint):
        mock_randint.return_value = 2
        self.assertEqual(computer_pon(), 'チョキ')
    
    @patch('random.randint')
    def test_computer_3(self, mock_randint):
        mock_randint.return_value = 3
        self.assertEqual(computer_pon(), 'パー')
    
    
if __name__ == '__main__':
    unittest.main()

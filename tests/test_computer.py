import unittest
from source.computer import computer_pon
from unittest.mock import patch

class TestComputer(unittest.TestCase):
    
    @patch('source.computer.random.choice')
    def test_computer_1(self, mock_randchoice):
        mock_randchoice.return_value = 'グー'
        self.assertEqual(computer_pon(), 'グー')
    
    @patch('source.computer.random.choice')
    def test_computer_2(self, mock_randchoice):
        mock_randchoice.return_value = 'チョキ'
        self.assertEqual(computer_pon(), 'チョキ')
    
    @patch('source.computer.random.choice')
    def test_computer_3(self, mock_randchoice):
        mock_randchoice.return_value = 'パー'
        self.assertEqual(computer_pon(), 'パー')
    
    
if __name__ == '__main__':
    unittest.main()

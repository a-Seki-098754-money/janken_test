import unittest
from source.player import player_pon
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_1(self, mock_input):
        self.assertEqual(player_pon(), 'グー')
        mock_input.assert_called_once_with("グー、チョキ、パーのいずれかを入力してください：")
    
    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_2(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
        mock_input.assert_called_once_with("グー、チョキ、パーのいずれかを入力してください：")
        
    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_3(self, mock_input):
        self.assertEqual(player_pon(), 'パー')
        mock_input.assert_called_once_with("グー、チョキ、パーのいずれかを入力してください：")
        
    @patch('builtins.input', side_effect=['0', '1'])
    def test_player_pon_0(self, mock_input):
        self.assertEqual(player_pon(), 'グー')
        self.assertEqual(mock_input.call_count, 2)  # 初回入力＋再入力の2回呼び出される
        mock_input.assert_any_call("グー、チョキ、パーのいずれかを入力してください：")
    
    @patch('builtins.input', side_effect=['4', '2'])
    def test_player_pon_4(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
        self.assertEqual(mock_input.call_count, 2)  # 初回入力＋再入力の2回呼び出される
        mock_input.assert_any_call("グー、チョキ、パーのいずれかを入力してください：")
        
if __name__ == '__main__':
    unittest.main()
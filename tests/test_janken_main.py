import unittest
from unittest.mock import patch
from source.janken_main import play_round, print_final_result

class TestJankenMain(unittest.TestCase):

    @patch('source.player.player_pon', return_value='グー')
    @patch('source.computer.computer_pon', return_value='チョキ')
    @patch('source.janken_judge.judge', return_value='player_win')
    def test_play_round_player_win(self, mock_judge, mock_computer, mock_player):
        round_num, player_win, computer_win, result = play_round(1, 0, 0)
        self.assertEqual(round_num, 2)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)
        self.assertEqual(result, 'player_win')

    @patch('source.player.player_pon', return_value='チョキ')
    @patch('source.computer.computer_pon', return_value='パー')
    @patch('source.janken_judge.judge', return_value='player_win')
    def test_play_round_player_win_2(self, mock_judge, mock_computer, mock_player):
        round_num, player_win, computer_win, result = play_round(2, 0, 1)
        self.assertEqual(round_num, 3)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 1)
        self.assertEqual(result, 'player_win')

    @patch('source.player.player_pon', return_value='グー')
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.janken_judge.judge', return_value='draw')
    def test_play_round_draw(self, mock_judge, mock_computer, mock_player):
        round_num, player_win, computer_win, result = play_round(1, 0, 0)
        self.assertEqual(round_num, 1)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 0)
        self.assertEqual(result, 'draw')

    @patch('source.player.player_pon', return_value='チョキ')
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.janken_judge.judge', return_value='computer_win')
    def test_play_round_computer_win(self, mock_judge, mock_computer, mock_player):
        round_num, player_win, computer_win, result = play_round(2, 1, 0)
        self.assertEqual(round_num, 3)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 1)
        self.assertEqual(result, 'computer_win')
        
    @patch('source.player.player_pon', return_value='パー')
    @patch('source.computer.computer_pon', return_value='チョキ')
    @patch('source.janken_judge.judge', return_value='computer_win')
    def test_play_round_computer_win_2(self, mock_judge, mock_computer, mock_player):
        round_num, player_win, computer_win, result = play_round(2, 1, 0)
        self.assertEqual(round_num, 3)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 1)
        self.assertEqual(result, 'computer_win')

    def test_print_final_result_player_win(self):
        with patch('builtins.print') as mocked_print:
            print_final_result(2, 1)
            mocked_print.assert_any_call("【最終結果】")
            mocked_print.assert_any_call("あなた: 2勝")
            mocked_print.assert_any_call("コンピュータ: 1勝")
            mocked_print.assert_any_call("あなたの総合勝利です！")

    def test_print_final_result_computer_win(self):
        with patch('builtins.print') as mocked_print:
            print_final_result(1, 2)
            mocked_print.assert_any_call("【最終結果】")
            mocked_print.assert_any_call("あなた: 1勝")
            mocked_print.assert_any_call("コンピュータ: 2勝")
            mocked_print.assert_any_call("コンピュータの総合勝利です！")

if __name__ == '__main__':
    unittest.main()
import unittest
from source.janken_judge import judge

class TestJudge(unittest.TestCase):
    def test_judge(self):
        patterns = [
            ("グー", "グー", "draw"),
            ("グー", "チョキ", "player_win"),
            ("グー", "パー", "computer_win"),
            ("チョキ", "グー", "computer_win"),
            ("チョキ", "チョキ", "draw"),
            ("チョキ", "パー", "player_win"),
            ("パー", "グー", "player_win"),
            ("パー", "チョキ", "computer_win"),
            ("パー", "パー", "draw"),
        ]
    
        for computer_hand, player_hand,  expected_result in patterns:
            with self.subTest():
                self.assertEqual(judge(player_hand, computer_hand), expected_result)

if __name__ == '__main__':
    unittest.main()

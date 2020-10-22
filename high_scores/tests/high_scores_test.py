import unittest

from src.high_scores import *

import pdb
# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.highest_scores = [3, 8, 15, 10, 2]
    # Tests

    def test_pass_latest(self):
        self.assertEqual(2, latest(self.highest_scores))

    # Test personal best (the highest score in the list)

    def test_personal_best(self):
        self.assertEqual(15, personal_best(self.highest_scores))

    # Test top three from list of scores

    def test_personal_top_three(self):
        self.assertEqual([8, 10, 15], personal_top_three(self.highest_scores))

    # Test ordered from highest tp lowest
    def test_scores_highest_to_lowest(self):
        self.assertEqual([15, 10, 8, 3, 2],
                         scores_highest_to_lowest(self.highest_scores))

    # Test top three when there is a tie
    def test_personal_top_three_tie(self):
        tie = [3, 4, 5, 4, 4]
        self.assertEqual([4, 4, 5], personal_top_three(tie))

    def test_personal_top_three_less_than_three(self):
        two = [13, 4]
        self.assertEqual([4, 13], personal_top_three(two))

    def test_personal_top_three_only_one(self):
        one = [5]
        self.assertEqual([5], personal_top_three(one))

import unittest
import bowling

game_result1 = "X4/34"
game_result2 = "X--4/34-8-/5-"
game_result3 = "пошол_на_хуй"


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_string1(self):
        points = bowling.game_result_parser(game_result1)
        self.assertEqual(points, 42)

    def test_string2(self):
        points = bowling.game_result_parser(game_result2)
        self.assertEqual(points, 70)
    #
    # def test_string3(self):
    #     points = bowling.game_result_parser(game_result3)
    #     self.assertEqual(points, 42)


if __name__ == '__main__':
    unittest.main()

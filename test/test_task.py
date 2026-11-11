import unittest
from unittest.mock import patch
from io import StringIO
from card_game.communication.ConsoleInOut import *
from card_game.card.entity.Deck import *
from card_game.Game import *
from card_game.LoadCSV import *

class test_task(unittest.TestCase):

    def test_get_input_integer(self):
        p = patch('card_game.communication.ConsoleInOut.get_string')
        mock_func = p.start()
        mock_func.return_value = 18
        self.assertEqual(get_input_integer(''), 18)
        p.stop()

    def test_get_game_info(self):
        p = patch('card_game.communication.ConsoleInOut.get_string')
        mock_func = p.start()
        mock_func.side_effect = ["Derek", 3]
        name, numPlayers = get_game_info()
        self.assertEqual(name, "Derek")
        self.assertEqual(numPlayers, 3)

    def test_get_integer_max_attempts(self):
        p = patch('card_game.communication.ConsoleInOut.get_string')
        mock_func = p.start()
        mock_func.return_value = 'abc'
        integer = get_integer()
        self.assertEqual(mock_func.call_count, 5)

    def test_get_csv_rows(self):
        p = patch('card_game.LoadCSV.create_csv_reader')
        mock_func = p.start()
        mock_func.return_value = StringIO("""Derek\nXi""")
        vals = get_csv_rows("test")
        print(vals)
        self.assertEqual(vals[1][0], "Xi")

    def test_play_a_card_from_deck_random(self):
        #Sub-task 5 – Mock Get Player Names
        pass
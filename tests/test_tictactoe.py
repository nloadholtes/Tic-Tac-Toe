from nose.tools import assert_equal
from mock import patch


from ttt.tictactoe import checkForWin, getUserInput, playGame, winningPlayer


class TestCheckForWin():
    def setUp(self):
        self.board = []
        self.messages_patch = patch.dict('ttt.tictactoe.WIN_MESSAGES', {1: "", 0: ""})
        self.messages = self.messages_patch.start()

    def tearDown(self):
        self.messages_patch.stop()

    def test_checkForWin_row_win(self):
        board = [1, 1, 1,
                 1, 0, 1,
                 0, 1, 0]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_row_1_lose(self):
        board = [1, 1, None,
                 1, 0, 1,
                 0, 1, 0]
        assert_equal(False, checkForWin(board))

    def test_checkForWin_last_row_win(self):
        board = [0, 1, 0,
                 1, 0, 1,
                 1, 1, 1]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_column_win(self):
        board = [1, 0, 0,
                 1, 0, 1,
                 1, 1, 0]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_last_column_win(self):
        board = [1, 0, 0,
                 1, 1, 0,
                 0, 1, 0]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_diagonal_win(self):
        board = [1, 0, 1,
                 0, 1, 0,
                 0, 1, 1]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_diagonal_loose(self):
        board = [None, 1, 1,
                 None, None, None,
                 None, None, None]
        # This is a condition seen while playing
        #that was due to a variable being reused
        #when a value should have been hard coded.
        assert_equal(False, checkForWin(board))

    def test_checkForWin_diagonal_win_other_diag(self):
        board = [1, 0, 0,
                 1, 0, 0,
                 0, 1, 1]
        assert_equal(True, checkForWin(board))

    def test_checkForWin_false_because_of_tie(self):
        board = [1, 0, 1,
                 0, 1, 0,
                 0, 1, 0]
        assert_equal(True, checkForWin(board))


class TestGetUserInput():

    def _check_result(self, value):
        board = [None for x in range(0, 9)]
        assert_equal(value, getUserInput(board))

    def test_getUserInput_good_keys(self):
        with patch('__builtin__.raw_input') as ri:
            for x in '123456789q':
                ri.return_value = x
                yield self._check_result, x

    def test_getUserInput_bad_keys(self):
        with patch('__builtin__.raw_input') as ri:
            inputs = ['1', 'd', 'x']
            ri.side_effect = lambda: inputs.pop()
            board = [None for x in range(0, 9)]
            output = getUserInput(board)
            assert_equal('1', output)
            assert_equal(3, len(ri.call_args_list))


class TestPlayGame():
    @patch('__builtin__.raw_input')
    def test_loose(self, ri):
        inputs = ['4', '7']
        ri.side_effect = lambda: inputs.pop()
        playGame(winningPlayer)

    @patch('__builtin__.raw_input')
    def test_quit(self, ri):
        inputs = ['4', 'q']
        ri.side_effect = lambda: inputs.pop()
        playGame(winningPlayer)

    @patch('__builtin__.raw_input')
    def test_computer_win_diag(self, ri):
        inputs = ['3', '4', '8']
        ri.side_effect = lambda: inputs.pop()
        playGame(winningPlayer)

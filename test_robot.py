import unittest
import pytest
from table import Table

class TestTableAndRobot:
    table = Table()

    @pytest.mark.parametrize(
        "x, y, face, expected",
        [
            ("a", "b", "south", "Unable to place robot, coordinates should be a number. a,b."),
            ("1", "2", "Mac", "Unrecognize direction Mac."),
            ("1", "5", "north", "Unable to place robot, improper coordinates. 1,5."),
            ("1", "2", "Mac", "Unrecognize direction Mac."),
        ]
    )
    def test_place(self, x, y, face, expected):
        assert self.table.execute_cmd("PLACE", x_axis=x, y_axis=y, face=face) == expected

    def test_move(self):
        pass

    def test_left(self):
        pass

    def test_right(self):
        pass

    def test_report(self):
        pass 
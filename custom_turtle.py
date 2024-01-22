from collections import OrderedDict
from y_position import YPosition
class CustomTurtle:
    @staticmethod
    def get_turtles():
        y_pos = YPosition()
        return OrderedDict([
            ('red', y_pos.get_position()),
            ('orange', y_pos.get_position()),
            ('yellow', y_pos.get_position()),
            ('green', y_pos.get_position()),
            ('blue', y_pos.get_position()),
            ('purple', y_pos.get_position()),

        ])

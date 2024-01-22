class YPosition:
    def __init__(self):
        self.__number = -100

    def get_position(self):
        self.__number = self.__number + 30
        return self.__number
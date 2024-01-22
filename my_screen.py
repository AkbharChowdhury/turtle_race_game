from turtle import Screen


class MyScreen:

    @staticmethod
    def screen(title='Turtle Game'):
        screen = Screen()
        screen.setup(width=500, height=400)
        screen.title(title)
        return screen

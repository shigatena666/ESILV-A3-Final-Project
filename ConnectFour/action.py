class Action:

    def __init__(self, x, y):

        # an action is defined with an x and y coordonate.
        self.__x = x
        self.__y = y

    def get_x(self):

        # return the x coordonate.
        return self.__x

    def get_y(self):

        # return the y coordonate.
        return self.__y
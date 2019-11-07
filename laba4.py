import math
import os
import random
import re
import sys


class Robot:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, direction):
        if direction == "left":
            self._x -= 1
        elif direction == "right":
            self._x += 1
        elif direction == "up":
            self._y += 1
        else:
            self._y -= 1
        print("(" + str(self._x) + ", " + str(self._y) + ")")

    def format_position(self):
        return (self._x, self._y)

    def X(self):
        return self._x

    def Y(self):
        return self._y


def distance_to_origin(robot):
    distance = round(math.sqrt(robot.X() ** 2 + robot.Y() ** 2), 1)
    print(distance)


if __name__ == '__main__':
    initial_position = input().split()
    moves = input().split()

    bot = Robot(x=float(initial_position[0]), y=float(initial_position[1]))

    for i in moves:
        bot.move(i)
        bot.format_position()
        distance_to_origin(bot)


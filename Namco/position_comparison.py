import numpy as np
import os


class PositionComparison:
    def check_collision(self) -> None:
        """
        Checks whether Pacman picked up a dot and increases the score accordingly
        :return: -
        """
        for dot in self.dots:
            if dot == tuple(self.pacman):
                # If Pacman moved on a dot, increase the score and remove the dot
                self.score += 1
                self.dots.remove(dot)

        for wall in self.wall:
            if wall == tuple(self.pacman):
                # If Pacman moved on a wall, terminate game
                self.wall_hit = true


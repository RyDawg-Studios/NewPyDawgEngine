import pygame
from content.game import Game
import os

pygame.init()
masterGame = Game(path=os.path.dirname(__file__))

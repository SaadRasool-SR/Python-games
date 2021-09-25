# Pong V3 ( Full Version of the game)
# In this version the movement of the paddle is added and has been assigned to proper keys.
# The Score is updated and the game end if any of the player reaches max score of 11
# The Ball bounces from the front of the paddles but not from the back
# Each player is given a score if the ball collides with surface between other player's paddle
# importing required modules
from uagame import Window
import pygame
import time
from pygame.locals import*

# User-defined functions


def main():

    window = Window('Pong', 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

# User-defined classes


class Game:
    # An object in this class represents a complete game.

    def __init__(self, window):
        # Initialize a Game.
        # self is the Game to initialize
        # window is the uagame window object
        # surface = pygame.display.get_surface()
        # Surface_height = surface.get_height()
        Paddle_length = 50
        Paddle_width = 10
        Paddle_Coord = [400, 150]
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.001  # smaller number the faster game
        self.close_clicked = False
        self.continue_game = True
        self.center = [250, 250]
        self.small_ball = Ball('white', 5, [self.center[0], self.center[1]], [
                               1, 2], self.window.get_surface())
        self.paddle_1 = Rectangle(
            'white', [Paddle_Coord[0], Paddle_Coord[1], Paddle_width, Paddle_length], self.window.get_surface())
        self.paddle_2 = Rectangle(
            'white', [Paddle_Coord[0]-300, Paddle_Coord[1], Paddle_width, Paddle_length], self.window.get_surface())
        self.score = Score(self.small_ball, self.window.get_surface(), self.window)
        pygame.key.set_repeat(20, 20)

    def play(self):
        # Play the game until the player presses the close box.
        # self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_event()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            time.sleep(self.pause_time)  # set game velocity by pausing

    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # self is the Game whose events will be handled

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # self is the Game to draw

        self.window.clear()
        self.small_ball.draw()
        self.paddle_1.draw()
        self.paddle_2.draw()
        self.score.draw_score()
        self.window.update()

    def update(self):
        # Update the game objects.
        # self is the Game to update
        self.small_ball.move()
        self.small_ball.Collide(self.paddle_1, self.paddle_2)
        self.score.update_score()
        self.paddle_1.move()
        self.paddle_2.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        # self is the Game to check
        if self.score.game_over():
            self.continue_game = False


class Ball:
    # An object in this class represents a colored ball.

    def __init__(self, color, radius, center, velocity, surface):
        # Initialize a ball.
        # self is the ball to initialize
        # center is a list containing the x and y int
        # coords of the center of the ball
        # radius is the int pixel radius of the ball
        # color is the pygame.Color of the ball
        # window is the uagame window object

        self.color = pygame.Color(color)
        self.radius = radius
        self.center = center
        self.velocity = velocity
        self.surface = surface
        self.increase_score_1 = False
        self.increase_score_2 = False

    def move(self):
        # Move the circle.
        # self is the Circle to move
        # checks if the ball has collided with the left and the right surface.
        size = self.surface.get_size()
        for coordinate in range(0, 2):
            self.center[coordinate] = (self.center[coordinate] + self.velocity[coordinate])
            if self.center[coordinate] < self.radius:
                self.velocity[coordinate] = -self.velocity[coordinate]
                if coordinate == 0:
                    self.increase_score_1 = True
            elif self.center[coordinate] > size[coordinate] - self.radius:
                self.velocity[coordinate] = -self.velocity[coordinate]
                if coordinate == 0:
                    self.increase_score_2 = True

    def draw(self):
        # drawing the object circle filled with color
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    # method that checks if the ball in colliding with any of the 2 paddles, if True, changes the direction of the ball.
    def Collide(self, paddle_1, paddle_2):
        if paddle_1.rectangle.collidepoint(self.center[0], self.center[1]) and self.center[0] <= paddle_1.area[0] + self.velocity[0] and self.velocity[0] > 0:
            self.velocity[0] = -self.velocity[0]
        elif paddle_2.rectangle.collidepoint(self.center[0], self.center[1]) and self.center[0] >= (paddle_2.area[0] + paddle_2.area[2] + self.velocity[0]) and self.velocity[0] < 0:
            self.velocity[0] = -self.velocity[0]


class Rectangle:
    # An object in this class represents a reactangle
    def __init__(self, color, area, surface):

        self.color = pygame.Color(color)
        self.area = area
        self.surface = surface
        self.rectangle = Rect(self.area[0], self.area[1], self.area[2], self.area[3])

    # Method that moves the paddle
    def move(self):
        self.rectangle = Rect(self.area[0], self.area[1], self.area[2], self.area[3])
        size = self.surface.get_size()
        paddle_speed = 2
        key_list = pygame.key.get_pressed()
        if self.area[1] >= 0 and self.area[1] + self.area[3] <= size[1]:
            if self.area[0] < size[0] // 2:
                if key_list[K_q] == True:
                    self.area[1] = self.area[1] - paddle_speed
                if key_list[K_a] == True:
                    self.area[1] = self.area[1] + paddle_speed
            elif self.area[0] >= size[0]//2:
                if key_list[K_p] == True:
                    self.area[1] = self.area[1] - paddle_speed
                if key_list[K_l] == True:
                    self.area[1] = self.area[1] + paddle_speed
        if self.area[1] <= 0:
            self.area[1] = 0
        if self.area[1] + self.area[3] >= size[1]:
            self.area[1] = size[1] - self.area[3]

        self.rectangle = Rect(self.area[0], self.area[1], self.area[2], self.area[3])

    # draws the rectangle
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.area)


class Score:
    # a class that represents the object score
    # store the score of each player
    def __init__(self, small_ball, surface, window):
        self.small_ball = small_ball
        self.surface = surface
        self.window = window
        self.max_score = 11  # max score allowed
        self.player_1 = 0  # initial score of the player_1
        self.player_2 = 0  # initial score of the player_2
        self.window.set_font_size(72)  # setting font size of the score
        self.window.set_font_color('white')  # setting font color of the string

    # updating score
    def update_score(self):
        if self.small_ball.increase_score_1 == True:
            self.player_1 = self.player_1 + 1
            self.small_ball.increase_score_1 = False
        elif self.small_ball.increase_score_2 == True:
            self.player_2 = self.player_2 + 1
            self.small_ball.increase_score_2 = False

    # draw's the score
    def draw_score(self):
        player_2_string = str(self.player_2)
        player_1_string = str(self.player_1)
        self.window.draw_string(player_2_string, 0, 0)
        self.window.draw_string(player_1_string, self.window.get_width() -
                                self.window.get_string_width(player_1_string), 0)

    # game over condition is the max score is reached
    def game_over(self):
        max_score_reached = False
        if self.player_2 >= self.max_score or self.player_1 >= self.max_score:
            max_score_reached = True
        else:
            max_score_reached = False
        return max_score_reached


main()

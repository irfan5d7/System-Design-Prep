import random
from typing import List, Tuple


# Core classes (Square, Snake, Ladder, Board)

class Square:
    def __init__(self, position):
        self.position = position


class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Board:
    def __init__(self, size, snakes, ladders):
        self.squares = [Square(i) for i in range(1, size + 1)]
        self.snakes = {snake.start: snake.end for snake in snakes}
        self.ladders = {ladder.start: ladder.end for ladder in ladders}

    def get_destination(self, position):
        if position in self.snakes:
            return self.snakes[position]
        elif position in self.ladders:
            return self.ladders[position]
        return position


# Singleton Die

class Die:
    _instance = None

    @staticmethod
    def get_instance():
        if Die._instance is None:
            Die._instance = Die()
        return Die._instance

    def roll(self):
        return random.randint(1, 6)


# Player and PlayerFactory

class Player:
    def __init__(self, name, order):
        self.name = name
        self.position = 1
        self.order = order

    def move(self, steps, board):
        new_position = self.position + steps
        if new_position <= len(board.squares):
            self.position = board.get_destination(new_position)


class PlayerFactory:
    @staticmethod
    def create_players(names: List[str]):
        return [Player(name, i) for i, name in enumerate(names)]


# BoardComponentFactory

class BoardComponentFactory:
    @staticmethod
    def create_snakes(snake_positions: List[Tuple[int, int]]):
        return [Snake(start, end) for start, end in snake_positions]

    @staticmethod
    def create_ladders(ladder_positions: List[Tuple[int, int]]):
        return [Ladder(start, end) for start, end in ladder_positions]


# Observer Pattern

class Observer:
    def update(self, player_name: str, position: int, roll: int):
        pass


class ConsoleObserver(Observer):
    def update(self, player_name: str, position: int, roll: int):
        print(f"{player_name} rolled a {roll} and moved to {position}")


# Singleton Game

class Game:
    _instance = None

    @staticmethod
    def get_instance(player_names: List[str], snake_positions: List[Tuple[int, int]],
                     ladder_positions: List[Tuple[int, int]]):
        if Game._instance is None:
            Game._instance = Game(player_names, snake_positions, ladder_positions)
        return Game._instance

    def __init__(self, player_names: List[str], snake_positions: List[Tuple[int, int]],
                 ladder_positions: List[Tuple[int, int]]):
        snakes = BoardComponentFactory.create_snakes(snake_positions)
        ladders = BoardComponentFactory.create_ladders(ladder_positions)
        self.board = Board(100, snakes, ladders)
        self.players = PlayerFactory.create_players(player_names)
        self.die = Die.get_instance()
        self.current_player_index = 0
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self, player: Player, roll: int):
        for observer in self.observers:
            observer.update(player.name, player.position, roll)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        roll = self.die.roll()
        current_player.move(roll, self.board)

        self.notify_observers(current_player, roll)

        if self.check_winner():
            print(f"{current_player.name} wins!")
            return True

        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False

    def check_winner(self):
        current_player = self.players[self.current_player_index]
        return current_player.position == len(self.board.squares)


# Example game setup

snake_positions = [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19),
                   (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
ladder_positions = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84),
                    (36, 44), (51, 67), (71, 91), (80, 100)]

# Get the game instance
game = Game.get_instance(["Alice", "Bob", "Charlie"], snake_positions, ladder_positions)

# Adding observers
console_observer = ConsoleObserver()
game.add_observer(console_observer)

# Play the game
while True:
    if game.play_turn():
        break

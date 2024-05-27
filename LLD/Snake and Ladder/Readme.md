## Problem Statement:

Develop a text-based implementation of the Snakes and Ladders game. The game should support multiple players and follow the standard rules of Snakes and Ladders. Players take turns rolling a die and move their tokens accordingly on the board. The game ends when one of the players reaches the last square of the board.

## Functional Requirements:

1. **Game Initialization:**
   - Allow the user to specify the number of players and their names.
   - Initialize the game board with snakes and ladders at predefined positions.

2. **Player Turns:**
   - Players take turns rolling a six-sided die.
   - Move the player token according to the result of the die roll.
   - If a player lands on the bottom of a ladder, move the token to the top of the ladder. If a player lands on the head of a snake, move the token to the tail of the snake.

3. **Game End:**
   - Declare the winner when a player reaches the last square of the board.

4. **Observers:**
   - Notify observers (e.g., console output) of game events such as player movements and die rolls.

## Classes:

1. **Square Class:**
   - Represents each square on the board.
   - Attributes:
     - `position`: Integer representing the position of the square on the board.

2. **Snake Class:**
   - Represents a snake in the game.
   - Attributes:
     - `start`: Integer representing the start position of the snake.
     - `end`: Integer representing the end position of the snake.

3. **Ladder Class:**
   - Represents a ladder in the game.
   - Attributes:
     - `start`: Integer representing the start position of the ladder.
     - `end`: Integer representing the end position of the ladder.

4. **Board Class:**
   - Manages the game board.
   - Attributes:
     - `squares`: List of Square objects representing the squares on the board.
     - `snakes`: Dictionary mapping the start position of each snake to its end position.
     - `ladders`: Dictionary mapping the start position of each ladder to its end position.
   - Methods:
     - `get_destination(position)`: Returns the destination position after moving from the given position, considering any snakes or ladders.

5. **Die Class:**
   - Represents a six-sided die for rolling.
   - Implements the Singleton pattern to ensure only one instance exists.
   - Methods:
     - `roll()`: Rolls the die and returns a random integer between 1 and 6.

6. **Player Class:**
   - Represents a player in the game.
   - Attributes:
     - `name`: String representing the player's name.
     - `position`: Integer representing the player's current position on the board.
     - `order`: Integer representing the player's order of play.
   - Methods:
     - `move(steps, board)`: Moves the player's token on the board according to the number of steps rolled.

7. **PlayerFactory Class:**
   - Implements the Factory pattern to create Player objects.
   - Methods:
     - `create_players(names)`: Creates and returns a list of Player objects based on the provided names.

8. **BoardComponentFactory Class:**
   - Implements the Factory pattern to create Snake and Ladder objects.
   - Methods:
     - `create_snakes(snake_positions)`: Creates and returns a list of Snake objects based on the provided start and end positions.
     - `create_ladders(ladder_positions)`: Creates and returns a list of Ladder objects based on the provided start and end positions.

9. **Observer Interface:**
   - Defines the `update` method to be implemented by concrete observers.

10. **ConsoleObserver Class:**
    - Implements the Observer pattern to observe game events and print them to the console.
    - Methods:
      - `update(player_name, position, roll)`: Prints the player's name, roll, and new position to the console when notified.

11. **Game Class:**
    - Manages the overall game.
    - Implements the Singleton pattern to ensure only one instance exists.
    - Attributes:
      - `board`: Board object representing the game board.
      - `players`: List of Player objects representing the players in the game.
      - `die`: Die object for rolling the die.
      - `current_player_index`: Integer representing the index of the current player.
      - `observers`: List of Observer objects observing the game.
    - Methods:
      - `add_observer(observer)`: Adds an observer to the list of observers.
      - `remove_observer(observer)`: Removes an observer from the list of observers.
      - `notify_observers(player, roll)`: Notifies all observers of a player's move and die roll.
      - `play_turn()`: Manages a single turn of the game, including rolling the die, moving the player, checking for a winner, and updating the current player.
      - `check_winner()`: Checks if a player has reached the last square of the board, indicating a winner.


## Design Patterns Used:

1. **Factory Pattern:**
   - Used for creating players, snakes, and ladders.
   - `PlayerFactory` creates player objects based on the provided names.
   - `BoardComponentFactory` creates snake and ladder objects based on their start and end positions.

2. **Singleton Pattern:**
   - Applied to the `Die` class to ensure there is only one instance throughout the game for rolling dice.
   - Applied to the `Game` class to ensure there is only one instance of the game, allowing consistent access to game state and preventing multiple game instances.

3. **Observer Pattern:**
   - Implemented to notify observers of game events such as player movements and die rolls.
   - `Observer` interface defines the `update` method, and `ConsoleObserver` implements it to print game events to the console.

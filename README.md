# Rock Paper Scissors Game

## Introduction
The classic game of ‘Rock Paper Scissors’ is played between two players in which each player simultaneously forms one of three shapes with their outstretched hand. These shapes are "rock", "paper", and "scissors". In this project, we have digitized this classic game, allowing players to face off against a computer bot in two modes: **Singleplayer** and **Multiplayer**.

The main objective is to score the highest points by winning rounds.

## Game Modes

### 1. **Singleplayer**
In Singleplayer mode, the player competes against the computer. The player can decide how many rounds they want to play. If the player wins more than half of the rounds, they are declared the winner.

### 2. **Multiplayer**
In Multiplayer mode, multiple players can compete against the computer. The program keeps track of each player’s score. At the end of the game, the player with the highest score is declared the winner.

## Rulebook:
- **Rock** beats **Scissors**.
- **Scissors** beats **Paper**.
- **Paper** beats **Rock**.
- Winning a match earns you +1 point.
- Losing a match earns you 0 points.
- A draw results in no points.

## How to Play:
- For **Rock**, type `r` or `rock`.
- For **Paper**, type `p` or `paper`.
- For **Scissors**, type `s` or `scissors`.

The player is given a choice of how many rounds they want to play against the bot. All players play the specified number of rounds. At the end, the player(s) with the highest score win.

## Features:
- Two game modes: **Singleplayer** and **Multiplayer**.
- Score tracking for each round.
- ASCII art for visual representation of Rock, Paper, and Scissors.
- Handles invalid inputs and provides instructions.
- Displays the winner at the end of the game.

## Example:
```
Welcome to the game of ROCK PAPER SCISSORS

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
If you win a match, you get +1 points.
If you lose a match, you get none.
In the case of a draw, you do not get any points.

...

How many players? 2
How many rounds? 3
```

## Installation:
To play this game, simply clone the repository and run the `rock_paper_scissors.py` file. Ensure that Python is installed on your system.

```bash
git clone https://github.com/yourusername/rock-paper-scissors.git
cd rock-paper-scissors
python rock_paper_scissors.py
```



## Acknowledgments:
- ASCII art used in the game was sourced from [gist.github.com](https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe).


This README file covers the game introduction, modes, rules, and setup instructions. It also includes the key parts of the code for easy reference.

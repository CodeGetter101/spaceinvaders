#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.opponents_last_move = random.choice(moves)

    def move(self):
        return self.opponents_last_move

    def learn(self, my_move, their_move):
        self.opponents_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = random.choice(moves)

    def move(self):
        index = moves.index(self.my_last_move)
        if index == 3:
            return moves[0]
        else:
            return moves[index - 1]

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


class Human(Player):

    def move(self):
        Human_move = ""

        while True:
            Human_move = input(
                "Rock, Paper, or Scissors:? "
                ).lower()

            if Human_move.lower() not in moves:
                print("Please Try Again")
            else:
                break
        return Human_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0
        self.rounds = 0

    def ask_rounds(self):
        while True:
            num_rounds = input(
                "How many round would you like to play?: ")
            if num_rounds.isnumeric():
                num_rounds = int(num_rounds)
                if num_rounds <= 0:
                    print ("Please pick a valid number:  ")
                elif num_rounds > 9:
                    print ("Max number of rounds is 5. Try Again:  ")
                else:
                    print(f"Cool! Lets's play {num_rounds} rounds!")
                    self.rounds = num_rounds
                    break
            else:
                print("Try Again Please.")

    def choose_opponent(self):
        print(
            "\nChoose a Player You Want to Face"
            "\n[1] Player 1 always plays 'rock'."
            "\n[2] Player 2 chooses its moves randomly."
            "\n[3] Player 3 remembers what you did previous round."
            "\n[4] Player 4 cycles through the three moves."
            "\n ")
        while True:
            opponent_choice = (input("Enter your choice now: "))
            if opponent_choice == "1":
                self.p2 = Player()
                break
            elif opponent_choice == "2":
                self.p2 = RandomPlayer()
                break
            elif opponent_choice == "3":
                self.p2 = ReflectPlayer()
                break
            elif opponent_choice == "4":
                self.p2 = CyclePlayer()
            break
        else:
            print("I'm sorry. I didnt understand, please try again.")

    def keep_score(self, move1, move2):

        if beats(move1, move2):
            self.p1wins += 1
            print(f"{move1} beats {move2}! Player 1 wins this round!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")
        elif beats(move2, move1):
            self.p2wins += 1
            print(f"{move2} beats {move1}! Player 2 wins this round!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")
        else:
            self.ties += 1
            print("It's a tie!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")

    def show_final_score(self):
            print("Final Score:")
            print(f"Player One: {self.p1wins}")
            print(f"Player Two: {self.p2wins}")
            print(f"Ties: {self.ties}")

    def play_round(self):
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.keep_score(move1, move2)
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)

    def play_game(self):

            print("Want to play Rock Paper Scissors?! ")
            while True:
                ready = input("Are you ready? Type y to play, or q to exit.")
                if ready == 'y' or ready == 'yes':
                    break
                elif ready == 'quit':
                    print("Ok. Come back when you're ready ")
                    break
                else:
                    print("Try again.")
            self.ask_rounds()
            self.choose_opponent()
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for round in range(0, self.rounds):
                print(f"Round {round+1}: ")
                self.play_round()
            self.show_final_score()
if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.play_game()

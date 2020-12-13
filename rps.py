#!/usr/bin/env python3
import random

# Store all possibilities in a list all functions can access
from typing import List

options: list[str] = ["rock", "paper", "scissors"]


def info():
    # return possible options
    answer: str = "the possibilities are " + options
    return answer


def play(pinput):
    # check if the players input is valid
    if pinput in options:
        n = len(options)
        r = random.randint(0, n - 1)
        binput = options[r]
        # check for winner
        if pinput == "rock" and binput == "rock":
            return "I chose " + binput + ", noone won!"
        if pinput == "rock" and binput == "paper":
            return "I chose " + binput + ", I won!"
        if pinput == "rock" and binput == "scissors":
            return "I chose " + binput + ", you won!"

        if pinput == "paper" and binput == "rock":
            return "I chose " + binput + ", you won!"
        if pinput == "paper" and binput == "paper":
            return "I chose " + binput + ", noone won!!"
        if pinput == "paper" and binput == "scissors":
            return "I chose " + binput + ", I won!"

        if pinput == "scissors" and binput == "rock":
            return "I chose " + binput + ", I won"
        if pinput == "scissors" and binput == "paper":
            return "I chose " + binput + ", you won!!"
        if pinput == "scissors" and binput == "scissors":
            return "I chose " + binput + ", noone won!"
        else:
            answer = "something weird happened"
            return answer
    else:
        answer = 'Something is off here, did you check you submitted your choice in lower case and it is one of ' + options + '?'

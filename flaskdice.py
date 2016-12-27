from flask import Flask, jsonify
import json
import random


app = Flask(__name__)


@app.route('/')
@app.route('/roll')
@app.route('/roll/dice/<int:num_dice>/sides/<int:sides>/')
def roll(num_dice=2, sides=6):
    return jsonify(dice_roll(num_dice, sides))

@app.route('/loadedroll')
@app.route('/loadedroll/dice/<int:num_dice>/sides/<int:sides>/<bias>')
def loaded_roll(num_dice=2, sides=6, bias=27):
    return jsonify(loaded_dice(num_dice, sides, bias))


def dice_roll(num_dice, sides):
    """
        Generates a dice roll taking the number of dice and sides as an argument.
        If numbers are higher than 100 or lower than 1 it will default to 2, 6 sided
        die. 
    """
    result = {}
    if (sides >= 100 or num_dice >= 100) is True:
        sides=6
        num_dice=2
    elif (sides <= 0 or num_dice <= 0) is True:
        sides=6
        num_dice=2
    for dice in range(0, num_dice):
        result['Dice ' + str(dice + 1)] = random.randint(1, int(sides))
    return result


def loaded_dice(num_dice, sides, bias):
    """
        Generates a 'loaded' roll. Takes number of dice and sides
        as well as an integer argument named bias. a list of combinations
        of the sides is combined with a list of the biased numbers and
        a random choice is generated, while the more a number appears the
        more likely it is selected.
    """
    result = {}
    # creates a list of sides from 1 til highest number and removes 0
    side_list = list(range(sides + 1))
    side_list.pop(0)
    # creates a list from bias
    bias_list = [int(x) for x in bias]
    # creates a new list combining the side_list and bias
    loaded_list = side_list + bias_list
    # creates a random selection in the loaded_list
    for dice in range(0, num_dice):
        result['Dice ' + str(dice + 1)] = random.choice(loaded_list)
    return result


if __name__ == '__main__':
    app.debug = True
    app.run()

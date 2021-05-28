#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 28, 2021
# This program displays every RGB colours

import constants


def main():
    # declare variables
    counter_red = 0
    counter_green = 0
    counter_blue = 0

    # nested loop that generates all values of RGB colours
    for counter_red in range(constants.MAX_COLOUR_VALUE + 1):
        for counter_green in range(constants.MAX_COLOUR_VALUE + 1):
            for counter_blue in range(constants.MAX_COLOUR_VALUE + 1):
                print("RGB ({0}, {1}, {2})\
". format(counter_red, counter_green, counter_blue))


if __name__ == "__main__":
    main()

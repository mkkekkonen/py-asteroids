'''
This module contains the function that loads the high scores from a file.
'''

import os

FILE_NAME = 'high_scores.txt'


def load_high_scores() -> list[dict[str, int]]:
    '''
    Loads the high scores.
    '''

    file_exists = os.path.exists(FILE_NAME)

    high_scores = []

    if file_exists:
        with open(FILE_NAME, 'r', encoding='utf8') as high_scores_file:
            high_scores = high_scores_file.readlines()
            high_scores = [parse_high_score(line) for line in high_scores]

    return high_scores


def parse_high_score(line: str):
    '''
    Parses a high score line.
    '''
    split_line = line.strip().split(' ')
    name = split_line[0]
    time = int(split_line[1])
    return {'name': name, 'time': time}

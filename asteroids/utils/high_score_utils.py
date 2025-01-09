'''
This module contains the function that loads the high scores from a file.
'''

import os

FILE_NAME = 'high_scores.txt'


def load_high_scores() -> list:
    '''
    Loads the high scores.
    '''

    file_exists = os.path.exists(FILE_NAME)

    high_scores = []

    if file_exists:
        with open(FILE_NAME, 'r', encoding='utf8') as high_scores_file:
            high_scores = high_scores_file.readlines()

    return high_scores

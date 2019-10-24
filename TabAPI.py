"""
file: TabAPI.py
purpose: Class that handles requests to the R6Tab API
author: rml1168@rit.edu (Ryan Lei)
author: jdesig8@aol.com (Jordan Disciglio)
"""

import requests

PLATFORM = 'uplay'
SEARCH_BY_USERNAME = 'https://r6tab.com/api/search.php'
SEARCH_BY_ID = 'https://r6tab.com/api/player.php'

users = dict()


def find_by_username(username):
    """
    Use the first returned search result to get the player id
    :param username: Uplay username
    :return: player id given by ubisoft
    """
    response = requests.get(SEARCH_BY_USERNAME, params={'platform': PLATFORM, 'search': username}).json()
    return response['results'][0]['p_id']


def get_rank(p_id):
    """
    Get a players rank
    :param p_id: player id given by ubisoft
    :return: rank as an int
    """
    response = requests.get(SEARCH_BY_ID, params={'p_id': p_id}).json()
    return int(response['seasonal']['current_NA_mmr'])


def add_to_dict(user, p_id, rank):
    """
    Add to the dictionary that stores players
    :param user: discord user object
    :param p_id: ubisoft given player id
    :param rank: current rank
    :return:
    """
    global users
    value = [p_id, rank]
    users[user] = value


def get_users():
    """
    Simple getter for users
    :return: users dictionary
    """
    return users

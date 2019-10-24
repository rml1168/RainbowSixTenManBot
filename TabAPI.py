"""
file: TabAPI.py
purpose: Util file that handles requests to the R6Tab API
author: rml1168@rit.edu (Ryan Lei)
author: jdesig8@aol.com (Jordan Disciglio)
"""

import requests

PLATFORM = 'uplay'
SEARCH_BY_USERNAME = 'https://r6tab.com/api/search.php'
SEARCH_BY_ID = 'https://r6tab.com/api/player.php'
FAILURE = "FAIL"

users = dict()


def find_by_username(username):
    """
    Use the first returned search result to get the player id
    :param username: Uplay username
    :return: player id given by ubisoft
    """
    response = requests.get(SEARCH_BY_USERNAME, params={'platform': PLATFORM, 'search': username}).json()
    if int(response['totalresults']) > 1:
        return "FAIL"
    return response['results'][0]['p_id']


def get_rank(p_id):
    """
    Get a players rank
    :param p_id: player id given by ubisoft
    :return: rank as an int
    """
    response = requests.get(SEARCH_BY_ID, params={'p_id': p_id}).json()
    return int(response['seasonal']['current_NA_mmr'])

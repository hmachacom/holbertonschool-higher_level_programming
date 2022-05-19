#!/usr/bin/python3
"""Progress vs Score  Task Body Write a Python script that takes
in a URL, sends a request to the URL and displays the value of the
` X-Request-Id `   variable found in the header of the response."""

import requests

if __name__ == "__main__":

    url = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(url.text)))
    print('\t- content: {}'.format(url.text))

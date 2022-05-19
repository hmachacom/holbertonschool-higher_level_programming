#!/usr/bin/python3
"""Progress vs Score  Task Body Write a Python script that takes
in a URL, sends a request to the URL and displays the value of the
` X-Request-Id `   variable found in the header of the response."""

import requests
import sys

if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)

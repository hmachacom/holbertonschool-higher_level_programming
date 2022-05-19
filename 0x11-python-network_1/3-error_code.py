#!/usr/bin/python3
"""Progress vs Score  Task Body Write a Python script that takes
in a URL, sends a request to the URL and displays the value of the
` X-Request-Id `   variable found in the header of the response."""

if __name__ == "__main__":

    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

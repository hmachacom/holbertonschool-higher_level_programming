#!/usr/bin/python3
"""Progress vs Score  Task Body Write a Python script that takes
in a URL, sends a request to the URL and displays the value of the
` X-Request-Id `   variable found in the header of the response."""

if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        answer = response.read().decode('utf-8')
    print(answer)

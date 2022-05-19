#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as status:
        statusHtml = status.read()
        print("Body response:")
        print("\t- type: {}".format(type(statusHtml)))
        print("\t- content: {}".format(statusHtml))
        print(
            "\t- utf8 content: {}"
            .format(statusHtml.decode("utf-8", "replace"))
            )

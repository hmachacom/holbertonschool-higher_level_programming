#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)
    if long == 0:
        return (long, None)
    else:
        return (long, sentence[0])

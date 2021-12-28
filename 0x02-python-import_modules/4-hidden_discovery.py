#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list = sorted(dir(hidden_4))
    for lis in list:
        if lis[0] != "_" and lis[1] != "_":
            print(lis)

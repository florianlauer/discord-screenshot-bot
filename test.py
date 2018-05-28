from mss import mss

with mss() as sct:
    for filename in sct.save():
        print(filename)

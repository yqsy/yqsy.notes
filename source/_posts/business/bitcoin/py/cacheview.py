import struct
import sys

import plyvel


def main():
    if len(sys.argv) < 2:
        print("usage: cacheview.py {indexdirectory}")
        exit(0)

    db = plyvel.DB(sys.argv[1])

    for k,v in db.iterator():
        if k[0] == ord('b'):
            print("{0}".format((k[1:])[::-1].hex()))
            print("{0}".format(v.hex()))
    db.close()


if __name__ == "__main__":
    main()
